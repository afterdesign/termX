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

    def __init__(self, view, selected_paths):
        self.view = view
        self.selected_paths = selected_paths

    def fetch_paths(self):
        """
        Get list of paths
        """
        paths = []
        paths += self.get_paths_from_selected_paths()
        if not paths:
            paths += self.get_project_paths()

        return list(set(paths))

    def get_paths_from_selected_paths(self):
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

    def get_project_paths(self):
        '''
        Get all root directories for project
        '''
        settings = sublime.load_settings('termX.sublime-settings')
        directory_mode = settings.get('directory_mode')

        if directory_mode == 'project':
            return self.view.window().folders()
        else:
            if self.view.file_name() is not None:
                p = []
                p.append(os.path.dirname(self.view.file_name()))
                return p
            elif self.view.window().active_view().file_name() is not None:
                p = []
                p.append(os.path.dirname(self.view.window().active_view().file_name()))
                return p
            else:
                return self.view.window().folders()


class OpenTermxTerminal(sublime_plugin.WindowCommand):

    '''
    Class is opening new terminal window with the path of current file
    '''

    def __init__(self, *args, **kwargs):
        sublime_plugin.WindowCommand.__init__(self, *args, **kwargs)

        self.settings = sublime.load_settings('termX.sublime-settings')
        self.paths = []
        self.debug_info = {}

    def run(self, *dummy, **kwargs):
        '''
        This method is invoked by sublime
        '''

        selected_paths = kwargs.get('paths', [])
        paths_picker = PathPicker(self.window.active_view(), selected_paths)
        self.paths = paths_picker.fetch_paths()
        self.open_terminal()
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

        self.window.show_quick_panel(  # pylint: disable=no-member
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
        version = '.'.join(platform.mac_ver()[0].split(".")[:2])
        if Decimal(version) >= Decimal('10.10'):
            ext_language = 'js'
        else:
            ext_language = 'scpt'

        # set path and terminal
        tpl = '{packages_dir}/termX/termx_{terminal_name}.{ext}'
        applescript_path = tpl.format(
            packages_dir=sublime.packages_path(),
            terminal_name=self.settings.get('terminal', 'terminal'),
            ext=ext_language
        )

        command.append(applescript_path)
        command.append(quoted_path)

        # open terminal
        proc = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                startupinfo=None)
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

    pprint("---termX DEBUG START---")
    pprint(debug_info)
    pprint("---termX DEBUG END---")
