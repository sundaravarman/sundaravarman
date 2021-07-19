Attribute VB_Name = "LoadGui"
Sub CreateExcel()
Workbook.Add
'Check if JSON Exist
LoadJson
'If no JSON then
'SelectFolder
LoopThroughFiles
'Show it to the user to save
SaveJSON

End Sub
Sub LoopThroughFiles()

Dim oFSO As Object
Dim oFolder As Object
Dim oFile As Object
Dim i As Integer
Dim fileName As String
Set oFSO = CreateObject("Scripting.FileSystemObject")
'Application.GetOpenFilename("*",,"Please Choose file")

Dim sFolder As String
    ' Open the select folder prompt
    With Application.FileDialog(msoFileDialogFolderPicker)
        .ButtonName = "Select"
        .InitialFileName = "C:\"
        If .Show = -1 Then ' if OK is pressed
            sFolder = .SelectedItems(1)
        End If
    End With
    FileNames = GetFiles(sFolder, TimeStamps)
Set oFolder = oFSO.GetFolder("E:\json")

For Each oFile In oFolder.Files

    fileName = fileName & "," & oFile.Name

    i = i + 1

Next oFile

End Sub

Sub test()
Dim FilePath As String
FilePath = "E:\json\write json vertical"
GetFiles FilePath, tStamp
End Sub
'VBA function to return an array of file names from a folder:

Public Function GetFiles(sPath$, Optional TimeStamps, Optional sFilter$ = "*.*")
    Dim oFS As Object
    fileapath = sPath$
    Dim sFile As String
    Set oFS = CreateObject("Scripting.FileSystemObject")
    
    Dim p&, f$, s$, t$: s = Space(1000000#)
    Dim tStamp As String
    f = Dir(sPath & _
        String(Abs(Right(sPath, 1) <> "\"), "\") & sFilter)
        Do While Len(f)
            Mid(s, p + 1, Len(f) + 1) = f & vbLf
            tStamp = tStamp & oFS.GetFile(sPath$ & "\" & f).DateLastModified & vbLf
            p = p + Len(f) + 1
            f = Dir
            t = sPath$ & "\" & f
        Loop
    GetFiles = Split(Left(s, p - 1), vbLf)
    TimeStamps = Split(tStamp, vbLf)
End Function

