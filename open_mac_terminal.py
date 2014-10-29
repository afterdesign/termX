# -*- coding: utf-8 -*-
#pylint: disable-msg=E1101, F0401
'''
Sublime text plugin that opens terminal.
'''

import sublime_plugin
import os
import sublime
import subprocess
import pipes
import platform
from pprint import pprint

PROJECT_FOLDERS = []

class OpenMacTerminal(sublime_plugin.TextCommand):#pylint: disable-msg=R0903,W0232
    '''
    Class is opening new terminal window with the path of current file
    '''

    def run(self, edit, paths = None):#pylint: disable-msg=W0613
        '''
        Sublime text run

        @param edit: sublime.Edit
        @param paths: paths from sidebar
        '''
        #clear directories list
        del PROJECT_FOLDERS[:]

        #get settings
        settings = sublime.load_settings('MacTerminal.sublime-settings')
        terminal_name = settings.get("terminal")
        directory_mode = settings.get("directory_mode") or "default"

        if len(terminal_name) == 0:
            return

        if directory_mode == "project":
            path = self.get_first_project_directory()

        if directory_mode != "project" or path == None:
            path = self.get_current_path(paths)

        run_command(path)

    def get_first_project_directory(self):
        '''
        Open first directory on list of folders in sidebar.
        '''
        if len(self.view.window().folders()) == 1:
            return self.view.window().folders()[0]

        elif len(self.view.window().folders()) > 1:
            for folder in self.view.window().folders():
                PROJECT_FOLDERS.append(folder)

            self.view.window().show_quick_panel(
                PROJECT_FOLDERS,
                run_with_selected_direcotory,
                sublime.MONOSPACE_FONT
            )
            return None

        else:
            return None

    def get_current_path(self, paths):
        '''
        Get path to directory selected from sidebar or directory of selected file.
        '''

        if paths is not None and len(paths) == 1:
            path = os.path.dirname(paths[0])

        elif self.view.file_name() is not None:
            path = os.path.dirname(self.view.file_name())

        elif self.view.window().active_view().file_name() is not None:
            path = os.path.dirname(self.view.window().active_view().file_name())

        elif len(self.view.window().folders()) > 0:
            return self.get_first_project_directory()

        else:
            raise Exception("This may be a bug, please enable debug mode and create issue on github")

        return path

def run_with_selected_direcotory(index):
    '''
    Open directory selected in quickpanel
    '''
    if index == -1:
        return

    run_command(PROJECT_FOLDERS[index])

def run_command(path):
    '''
    Open terminal in selected directory
    '''
    if path is None or len(path) == 0:
        return
        # raise Exception("This may be a bug, please enable debug mode and create issue on github")

    path = pipes.quote(path)

    settings = sublime.load_settings('MacTerminal.sublime-settings')
    debug_settings = settings.get("debug")
    terminal_name = settings.get("terminal")
    directory_mode = settings.get("directory_mode") or "default"

    # set command to run applescript
    command = []

    # get osascript from settings or just use default value
    command.append(settings.get("osascript") or "/usr/bin/osascript")

    if '10.10' in platform.mac_ver()[0]:
        ext_language = 'js'
    else:
        ext_language = 'scpt'

    # set path and terminal
    applescript_path = "{packages_dir}/MacTerminal/macterminal_{terminal_name}.{ext}".format(
        packages_dir=sublime.packages_path(),
        terminal_name=settings.get("terminal"),
        ext=ext_language
    )

    command.append(applescript_path)

    command.append(path)

    #open terminal
    if debug_settings:
        proc = subprocess.Popen(command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            startupinfo=None
        )
        (out, err) = proc.communicate()

        debug(
            {
                'out':out,
                'err':err
            },
            command,
            terminal_name,
            directory_mode
        )
    else:
        subprocess.Popen(command)

def debug(process, command, terminal_name, directory_mode):
    '''
    show some debug stuff when needed
    '''
    debug_info = {}
    debug_info['cmd'] = ''.join(command)
    debug_info['out'] = process['out']
    debug_info['err'] = process['err']
    debug_info['terminal_name'] = terminal_name
    debug_info['directory_mode'] = directory_mode
    print("---MacTerminal DEBUG START---")
    pprint(debug_info)
    print("---MacTerminal DEBUG END---")
