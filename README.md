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


6. Its not working for me.

    Well then check your python console in sublime (default shortcut is ``` ctrl+` ```) 
    and you can always ping me on [twitter](http://twitter.com/afterdeign) or 
    simply write [issue on github](https://github.com/afterdesign/MacTerminal/issues).
    

# Contact

You can follow me on twitter: [@afterdesign](http://twitter.com/afterdesign)

# License

Licensed under the [MIT license](http://opensource.org/licenses/MIT).