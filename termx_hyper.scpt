on run argv
    if count of argv is 1 then
        set folderName to item 1 of argv
    end if
    
    if folderName is missing value then
        return
    end if
    
    tell application "Hyper"
        if not frontmost then
            activate
            delay (0.1)
        end if
    
        tell application "System Events"
            set commandToRun to "cd " & (folderName as string)
            keystroke "t" using command down
            delay (1)
            keystroke commandToRun
            keystroke return
            keystroke "clear"
            keystroke return
        end tell
    
    
    end tell


end run