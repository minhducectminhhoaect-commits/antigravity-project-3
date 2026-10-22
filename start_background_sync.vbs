Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
currentDir = fso.GetParentFolderName(WScript.ScriptFullName)
cmd = "pythonw """ & currentDir & "\realtime_sync.py"""
WshShell.Run cmd, 0, False
MsgBox "Tự động đồng bộ thời gian thực với GitHub đã được bật ngầm!" & vbCrLf & "Mọi thao tác thêm, sửa, xóa file sẽ được tự động push lên GitHub.", vbInformation, "Realtime Git Sync"
