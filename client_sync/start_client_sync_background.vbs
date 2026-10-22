Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
currentDir = fso.GetParentFolderName(WScript.ScriptFullName)
cmd = "pythonw """ & currentDir & "\client_realtime_pull.py"""
WshShell.Run cmd, 0, False
MsgBox "Tiến trình nhận đồng bộ từ máy chủ đã được bật ngầm!" & vbCrLf & "Mỗi khi máy chủ có tệp mới hoặc xóa tệp, máy tính này sẽ tự động cập nhật theo.", vbInformation, "Client Auto-Sync"
