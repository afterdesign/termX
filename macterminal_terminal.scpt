on run argv
    -- Don't set if no path to use
    if count of argv is 1 then
        set folderName to item 1 of argv -- Folder path
    end if
    
    if folderName is not missing value then
        tell application "Terminal"
            activate

            delay 0.25
            tell application "System Events" to keystroke "t" using command down
            delay 0.5

            set windowsCount to (count of windows)
            
            if windowsCount is not 0 then
                set window_id to id of first window whose frontmost is true
                set commandToRun to "cd " & quoted form of (folderName as string)

                do script commandToRun in window id window_id of application "Terminal"
                do script "clear" in window id window_id of application "Terminal"
            end if
        end tell
    end if
end run
