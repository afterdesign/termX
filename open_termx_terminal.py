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


def get_paths_from_selection(selection):
    '''
    Get paths for selected items in sidebar.
    '''
    paths = []
    for single_path in selection:
        if os.path.isdir(single_path):
            paths.append(single_path)
        else:
            paths.append(os.path.dirname(single_path))

    return paths


def get_root_paths(view):
    '''
    Get all root directories for project
    '''
    return view.window().folders()


def get_file_path(view):
    '''
    Get the directory of the current file
    '''
    file = view.file_name()
    if file is not None:
        p = []
        p.append(os.path.dirname(file))
        return p

    file = view.window().active_view().file_name()
    if file is not None:
        p = []
        p.append(os.path.dirname(file))
        return p


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

        project = kwargs.get('project', False)
        if project:
            paths = get_root_paths(self.window.active_view())
        else:
            paths = get_paths_from_selection(kwargs.get('paths', []))

        if not paths:
            paths = get_file_path(self.window.active_view())

        self.paths = paths
        self.debug_info['paths'] = self.paths
        debug(self.debug_info)

        if len(self.paths) == 1:
            self.open_terminal_command(self.paths[0])
        elif len(self.paths) > 1:
            self.window.show_quick_panel(
                self.paths,
                self.open_selected_directory
            )

    def open_selected_directory(self, selected_index):
        '''
        This method is invoked by sublime quick panel
        '''
        if selected_index != -1:
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
        debug(self.debug_info)


def debug(debug_info):
    '''
    show some debug stuff when needed
    '''
    settings = sublime.load_settings('termX.sublime-settings')
    if settings.get('debug'):
        pprint("---termX DEBUG START---")
        pprint(debug_info)
        pprint("---termX DEBUG END---")
