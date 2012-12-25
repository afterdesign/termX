on run argv
    set folderName to item 1 of argv -- Folder path
    
    tell application "iTerm"
        activate
        make new terminal
        
        tell the first terminal
            launch session "Default Session"
            set _session to current session
        end tell
        
        tell _session
            write text "cd \"" & folderName & "\""
            write text "clear"
        end tell
    end tell
end run