# Sublime Text terminal plugin for macs

1. Fully packaged
2. Currently with option to open new tab
3. Sublime Text 2 and 3

# Installation
### From git:
```
cd $PATH_OF_SUBLIME_PACKAGES
git clone git://github.com/afterdesign/termX.git
```

### From [package control](http://wbond.net/sublime_packages/package_control)
Just type termX


# Keybinding

Default keybinding is:

```
ctrl+cmd+t
```

To change it go to:

```
Sublime Text 2 -> Preferences -> Package Settings -> termX -> Key Bindings
```

And set something similar to:

```json
{ "keys": ["ctrl+super+t"], "command": "open_termx_terminal" }
```

# Alternative terminals:

By default this plugin is using native ```Terminal.app```.
You can also use [iTerm2](http://iterm2.com) and (thanks to awesome [@JohnBehnke](https://github.com/JohnBehnke)) [Hyper](http://hyper.is).

To change settings edit:

```
Sublime Text 2 -> Preferences -> Package Settings -> termX -> Settings - User
```

And change terminal setting to ```iterm``` (default is ```terminal```):

```json
{
    "terminal"   :  "terminal/iterm/hyper"
}
```

# Terminal opening strategy

By default termX is opening terminal with path to directory where currently edited file is placed.

You can change this behavious by editing settings file:

```
Sublime Text 2 -> Preferences -> Package Settings -> termX -> Settings - User
```

Default option is ```file``` and you can change it to ```project```:

```json
{
    "directory_mode" : "file/project"
}
```

# FAQ

1. The "Open in terminal" is greyed out.
    This happens when there is no opened file and for now I don't know if
    this is just a sublime bug or I need to change something.
        For now I saw the same behavior in


2. How do I change path to ``` osascript ``` ?

    To check what is path for ``` osascript ``` just open terminal and type:

    ```
    which osascript
    ```

    With path simply go to:

    ```
    Sublime Text 2 -> Preferences -> Package Settings -> termX -> Settings - User
    ```

    and add:

    ```
    {
        "osascript"   :  "/usr/bin/osascript"
    }
    ```

3. Can I always open main directory of project ?

    From version 2.0 you can.

    Open:
    ```
    Sublime Text 2 -> Preferences -> Package Settings -> termX -> Settings - User
    ```

    And set :
    ```
    {
        "directory_mode" : "project"
    }
    ```

    From now on if you have only 1 directory added to project it's going to be opened by default.
    If you have more than 1 directory in your project you'll see quickpanel to select what you would like to open.

    ![](https://raw.github.com/afterdesign/termX/master/messages/termx_2.gif)

    Thanks [@dirajkumar](https://github.com/dirajkumar) for the idea !

4. Its not working for me.

    First of all enable ```debug``` mode. To do this open your settings and add:
    ``` "debug": true ```

    After this try to open terminal again. If it's not working (and debug shouldn't repair the problem)
    open sublime console (default shortcut is ``` ctrl+` ```) and open new issue with log
    between ```---termX Debug Start---``` and ```---termX Debug End---```.

    You can always ping me on [twitter](http://twitter.com/afterdeign) or
    simply write [issue on github](https://github.com/afterdesign/termX/issues).

# Contact

All info about me you can find on my "goto page": [http://malinowski.be](https://malinowski.be) or just ping me on twitter: [@afterdesign](http://twitter.com/afterdesign)

# License

Licensed under the [MIT license](http://opensource.org/licenses/MIT).
