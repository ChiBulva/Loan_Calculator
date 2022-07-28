import os
import shutil

def Create_Folder( Folder_Name, Path ):
    if( os.path.exists( Path ) ):
        Error_Handler( str( Folder_Name ) + " Exists Already" )
    else:
        os.makedirs( Path )

def Create_File( File_Name, Path, Contents, File_Type ):

    File = Path + str( File_Name ) + str( File_Type )

    print( File )

    file = open( File,'w+' )

    file.write( Contents )

    file.close(  )

    return

def Copy_Contents( From_Path, To_Path ):
    #call(["xcopy", str( From_Path), str( To_Path ), "/K/O/X"])
    #call( [ "xcopy", "/s", str( From_Path ), str( To_Path ) ] )
    print( "hey hey hey" )
    shutil.copytree( From_Path, To_Path )
    print( "hey hey hey" )
