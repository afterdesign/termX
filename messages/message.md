# If You like this project - hit it with a star ツ

Default keybinding is "ctrl+cmd+t" !

---

SETTINGS:

    Sublime Text 2 -> Preferences -> Package Settings -> termX ->

OPTIONS:

    {
        "terminal" : "terminal/iterm",
        "osascript" : "/usr/bin/osascript",
        "debug" : false/true,
        "directory_mode" : "file/project"
    }


---

directory_mode: "file"

    DEFAULT
    open path with currently opened file/currently chosen file in sidebar

directory_mode: "project"

    always open top project directory (if there is one) or dialog to select one of top directories

---

terminal: "terminal"

    DEFAULT
    open Terminal.app

terminal: "iterm"

    open iterm2.app (version 3)

---

debug: false

    DEFAULT
    don't print debug message in sublime console

debug: true

    print debug message in sublime console

---

osascript: "/usr/bin/osascript"

    Path to OSA scripts executor (AppleScript, JavaScript, etc.)
