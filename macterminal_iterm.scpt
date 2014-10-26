on run argv
    if count of argv is 1 then
        set folderName to item 1 of argv
    end if

    if folderName is missing value then
        return
    end if

    tell application "iTerm"
        if not frontmost then
            activate
            delay (1)
        end if

        tell application "System Events"
            keystroke "t" using command down
        end tell

        tell current session of current terminal
            write text "cd " & folderName
            write text "clear"
        end tell
    end tell
end run
