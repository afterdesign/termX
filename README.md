[![endorse](https://api.coderwall.com/afterdesign/endorsecount.png)](https://coderwall.com/afterdesign)

# Terminal plugin for sublime

1. Fully packaged
2. Currently with option to open new tab on OS X (works fine on 10.8)
3. Sublime Text 3 beta support

# How to install ?
### From git:
```
cd $PATH_OF_SUBLIME_PACKAGES
git clone git://github.com/afterdesign/MacTerminal.git
```

### From [package control](http://wbond.net/sublime_packages/package_control)
Just type MacTerminal

# FAQ
1. How do I use this ?

    Just use "ctrl+command+t" while editing file to open terminal with cd to directory where the file exists.

    You can also use the "Open in terminal" option in sidebar.

2. How can I change shortcut ?

    Go to:

    ```
    Sublime Text 2 -> Preferences     -> Package Settings -> Macterminal -> Key Bindings - User
    ```
    and add something like:

    ```
    { "keys": ["super+t"], "command": "open_mac_terminal" }
    ```

3. The "Open in terminal" is greyed out.
    This happens when there is no opened file and for now I don't know if
    this is just a sublime bug or I need to change something.
        For now I saw the same behavior in

4. How to I use it with iTerm 2 ?
    Simply go to:

    ```
    Sublime Text 2 -> Preferences -> Package Settings -> Macterminal -> Settings - User
    ```

    and add:

    ```
    {
        "terminal"   :  "iterm"
    }
    ```

    If you wish you can also change it in Settings - Default.

5. How do I change path to ``` osascript ``` ?

    To check what is path for ``` osascript ``` just open terminal and type:

    ```
    which osascript
    ```

    With path simply go to:

    ```
    Sublime Text 2 -> Preferences -> Package Settings -> Macterminal -> Settings - User
    ```

    and add:

    ```
    {
        "osascript"   :  "/usr/bin/osascript"
    }
    ```

6. Can I always open main directory of project ?

    From version 2.0 you can.

    Open:
    ```
    Sublime Text 2 -> Preferences -> Package Settings -> Macterminal -> Settings - User
    ```

    And set :
    ```
    {
        "directory_mode" : "project"
    }
    ```

    From now on if you have only 1 directory added to project it's going to be opened by default.
    If you have more than 1 directory in your project you'll see quickpanel to select what you would like to open.

    ![](https://raw.github.com/afterdesign/MacTerminal/master/messages/macterminal_2.gif)

    Thanks [@dirajkumar](https://github.com/dirajkumar) for the idea !

7. Its not working for me.

    First of all enable ```debug``` mode. To do this open your settings and add:
    ``` "debug": true ```

    After this try to open terminal again. If it's not working (and debug shouldn't repair the problem)
    open sublime console (default shortcut is ``` ctrl+` ```) and open new issue with log
    between ```---MacTerminal Debug Start---``` and ```---MacTerminal Debug End---```.

    You can always ping me on [twitter](http://twitter.com/afterdeign) or
    simply write [issue on github](https://github.com/afterdesign/MacTerminal/issues).

# Contact

You can follow me on twitter: [@afterdesign](http://twitter.com/afterdesign)
or find me on coderwall: [@afterdesign](http://coderwall.com/afterdesign)
or find me on g+: [+RafałMalinowski](https://plus.google.com/+RafałMalinowski)

# License

Licensed under the [MIT license](http://opensource.org/licenses/MIT).