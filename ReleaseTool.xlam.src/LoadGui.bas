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

'Check if file already exists
If FileExists(Environ("temp") & JSONfilename) Then
    If Not IsWorkBookOpen(ParseJSONwb) Then
        'Open if the file exists
        If FileExists(ThisWorkbook.path & "\" & ParseJSONwb) Then Workbooks.Open ThisWorkbook.path & "\" & ParseJSONwb
    End If
    Dim test As String
    test = Application.Run(ParseJSONwb & "!readjsontxt", Environ("temp") & JSONfilename)

Else

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
End If
    LoadButton
'Set oFolder = oFSO.GetFolder("E:\json")

End Sub

Sub test()
Dim filePath As String
filePath = "E:\json\write json vertical"
GetFiles filePath, tStamp
End Sub
'VBA function to return an array of file names from a folder:

Public Function GetFiles(sPath$, Optional TimeStamps, Optional sFilter$ = "*.*")
    Dim oFS As Object
    fileapath = sPath$
    Dim sFile As String
    Set oFS = CreateObject("Scripting.FileSystemObject")
    
    Dim p&, f$, s$, t$: s = Space(1000000#)
    Dim tStamp As String
    Dim i As Integer
    i = 1
    With Workbooks(wb_name).Sheets(SheetName)
        f = Dir(sPath & _
            String(Abs(Right(sPath, 1) <> "\"), "\") & sFilter)
            
        Do While Len(f)
            'Mid(s, p + 1, Len(f) + 1) = f & vbLf
            'tStamp = tStamp & oFS.GetFile(sPath$ & "\" & f).DateLastModified & vbLf
            p = p + Len(f) + 1
            f = Dir
            t = sPath$ & "\" & f
            If f <> "" Then
                i = i + 1
                .Cells(i, 1) = f
                .Cells(i, 2) = oFS.GetFile(sPath$ & "\" & f).DateLastModified
                .Cells(i, 3) = t
                .Cells(i, 4) = "null"
            End If
        Loop
        'GetFiles = Split(Left(s, p - 1), vbLf)
        'TimeStamps = Split(tStamp, vbLf)
        Dim objTable As ListObject
        Dim LastRow, LastCol As Integer
        LastCol = .Cells(1, .Columns.Count).End(xlToLeft).Column
        LastRow = .Cells(.Rows.Count, "A").End(xlUp).row

        .Range(.Cells(1, 1), .Cells(LastRow, LastCol)).Select
        '.Range(.Cells(1, 1), .Cells(1, .UsedRange.Columns.Count)).Select
        'Selection.End(xlDown).Select
        '.Range(.Cells(1, 1), .Cells(1, .UsedRange.Columns.Count)).End(xlDown).Select
        Set objTable = ActiveSheet.ListObjects.Add(xlSrcRange, Selection, , xlYes)
    End With
End Function
Sub SaveJsonAndRelease()
'save Content as Json
 exceltojson
End Sub
Function LoadButton()
ActiveSheet.Shapes.AddShape(msoShapeRectangle, 645.5, 1.5, 63, 22.5).Select
Selection.OnAction = "SaveJsonAndRelease"
Selection.ShapeRange(1).TextFrame2.TextRange.Characters.Text = "  Release"
End Function


