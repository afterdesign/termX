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

2. Its not working for me.

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
