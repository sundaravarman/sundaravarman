Attribute VB_Name = "exceltojsons"
Option Explicit
Public Const ParseJSONwb As String = "ParseJSON.xlam"
Public Sub exceltojson()
    Dim rng As Range, items As New Collection, myitem As New Dictionary, i As Integer, cell As Variant
    Dim jstring As String
    'Check if there is any active worksheet, else create one
    On Error Resume Next
    If ActiveSheet.Name = "" Then
        Workbooks.Add
    End If
    On Error GoTo 0
    With ActiveSheet
        Set rng = .Range(.Cells(2, 1), .Cells(.UsedRange.Rows.Count, .UsedRange.Columns.Count))
         
        '.UsedRange '("A2:A3") '
        
        'Set rng = Range(Sheets(2).Range("A2"), Sheets(2).Range("A2").End(xlDown)) use this for dynamic range
        i = 1
        Dim j As Integer
        For i = 2 To .UsedRange.Rows.Count ' cell In rng
            For j = 1 To .UsedRange.Columns.Count
                myitem(.Cells(1, j)) = .Cells(i, j)
            Next
                'myitem("Toolname") = cell.Value
                'myitem("Revision") = cell.Offset(0, 1).Value
                'myitem("ReleasePath") = cell.Offset(0, 2).Value
                'myitem("source path(optional)") = cell.Offset(0, 3).Value
            items.Add myitem
            Set myitem = Nothing
            Dim wb_name As String
            If Not IsWorkBookOpen(ParseJSONwb) Then
                'Open if the file exists
                If FileExists(ThisWorkbook.path & "\" & ParseJSONwb) Then Workbooks.Open ThisWorkbook.path & "\" & ParseJSONwb
            End If
            'jstring = ConvertToJson(items, Whitespace:=2)
        Next
        jstring = Application.Run(ParseJSONwb & "!ConvertToJson", items, 2)
        SaveTextToFile jstring
    End With
    'Sheets(1).Range("A4").Value = ConvertToJson(items, Whitespace:=2)
End Sub

