# If You like this project - hit it with a star ツ

# 10.10.2013 version 1.4.7

---

1. Resolved issue with ST3 by adding .no-sublime-package to download whole package not just create .sublime-package


# 10.08.2013 version 1.4.2

---

1. Resolved issue with going to path when plugin is used from "Open in terminal" menu.
2. Updated package to new package manager schema.

# 06.07.2013 version 1.4.1

---

1. Resolved issue #13 - problems with print function in sublime text 3

# 28.07.2013 version 1.4

---

1. Added Debug mode.
    When plugin is not working correctly you can turn on debug mode with ```'debug': true``` in settings.
    After that please use again plugin and send me log from sublime console (default shortcut is ``` ctrl+` ```).
    Just copy text between "---MacTerminal Debug Start---" and "---MacTerminal Debug End---" and paste it to issue.

2. Updated Terminal applescript.
    I found that Terminal can have problems with speed between commands so I've added small delays.
    Looks like it does the trick.

3. Updated links in packages.json to codeload.github.com

4. Added tags and updated packages.json to download code from tag.

5. Updated readmes.

# 23.03.2013

---

Added option to define ``` osascript ``` path because some of you may have problem with PATHs.
From now by path to ``` osascript ``` it's set to ``` /usr/bin/osascript ``` and can be changed in settings.
More info in [issue #8](https://github.com/afterdesign/MacTerminal/issues/8).

For more info how to setup ``` osascript ``` path just checkout [README.md](https://github.com/afterdesign/MacTerminal)

Added "Open in terminal" to command palette.

---

# 30.01.2013

---

Some minor (print call) changes and MacTerminal is working with Sublime Text 3 beta !

Thanx to ap0 (https://github.com/ap0) there is default_path to fallback if there is a problem with file path.

There is also some interesting information from Thomas Noe
about possible issue for people using dropbox for project syncing:
https://github.com/afterdesign/MacTerminal/issues/6#issuecomment-11831154

---



# 25.12.2012

---

Changed default keybinding to "ctrl+cmd+t" due to global bindings problems
explained in [issue 5](https://github.com/afterdesign/MacTerminal/issues/5)

---

Added support for iTerm 2. Just go to:

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

---

Added full support for opening terminal from sidebar.
Just right click on file or directory and use "Open in terminal".
For now there is no support for multiple selected files in sidebar.

---

Added simple FAQ on main project site. If you have any questions just
ping me on [twitter](http://twitter.com/afterdeign) or
simply write [issue on github](https://github.com/afterdesign/MacTerminal/issues).

---
