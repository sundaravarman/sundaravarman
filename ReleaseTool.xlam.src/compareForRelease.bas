Attribute VB_Name = "compareForRelease"

Sub compareAndRelease()
    wb_name = Tools_GUI
    Dim filePath As String
    
    Dim Selected_Tool  As String
    Selected_Tool = sel_tool
    filePath = Environ("temp") & "\" & Selected_Tool

    If Checktimestampdiff(filePath, tStamp) Then ReleaseAll
    Checktimestampdiff filePath, tStamp, True 'Runs the post process
End Sub
' Optional sFilter$ = "*.*"
Public Function Checktimestampdiff(sPath$, Optional TimeStamps, Optional post As Boolean) As Boolean
    Dim oFS As Object
    fileapath = sPath$
    Dim sFile As String
    Set oFS = CreateObject("Scripting.FileSystemObject")
    
    Dim p&, f$, s$, t$: s = Space(1000000#)
    Dim tStamp As String
    Dim i As Integer
    SheetName = "Release"
    With Workbooks(wb_name).Sheets(SheetName)
        'Find the coloumn last released path, Dev path,File name,Timestamp
        Dim releasedCol, DevCol, Filecol, Timestampcol As Integer
        releasedCol = .Rows(1).Find(What:="ReleasePath", _
                        LookIn:=xlValues, _
                        LookAt:=xlWhole, _
                        SearchOrder:=xlByRows, _
                        SearchDirection:=xlNext, _
                        MatchCase:=False).Column
        releasedTagCol = .Rows(1).Find(What:="LastReleasedTagFilew", _
                        LookIn:=xlValues, _
                        LookAt:=xlWhole, _
                        SearchOrder:=xlByRows, _
                        SearchDirection:=xlNext, _
                        MatchCase:=False).Column
        DevCol = .Rows(1).Find(What:="DevPath", _
                        LookIn:=xlValues, _
                        LookAt:=xlWhole, _
                        SearchOrder:=xlByRows, _
                        SearchDirection:=xlNext, _
                        MatchCase:=False).Column
        Filecol = .Rows(1).Find(What:="FileName", _
                        LookIn:=xlValues, _
                        LookAt:=xlWhole, _
                        SearchOrder:=xlByRows, _
                        SearchDirection:=xlNext, _
                        MatchCase:=False).Column
        Timestampcol = .Rows(1).Find(What:="Timestamp", _
                        LookIn:=xlValues, _
                        LookAt:=xlWhole, _
                        SearchOrder:=xlByRows, _
                        SearchDirection:=xlNext, _
                        MatchCase:=False).Column
    Dim fso As Object
    Set fso = VBA.CreateObject("Scripting.FileSystemObject")
        'Loopthrough used range
        i = 2
        Do While (.Cells(i, Filecol) <> "")
            'Get the timestamp of Dev path\FileName
            Debug.Print (.Cells(i, DevCol) & .Cells(i, Filecol))
            If Not FileExists((.Cells(i, DevCol) & .Cells(i, Filecol))) Then
                MsgBox ("Filename " & ((.Cells(i, DevCol) & .Cells(i, Filecol))) & " does not exist.Please check and Add in Dev Path")
                End
            End If
            tStamp = oFS.GetFile(.Cells(i, DevCol) & .Cells(i, Filecol)).DateLastModified
            reltStamp = .Cells(i, Timestampcol)
            'Compare timestamp read vs Dev timestamp if no difference then compare file = False Else True
            If reltStamp <> tStamp Then
                Checktimestampdiff = True
                'Copy the files different from dev to tag path to prepare for release
                If post = False Then Call fso.CopyFile(.Cells(i, DevCol) & .Cells(i, Filecol), .Cells(i, releasedTagCol), True)
                
                'Update the timestamp
                If post = True Then .Cells(i, Timestampcol) = tStamp
            End If
            i = i + 1
        Loop
        'Create the zip file
        'Copy the files different from tag path to release to prepare for release
        Dim fdir As String
        Dim fso2 As New FileSystemObject
        fdir = fso2.GetFolder(.Cells(2, releasedTagCol) & "\..")
        CreateZipFile fdir, fdir & ".zip"
'   CreateZipFile "C:\Projects\PhasingAutomation\Phasing_tool_Installer", "C:\Projects\PhasingAutomation\Phasing_tool_Installer.zip"

        If post = False Then If Checktimestampdiff = True Then CreateVersionFile .Cells(2, DevCol) & sel_tool & "_revision", .Cells(2, releasedCol)
    End With
End Function
