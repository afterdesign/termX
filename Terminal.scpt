on run argv
    set folderName to item 1 of argv -- Folder path
    
    tell application "Terminal"
        set windowsCount to (count of windows)
        if windowsCount is 0 then
            do script ""
        end if
        activate
        set window_id to id of first window whose frontmost is true
        
        if windowsCount is not 0 then
            tell application "System Events"
                keystroke "t" using {command down}
            end tell
        end if

        set commandToRun to "cd " & quoted form of (folderName as string)

        do script commandToRun in window id window_id of application "Terminal"
        do script "clear" in window id window_id of application "Terminal"
    end tell
end run