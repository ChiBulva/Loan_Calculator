import os

import scripts.File_IO.JSON_Functions.JSON_Functions as JSON_Functions
import scripts.OS.OS as OS


def TEST( HELLO ):
    print( HELLO )

Business_Path = "./static/Businesses/"
CWD = str( os.getcwd() ) + "\\"
Business_Base_Path = CWD + "static\\Businesses\\"
Uploads_Base_Path = CWD + "Uploads\\"

def Upload_Business_Info( JSON_Info ):
    # Create a folder under the Business Name
    Folder_Name = str( JSON_Info['Business_Name'].replace( " ", "_" ) )
    Folder_Path = Business_Base_Path + Folder_Name

    print( Folder_Name )
    OS.Create_Folder( Folder_Name, Folder_Path )

    JSON_File_Path = Folder_Path + str( "\\contents.json" )
    # Create a JSON with the ARG_Info
    JSON_Functions.Save_JSON( JSON_Info, JSON_File_Path, 4 )
    print( "Create Files!!!" )
    # Create PDF Based on the info

    print( "Create PDF!!!" )

    return Folder_Name

def Upload_New_File( uploaded_file, filename, app, Folder_Name ):
    Final_Path = Business_Path + str( Folder_Name ) + "/"
    print( Final_Path )

    app.config['UPLOAD_PATH'] = "./static/Businesses/Test_Business_10/"
    app.config['UPLOAD_PATH'] = Final_Path
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        print( file_ext )
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            return "Upload NOT Successful!!! bad extention. Use: '.jpg' or '.png'"

    uploaded_file.save(os.path.join( app.config['UPLOAD_PATH'], filename))

    Create_QR_Code( Final_Path, Folder_Name )

    return "Success!!!"

def Create_QR_Code( Final_Path, Folder_Name ):
    import pyqrcode
    import png
    from pyqrcode import QRCode

    print( Final_Path )
    print( Folder_Name )

    String_URL = JSON_Functions.Open_JSON( Final_Path + "/contents.json" )
    #print( String_URL[ 'Website' ] )
    
    s = String_URL[ 'Website' ]

    url = pyqrcode.create(s)

    # Create and save the png file naming "myqr.png"
    url.png( Final_Path + 'qr.png', scale = 6)
