on run argv
    -- Don't set if no path to use
    if count of argv is 1 then
        set folderName to item 1 of argv -- Folder path
    end if
    
    tell application "Terminal"
        set windowsCount to (count of windows)
        if windowsCount is 0 then
            do script ""
        end if
        activate
        set window_id to id of first window whose frontmost is true
        
        if folderName is not missing value then
            if windowsCount is not 0 then
                tell application "System Events"
                    keystroke ("t" as string) using {command down} & return
                end tell
            end if

            set commandToRun to "cd " & quoted form of (folderName as string)

            do script commandToRun in window id window_id of application "Terminal"
            do script "clear" in window id window_id of application "Terminal"
        end if
    end tell
end run