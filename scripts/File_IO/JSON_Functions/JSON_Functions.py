import time
import json
import os
#from os import walk

from random import randint

JSON_Base_Path = "/static/JSON/"

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

CWD = os.getcwd()

# Open a JSON file
def Open_JSON( File_Name ):
    File_Location = ( str( CWD ) + JSON_Base_Path + File_Name ).replace( "/", "\\" )
    print( File_Location )
    try:
        print( "PRINTER: 1" )
        Count = 1
        with open( File_Location, "r", encoding="utf-8" ) as JSON_RAW_INFO:
            print( "PRINTER: " + str( Count ) )
            JSON_DATA = json.load( JSON_RAW_INFO )
            Count += 1
        print( "PRINTER: " + str( Count ) )
        return JSON_DATA
    except:
        return { "Error": "File Doesn't exist" }

# Save a JSON file using new data
def Save_JSON( JSON, filename, indent ):
    # open(filename, 'a', encoding="utf-8")

    #Pprint( False,json.dump(
    #JSON))

    out_file = open( filename, "w", encoding="utf-8" )

    #Pprint( False, "Before Dump" )

    if( indent == None ):
        json.dump( JSON, out_file )
    if( indent == 4 ):
        json.dump( JSON, out_file, indent = 4 )

    #Pprint( False, "After Dump" )

    out_file.close()

    return "Success!!!"
