Attribute VB_Name = "Check4Updates"
Option Explicit
Option Private Module

'This code, within your client's workbooks, will automatically check for an updated version.
'If an update exists, they will be prompted. If they decide to allow the newest version to
'replace the older one, the code will download the new version, kill the older version, and
'then load it'self into Excel. Download the example and open it. The workbook should replace
'itself with the newer version located on my server without any user intervention. (after the messagebox).
'Close it and open it again. You will not be prompted because your now have the latest file. Note
'the status text in the statusbar each time you open the workbook...

'Initial setup on your end.
'1. Copy and paste the code below into your workbook.
'
'2. Create a small textfile with two lines contained within. The date and time of your current file and the URL on the server...
'
'Example:
'
'07/08/2006 15:33
'server//logistics/dry_flood/manifest.xls
'
'Post this textfile to your server
'
'4. Change the Private Constant, "UpdateNotificationRemoteFileFullName" to reflect the URL of the textfile. This is
'the file that your clients' workbooks will check every time they are opened. The date will be compared with the date
'stored within their workbook. If the date in the textfile is more current, the update will download and replace the older version.
'
'5. After you have updated your file with this code and have performed other typical updates, run the following macro.
'"Sub Update_UpdateNotificationWorkbookName()"
'
'6. Obviously, you will need to perform an initial distribution (to your clients) of copies of the new file containing
'the macros code before this is functionally automated.
'
'7. Post your xls file to your server.
'Thereafter, the only activity that should be required of you before posting an updated file to your server is to run
'the macro, "Sub Update_UpdateNotificationWorkbookName()" after you have completed any changes. This could be automated
'as well but that's another post...
'
'NOTE! Use copies when testing. Your workbook will be replaced with the one on the server.
'Also. This code needs work and error handling.

'change this to the correct URL
Private Const UpdateNotificationRemoteFileFullName As String = "https://sharepoint.qualcomm.com/qct/PTE/TSS/Shared%20Documents/beta/phasing_update_revision.txt"
Public Const path As String = "C:\TSS\PhasingAutomation\"
Public Declare Function URLDownloadToFile Lib "urlmon" Alias "URLDownloadToFileA" (ByVal pCaller As Long, _
        ByVal szURL As String, ByVal szFileName As String, ByVal dwReserved As Long, ByVal lpfnCB As Long) As Long
Public debugenabled As Boolean
Function Release()
    'Release path:"\\qctdfsrt\prj\vlsi\pete\scripts\ptetools\tss_data\TSS_EXCEL\phasing"
    Dim sourcePath As String
    Dim destinationPath As String
    destinationPath = "\\qctdfsrt\prj\vlsi\pete\scripts\ptetools\tss_data\TSS_EXCEL\phasing\" & replace(ThisWorkbook.Name, "_dev", "")
    sourcePath = ThisWorkbook.path & "\" & replace(ThisWorkbook.Name, "_dev", "")
    On Error Resume Next
    Kill sourcePath
    If FileExists(sourcePath) Then
        Application.StatusBar = "Unable to delete " & sourcePath
        End
    End If
    Kill destinationPath
    If FileExists(destinationPath) Then
        Application.StatusBar = "Unable to delete " & destinationPath
        End
    End If
    On Error GoTo 0
    ThisWorkbook.SaveAs sourcePath
    Dim fso As Object
    Set fso = VBA.CreateObject("Scripting.FileSystemObject")
    Call fso.CopyFile(sourcePath, destinationPath, True)
    'Call fso.CopyFile(source, destination[, overwrite] )

