Attribute VB_Name = "ReleaseUtility"
Public wb_name As String
Public SheetName As String
Sub ReleaseToFolder(sourcePath As String, destinationPath As String)
    'Release path:"\\qctdfsrt\prj\vlsi\pete\scripts\ptetools\tss_data\TSS_EXCEL\phasing"
    On Error Resume Next
    'Kill sourcePath
    If Not FileExists(sourcePath) Then
        Application.StatusBar = "Source file does not exist: " & sourcePath
        End
    End If
    Kill destinationPath
    If InStr(destinationPath, ".") > 0 Then
        If FileExists(destinationPath) Then
            Application.StatusBar = "Unable to remove the Destination file:" & destinationPath
            End
        End If
    Else
        If Not FolderExists(destinationPath) Then
            Application.StatusBar = "Destination folder does not exist:" & destinationPath
            End
        End If
    End If
    On Error GoTo 0
    Dim fso As Object
    Set fso = VBA.CreateObject("Scripting.FileSystemObject")
    Call fso.CopyFile(sourcePath, destinationPath, True)
    'Call fso.CopyFile(source, destination[, overwrite] )
End Sub
Sub ReleaseAll()
    'ThisWorkbook.SaveAs sourcePath
    'Check if JSON loaded in Release sheet Else call Main in ParseJSON
    'CheckNLoadJSON
    'If InStr(Now, "7/6/2021") > 0 Then Exit Sub
    CreateZipFile "C:\Projects\PhasingAutomation\Phasing_tool_Installer", "C:\Projects\PhasingAutomation\Phasing_tool_Installer.zip"
    ReleaseToFolder "C:\Projects\PhasingAutomation\Phasing_tool_Installer.zip", "\\qctdfsrt\prj\vlsi\pete\scripts\ptetools\tss_data\TSS_EXCEL\phasing\Phasing_tool_Installer.zip"
    ReleaseToFolder ThisWorkbook.path & "\" & ThisWorkbook.Name, "\\qctdfsrt\prj\vlsi\pete\scripts\ptetools\tss_data\TSS_EXCEL\phasing\" & replace(ThisWorkbook.Name, "_dev", "")
End Sub
Function CheckNLoadJSON()
'Check if Sheet Release GUI exist
Dim fullname As String
Dim path As String
Dim shp As Shape

path = Environ("temp")
wb_name = "Tools_GUI.xlsx"
fullname = path & "\" & wb_name

If Not IsWorkBookOpen(wb_name) Then
    If FileExists(fullname) Then
        'Open if the file exists
        Workbooks.Open fullname
    Else
        'Create the file if it doesn't exist
        Workbooks.Add
        ActiveWorkbook.SaveAs fullname
    End If
End If
'Check if sheet exist
SheetName = "Release"
If Not Evaluate("ISREF('" & SheetName & "'!A1)") Then
     'Create the sheet
     Workbooks(wb_name).ActiveSheet.Name = SheetName
End If
With Workbooks(wb_name).ActiveSheet
    .Range(.Cells(1, 1), .Cells(.UsedRange.Rows.Count, .UsedRange.Columns.Count)).ClearContents
    'ActiveSheet.Shapes.Range(Array("Rectangle 1")).Select
    For Each shp In ActiveSheet.Shapes
        shp.Delete
    Next shp
End With
    With Workbooks(wb_name).Sheets(SheetName)
        .Cells(1, 1) = "FileName"
        .Cells(1, 2) = "Timestamap"
        .Cells(1, 3) = "SrcPath"
        .Cells(1, 4) = "ReleasePath"
    End With
LoopThroughFiles
End Function
Function IsWorkBookOpen(Name As String) As Boolean
    Dim xWb As Workbook
    On Error Resume Next
    Set xWb = Application.Workbooks.Item(Name)
    IsWorkBookOpen = (Not xWb Is Nothing)
End Function
Function CreateVersionFile() As Boolean
    'Get the OS library and start building
    
End Function
Function FileExists(wb_name As String) As Boolean

    On Error GoTo NotExist
    If Not Len(Dir(wb_name)) = 0 Then
        FileExists = True
        On Error GoTo 0
        Exit Function
    End If

NotExist:
    On Error GoTo 0
    FileExists = False
End Function ' FileExists

Sub CreateZipFile(folderToZipPath As Variant, zippedFileFullName As Variant)

    Dim ShellApp As Object
    
    'Create an empty zip file
    Open zippedFileFullName For Output As #1
    Print #1, Chr$(80) & Chr$(75) & Chr$(5) & Chr$(6) & String(18, 0)
    Close #1
    
    'Copy the files & folders into the zip file
    Set ShellApp = CreateObject("Shell.Application")
    ShellApp.Namespace(zippedFileFullName).CopyHere ShellApp.Namespace(folderToZipPath).items
    
    'Zipping the files may take a while, create loop to pause the macro until zipping has finished.
    On Error Resume Next
    Do Until ShellApp.Namespace(zippedFileFullName).items.Count = ShellApp.Namespace(folderToZipPath).items.Count
        Application.Wait (Now + TimeValue("0:00:01"))
    Loop
    On Error GoTo 0

End Sub
