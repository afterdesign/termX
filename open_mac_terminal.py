# -*- coding: utf-8 -*-
'''
Sublime text plugin that opens terminal.
'''

import os
import pipes
import sublime
import platform
import subprocess
import sublime_plugin
from pprint import pprint
from decimal import Decimal

class PathPicker(object):
    '''
    Class to manage paths for files
    '''

    def __init__(self, view, selected_paths, directory_mode):
        self.view = view
        self.selected_paths = selected_paths
        self.directory_mode = directory_mode

    def fetch_paths(self):
        """
        Get list of paths
        """
        paths = self.get_paths_for_selected_items()
        paths = self.get_project_paths(paths)
        paths = self.get_path_for_currently_open_file(paths)

        return list(set(paths))

    def get_paths_for_selected_items(self):
        '''
        Get paths for selected items in sidebar.
        '''

        paths_to_choose = []
        for single_path in self.selected_paths:
            if os.path.isdir(single_path):
                paths_to_choose.append(single_path)
            else:
                paths_to_choose.append(os.path.dirname(single_path))

        return paths_to_choose

    def get_project_paths(self, paths):
        '''
        Get all root directories for project.
        '''

        if len(paths) > 0:
            return paths

        if self.directory_mode != 'project':
            return paths

        paths = paths + self.view.window().folders()

        return paths

    def get_path_for_currently_open_file(self, paths): # pylint: disable=invalid-name
        '''
        Get paths for currently open tab in sublime
        '''
        if len(paths) > 0:
            return paths

        if self.directory_mode != 'file':
            return paths

        if self.view.file_name() is not None:
            paths.append(os.path.dirname(self.view.file_name()))

        elif self.view.window().active_view().file_name() is not None:
            paths.append(os.path.dirname(self.view.window().active_view().file_name()))

        else:
            paths = paths + self.view.window().folders()

        return paths

class OpenMacTerminal(sublime_plugin.TextCommand):
    '''
    Class is opening new terminal window with the path of current file
    '''

    def __init__(self, *args, **kwargs):
        sublime_plugin.TextCommand.__init__(self, *args, **kwargs)

        self.settings = sublime.load_settings('MacTerminal.sublime-settings')
        self.paths = []
        self.debug_info = {}

    def run(self, *dummy, **kwargs):
        '''
        This method is invoked by sublime
        '''

        selected_paths = kwargs.get('paths', [])

        # get settings
        directory_mode = self.settings.get('directory_mode', 'file')

        # temporary hack for old configurations
        if directory_mode not in ('project', 'file'):
            directory_mode = 'file'

        paths_picker = PathPicker(self.view, selected_paths, directory_mode) # pylint: disable=no-member
        self.paths = paths_picker.fetch_paths()
        self.open_terminal()

        self.debug_info['directory_mode'] = directory_mode
        self.debug_info['paths'] = self.paths

        debug(self.debug_info, self.settings.get('debug', False))

    def open_terminal(self):
        '''
        Choose what to open - terminal with current path or quick selection window
        '''
        if len(self.paths) == 0:
            return False

        if len(self.paths) == 1:
            self.open_terminal_command(self.paths[0])
            return True

        self.show_directory_selection()

    def show_directory_selection(self):
        '''
        Open quick selection window with paths
        '''

        self.view.window().show_quick_panel( # pylint: disable=no-member
            self.paths,
            self.open_selected_direcotory,
            sublime.MONOSPACE_FONT
        )

    def open_selected_direcotory(self, selected_index):
        '''
        This method is invoked by sublime quick panel
        '''
        if selected_index == -1:
            return False

        self.open_terminal_command(self.paths[selected_index])

    def open_terminal_command(self, path):
        '''
        Open terminal with javascript/applescript
        '''

        quoted_path = pipes.quote(path)
        command = []

        # get osascript from settings or just use default value
        command.append(self.settings.get('osascript', '/usr/bin/osascript'))

        if Decimal(".".join(platform.mac_ver()[0].split(".")[:2])) >= Decimal('10.10'):
            ext_language = 'js'
        else:
            ext_language = 'scpt'

        # set path and terminal
        applescript_path = '{packages_dir}/MacTerminal/macterminal_{terminal_name}.{ext}'.format(
            packages_dir=sublime.packages_path(),
            terminal_name=self.settings.get('terminal', 'terminal'),
            ext=ext_language
        )

        command.append(applescript_path)
        command.append(quoted_path)

        #open terminal
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=None)
        (out, err) = proc.communicate()

        self.debug_info['ext_language'] = ext_language
        self.debug_info['cmd'] = ' '.join(command)
        self.debug_info['process_out'] = out
        self.debug_info['process_err'] = err

def debug(debug_info, debug_mode):
    '''
    show some debug stuff when needed
    '''
    if not debug_mode:
        return False

    pprint("---MacTerminal DEBUG START---")
    pprint(debug_info)
    pprint("---MacTerminal DEBUG END---")
