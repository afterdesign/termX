# Sublime Text terminal plugin for macOS

Fully packaged and able to open in a new tab.

Install via [Package Control](http://wbond.net/sublime_packages/package_control), or clone the repo into your packages directory.


## Keybinding
Default keybinding is `ctrl+cmd+t`. To change it go to:

```
Sublime Text -> Preferences -> Package Settings -> termX -> Key Bindings
```


## Settings
To change settings go to:

```
Sublime Text -> Preferences -> Package Settings -> termX -> Settings
```

The available options will be explained in the left hand panel.


### Alternative terminals:

By default this plugin uses the native `Terminal.app`.
You can also use [iTerm2](http://iterm2.com) and (thanks to awesome [@JohnBehnke](https://github.com/JohnBehnke)) [Hyper](http://hyper.is).


### Terminal opening strategy

By default termX opens a new terminal in directory of the current file. You can change this to open in the current directory.


## FAQ

1. The "Open in terminal" is greyed out.
    This happens when there is no opened file and for now I don't know if
    this is just a sublime bug or I need to change something.
 

2. Can I always open main directory of project ?

    Edit the settings and change `directory_mode` to `project`:
    ```
    {
        "directory_mode" : "project"
    }
    ```

    From now on if you have only 1 directory added to project it's going to be opened by default.
    If you have more than 1 directory in your project you'll see quickpanel to select what you would like to open.

    ![](https://raw.github.com/afterdesign/termX/master/messages/termx_2.gif)

    Thanks [@dirajkumar](https://github.com/dirajkumar) for the idea !

3. Its not working for me.

    First of all enable `debug` mode. 
    To do this open your settings and add: `"debug": true`

    After this try to open terminal again. If it's not working
    open the Sublime Text console and open new issue with the log
    between ```---termX Debug Start---``` and ```---termX Debug End---```.

    You can always ping me on [twitter](http://twitter.com/afterdeign) or
    simply write [issue on github](https://github.com/afterdesign/termX/issues).

## Contact

All info about me you can find on my "goto page": [http://malinowski.be](https://malinowski.be) or just ping me on twitter: [@afterdesign](http://twitter.com/afterdesign)

## License

Licensed under the [MIT license](http://opensource.org/licenses/MIT).