End Function
Function DownloadFileFromWeb(strURL As String, strSavePath As String) As Long
    
    On Error Resume Next
    Kill Left(strSavePath, InStrRev(strSavePath, "\")) & "*"
    On Error GoTo 0

    ' strSavePath includes filename
    URLDownloadToFile 0&, strURL, strSavePath, 0&, 0&
    
    'Unzip the file after comparing the revision file
     UnzipAFile strSavePath, Left(strSavePath, InStrRev(strSavePath, "\"))
     
End Function
Sub UnzipAFile(zippedFileFullName As Variant, unzipToPath As Variant)

Dim ShellApp As Object

'Copy the files & folders from the zip into a folder
Set ShellApp = CreateObject("Shell.Application")
'Clear the files if it already exists
ShellApp.Namespace(CStr(unzipToPath)).CopyHere ShellApp.Namespace(CStr(zippedFileFullName)).items
End Sub
'run this everytime you are finished updating the source file
'adds or over-writes a workbook name containing the current date and time
Sub Update_UpdateNotificationWorkbookName()
    'Creates a line sample <definedName name="Update_DateTime" hidden="1">44362.3524305556</definedName>
    'inside the zip folder
    ThisWorkbook.Names.Add "Update_DateTime", Now, False
    Application.EnableEvents = False
    ThisWorkbook.Save
    Application.EnableEvents = True
    'add code here to upload to server or to save to your web folder
End Sub

Sub test()
    Dim x As String
    x = SetInput("project", "testing_prj2")
    
    x = GetInput("project")
    x = GetInput("si_revision")
    x = GetInput("block_name")
    x = GetInput("foundry")
    x = GetInput("platform")
    
    UnzipAFile "C:\TSS\PhasingAutomation\Phasing_tool_Installer.zip", "C:\TSS\PhasingAutomation\"
    Dim LauncherUpdate As Boolean
    Dim ComponentsUpdate As Boolean
    CheckForUpdates LauncherUpdate, ComponentsUpdate
End Sub

Function CheckForUpdates(LauncherUpdate As Boolean, ComponentsUpdate As Boolean) As Boolean
    Dim UpdateNotificationLocalFileFullName As String:    Dim FileNumber  As Integer
    Dim RemoteXlsFileDate As Double
    Dim LocalXlsFileDate As Double
    Dim RemoteXlsFileFullName As String
    Dim LocalXlsFileFullName As String
    Dim InputCheckForValidDate As String
    
    CheckForUpdates = False
    
    UpdateNotificationLocalFileFullName = Environ("temp") & "\phasing_update_revision.txt"
    
    If URLDownloadToFile(0&, UpdateNotificationRemoteFileFullName, _
       UpdateNotificationLocalFileFullName, 0&, 0&) = 0 Then
    
        FileNumber = FreeFile
        On Error Resume Next
        Open UpdateNotificationLocalFileFullName For Input As #FileNumber:        Input #FileNumber, InputCheckForValidDate:        Input #FileNumber, RemoteXlsFileFullName:        Close #FileNumber
        'Kill UpdateNotificationLocalFileFullName
        On Error GoTo 0
        
        If IsDate(InputCheckForValidDate) Then:            RemoteXlsFileDate = CDate(InputCheckForValidDate):
        
        'Check if phasing_update_revision_downloaded.txt rev
        If (FileExists(path & "phasing_update_revision_downloaded.txt")) Then
            Open UpdateNotificationLocalFileFullName For Input As #FileNumber
            Input #FileNumber, InputCheckForValidDate
            Input #FileNumber, RemoteXlsFileFullName
            Close #FileNumber
            If IsDate(InputCheckForValidDate) Then
                LocalXlsFileDate = CDate(InputCheckForValidDate)
            End If
        End If
        
        'if the name does not yet exist, an error will not be raised
        'however, the statement will evaluate to True and
        'attempt to download the update rather it is actually
        'more recent or not
        'todo: Insted of Update_DateTime use this workbook path phasing_update_revision_downloaded.txt
        If debugenabled Then Debug.Assert 0
        If RemoteXlsFileDate <> LocalXlsFileDate Then ComponentsUpdate = True
        If RemoteXlsFileDate > CDbl([Update_DateTime]) Then LauncherUpdate = True
        
        If ComponentsUpdate Then
            If FolderExists(path) = False Then CreateSubDirectories (path)
            DownloadFileFromWeb "https://sharepoint.qualcomm.com/qct/PTE/TSS/Shared%20Documents/beta/Phasing_tool_Installer.zip", path & "Phasing_tool_Installer.zip"
        End If 'If ComponentsUpdate Then
        
        If LauncherUpdate Then
            Application.StatusBar = "Found an update and update in progress..."
            CheckForUpdates = True
            
            If MsgBox("An update Is available. Click        'OK' to overwrite" & _
               " the current local version With the newest version.", vbOKCancel) = vbOK Then
            
                LocalXlsFileFullName = replace(ThisWorkbook.fullname, ".xl", "_temp.xl")
                'download updated file
                If URLDownloadToFile(0&, RemoteXlsFileFullName, _
                LocalXlsFileFullName, 0&, 0&) = 0 Then
                
                    On Error Resume Next
                    Kill replace(LocalXlsFileFullName, "_temp.xl", "_temp_2.xl")
                    On Error GoTo 0
                    
                    'must temporarily change the name of the activeworkbook and
                    'change the file access to readonly
                    ThisWorkbook.SaveAs replace(LocalXlsFileFullName, "_temp.xl", "_temp_2.xl")
                    If ThisWorkbook.ReadOnly = False Then
                        ThisWorkbook.ChangeFileAccess xlReadOnly
                    End If
                    
                    'create a name at the application level so that Open code is not run
                    'flag here. checked in workbook open
                    Application.ExecuteExcel4Macro "SET.NAME(""RunCode"",""NO"")"
                    Kill replace(LocalXlsFileFullName, "_temp.xl", ".xl")
                    
                    'you need to account for a file access error here
                    Name LocalXlsFileFullName As replace(LocalXlsFileFullName, "_temp.xl", ".xl")
                    Workbooks.Open replace(LocalXlsFileFullName, "_temp.xl", ".xl")
                    Application.ExecuteExcel4Macro "SET.NAME(""RunCode"")"
                    Kill ThisWorkbook.fullname
                    
                    'install the components
                    'Dim Path As String
                    'Path = "C:\TSS\PhasingAutomation"
                    'If FolderExists(Path) = False Then CreateSubDirectories (Path)
                    'DownloadFileFromWeb "https://sharepoint.qualcomm.com/qct/PTE/TSS/Shared%20Documents/beta/Phasing_tool_Installer.zip", Path & "\Phasing_tool_Installer.zip"
        
                    'Rename the downloaded file
                    ThisWorkbook.Close False
                    Application.StatusBar = "Update Successful. You have the most current version..."
                    
                Else
                    Application.StatusBar = "Update available. Failed To download updated version..."
                End If 'If URLDownloadToFile(0&, Remot
            Else
                Application.StatusBar = "Update available. User cancelled update..."
            End If 'If MsgBox("An update Is available
        Else
            Application.StatusBar = "You have the most current version..."
        End If 'If LauncherUpdate Then
        If ComponentsUpdate Or LauncherUpdate Then
            'Move the revision file to downloaded.txt file
            Dim fso As New FileSystemObject
            Dim fileName As String
            fileName = fso.GetFileName(UpdateNotificationRemoteFileFullName)
            Name Environ("temp") & "\" & fileName As path & replace(fileName, ".txt", "") & "_downloaded.txt"
        End If
    Else
        Application.StatusBar = "Failed To download update notification file..."
    End If
End Function

Sub CreateSubDirectories(fullPath As String)

    Dim Str As String
    Dim strArray As Variant
    Dim i As Long
    Dim basePath As String
    Dim newPath As String

    Str = fullPath

    ' add trailing slash
    If Right$(Str, 1) <> "\" Then
        Str = Str & "\"
    End If

    ' split string into array
    strArray = Split(Str, "\")

    basePath = strArray(0) & "\"

    ' loop through array and create progressively
    ' lower level folders
    For i = 1 To UBound(strArray) - 1
        If Len(newPath) = 0 Then
            newPath = basePath & newPath & strArray(i) & "\"
        Else
            newPath = newPath & strArray(i) & "\"
        End If

        If Not FolderExists(newPath) Then
            MkDir newPath
        End If
    Next i

End Sub

Function FolderExists(ByVal strPath As String) As Boolean
    ' from http://allenbrowne.com
    On Error Resume Next
    FolderExists = ((GetAttr(strPath) And vbDirectory) = vbDirectory)
    On Error GoTo 0
End Function
