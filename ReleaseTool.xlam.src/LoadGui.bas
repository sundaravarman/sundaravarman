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
Sub LoopThroughFiles(Optional filename As String)

Dim oFSO As Object
Dim oFolder As Object
Dim oFile As Object
Dim i As Integer
Set oFSO = CreateObject("Scripting.FileSystemObject")
'Application.GetOpenFilename("*",,"Please Choose file")

'Check if file already exists
If filename = "" Then filename = Environ("temp") & JSONfilename

If FileExists(filename) And (Not FolderExists(filename)) Then
    If Not IsWorkBookOpen(ParseJSONwb) Then
        'Open if the file exists
        If FileExists(ThisWorkbook.path & "\" & ParseJSONwb) Then Workbooks.Open ThisWorkbook.path & "\" & ParseJSONwb
    End If
    Dim test As String
    test = Application.Run(ParseJSONwb & "!readjsontxt", filename)
    ConvertDataToTable ActiveSheet
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
    Dim rng As Worksheet
    Set rng = Workbooks(wb_name).Sheets(SheetName)
    With rng
        f = Dir(sPath & _
            String(Abs(Right(sPath, 1) <> "\"), "\") & sFilter)
            
        Do While Len(f)
            'Mid(s, p + 1, Len(f) + 1) = f & vbLf
            'tStamp = tStamp & oFS.GetFile(sPath$ & "\" & f).DateLastModified & vbLf
            p = p + Len(f) + 1
            t = sPath$ & "\" & f
            If f <> "" Then
                i = i + 1
                .Cells(i, 1) = f
                .Cells(i, 2) = Format(oFS.GetFile(sPath$ & "\" & f).DateLastModified, "mm/dd/yyyy HH:mm:ss")
                .Cells(i, 3) = t
                .Cells(i, 5) = "\\qctdfsrt\prj\vlsi\pete\scripts\ptetools\tss_data\TSS_EXCEL\phasing"
            End If
            f = Dir
        Loop
        ConvertDataToTable rng
    End With
End Function
Function ConvertDataToTable(SelSheet As Worksheet)
        Dim objTable As ListObject
        Dim LastRow, LastCol As Integer
        With SelSheet
            LastCol = .Cells(1, .Columns.Count).End(xlToLeft).Column
            LastRow = .Cells(.Rows.Count, "A").End(xlUp).row
    
            .Range(.Cells(1, 1), .Cells(LastRow, LastCol)).Select
            '.Range(.Cells(1, 1), .Cells(1, .UsedRange.Columns.Count)).Select
            'Selection.End(xlDown).Select
            '.Range(.Cells(1, 1), .Cells(1, .UsedRange.Columns.Count)).End(xlDown).Select
            On Error Resume Next
            Set objTable = ActiveSheet.ListObjects.Add(xlSrcRange, Selection, , xlYes)
            On Error GoTo 0
        End With
End Function

Function LoadButton()

'clear the existing buttons if any
On Error Resume Next
ActiveSheet.Shapes(2).Delete
ActiveSheet.Shapes(1).Delete
On Error GoTo 0

ActiveSheet.Shapes.AddShape(msoShapeRectangle, 645.5, 1.5, 70, 22.5).Select
Selection.OnAction = "SaveJsonAndRelease"
Selection.ShapeRange(1).TextFrame2.TextRange.Characters.Text = "    Release"

ActiveSheet.Shapes.AddShape(msoShapeRectangle, 645.5, 55.5, 70, 22.5).Select
Selection.OnAction = "CheckNLoadJSON"
'Selection.ShapeRange(2).TextFrame2.TextRange.Characters.Text = "Load"
ActiveSheet.Shapes(2).TextFrame2.TextRange.Characters.Text = "  Select Tool"
End Function
