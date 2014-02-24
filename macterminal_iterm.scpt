on run argv
    -- Don't set if no path to use
    if count of argv is 1 then
        set folderName to item 1 of argv -- Folder path
    end if

    tell application "iTerm"
        activate

        if (count of terminals) = 0 then
            set _term to (make new terminal)
        else
            set _term to current terminal
        end if

        tell _term
            launch session "Default Session"
            set _session to current session
        end tell

        if folderName is not missing value then
            tell _session
                write text "cd \"" & folderName & "\""
                write text "clear"
            end tell
        end if
    end tell
end run