Attribute VB_Name = "ParsJSON"
Public Function readjsontxt(pathfile As String) As String

Dim fileName As String, textData As String, textRow As String, fileNo As Integer
fileName = pathfile '"E:\json\write json vertical\Text Document.json"
fileNo = FreeFile 'Get first free file number

Open fileName For Input As #fileNo
Do While Not EOF(fileNo)
   Line Input #fileNo, textRow
   textData = textData & textRow
Loop
Close #fileNo
exceljson textData
End Function
Public Sub exceljson(textin As String)

Dim textData As Object, JSON As Object, i As Integer
Dim OutStr As String
'textData = textin
'Set http = CreateObject("MSXML2.XMLHTTP")
'http.Open "GET", "http://jsonplaceholder.typicode.com/users", False
'http.Send
'Set JSON =
Set JSON = ParseJson(textin)
'Parse textin, OutObj, OutStr
i = 2
For Each Item In JSON
    'Key = json_ParseKey(textin, json_Index)
    'Sheets(1).Cells(i, 5).Value = Item(JSON.Items(1).Value)
    With ActiveSheet
        For j = 1 To .UsedRange.Columns.Count
            .Cells(i, j).Value = Item(CStr(.Cells(1, j)))
            'Debug.Print (.Cells(i, j).Value) & ":" & (.Cells(1, j)) & ":" & Item(CStr(.Cells(1, j)))
            
        Next
        '.Cells(i, 5).Value = Item("FileName")
        '.Cells(i, 6).Value = Item("Revision")
        '.Cells(i, 7).Value = Item("ReleasePath")
        '.Cells(i, 8).Value = Item("source path(optional)")
        'Sheets(1).Cells(i, 5).Value = Item("Foundary")
        'Sheets(1).Cells(i, 6).Value = Item("phone")
        'Sheets(1).Cells(i, 7).Value = Item("website")
        'Sheets(1).Cells(i, 8).Value = Item("company")("name")
    End With
    i = i + 1
Next
Application.StatusBar = "Completed loading of JSON"
End Sub
