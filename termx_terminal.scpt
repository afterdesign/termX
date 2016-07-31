on run argv
    if count of argv is 1 then
        set folderName to item 1 of argv
    end if

    if folderName is missing value then
        return
    end if

    tell application "Terminal"
        if not frontmost then
            activate
            delay (1)
        end if

        tell application "System Events"
            keystroke "t" using command down
        end tell

        set commandToRun to "cd " & (folderName as string)
        set current_tab to selected tab of first window whose frontmost is true
        do script commandToRun in current_tab
        do script "clear" in current_tab
    end tell
end run
