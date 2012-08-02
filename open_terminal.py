# -*- coding: utf-8 -*-
'''
Sublime text plugin that opens terminal.
'''

import sublime_plugin
import os
import sublime
import subprocess

class OpenTerminal(sublime_plugin.TextCommand):#pylint: disable-msg=R0903,W0232
    '''
    Class is opening new terminal window with the path of current file  
    '''

    def run(self, edit):#pylint: disable-msg=W0613
        '''
        Sublime text run
        
        @param edit: sublime.Edit
        '''

        #get settings
        settings = sublime.load_settings('Terminal.sublime-settings')

        #if user set packages_dir than replace it
        command = [subcommand % {"packages_dir" : sublime.packages_path()} for subcommand in settings.get("command")]

        #add path
        command.append(os.path.dirname(self.view.file_name()))#pylint: disable-msg=E1101

        #open terminal
        subprocess.Popen(command)#pylint: disable-msg=E1101