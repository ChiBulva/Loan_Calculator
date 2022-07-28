import scripts.File_IO.JSON_Functions.JSON_Functions as JSON_Functions
import numpy as np
import numpy_financial as npf

from termcolor import colored
import os

Terminal_Toggle = True

os.system('color')
#Loan_Info = JSON_Functions.Open_JSON( "Loan_Info.json" )

#
# -
# - =
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
# - =
# -
#
def Settle( Number ):
    if( len( str( "{:.3f}".format( Number ) ) ) <= 7 ):
        Number = "{:.3f}".format( Number ) + str( "\t" )
    else:
        Number = "{:.3f}".format( Number )
    return Number

def For_The_Record( Array, Payment_Array ):
    # Print out contents of Loan_Cost_Array
    print( "\t", end="" )
    # Print out contents of Loan_Cost_Array
    for thing in range( len( Array ) ):
        if( float( Payment_Array[ thing ] ) <= float( Loan_Info[ 'Target_Monthly_Payment' ] ) and Terminal_Toggle ):
            print( colored( str( Array[ thing ] ), 'green' ) + "\t", end="" )

        elif( float( Payment_Array[ thing ] ) >= float( Loan_Info[ 'Target_Monthly_Payment_Max' ] ) and Terminal_Toggle ):
            print( colored( str( Array[ thing ] ), 'red' ) + "\t", end="" )

        else:
            print( str( Array[ thing ] ) + "\t", end="" )

    print()

def compound_interest(principle, interestRate, time_months):
    monthlyPayment      = abs( npf.pmt(interestRate/12, time_months, principle) );

    Loan_Worth = Settle( float( float( monthlyPayment ) * float( time_months ) ) )
    Loan_Cost = Settle( float( Loan_Worth ) - float( principle ) )
    Payment = Settle( float( monthlyPayment ) )

    return Payment, Loan_Worth, Loan_Cost

def Create_Array( Array_One, Array_Two, Time ):
    print( str( Time ) + " Years\t", end = "" )

    Time_Months = Time * 12

    for Number_One in Array_One:
        print( Number_One + "\t", end = "" )

    print(  )
    print(  )

    for Number_Two in Array_Two:

        Payment_Array = [  ]
        Loan_Worth_Array = [  ]
        Loan_Cost_Array = [  ]
        Units_Sold_To_Profit_Array = [  ]
        Cost_With_Utilities_Array = [  ]

        print( str( "{:.2f}".format( float( Number_Two ) * 100 ) ) + " %" , end="" )

        for Number_One in Array_One:

            #print( "\t" + str( float( Number_One ) + float( Number_Two ) ), end="" )
            Payment, Loan_Worth, Loan_Cost = compound_interest( float( Number_One ), float( Number_Two ), float( Time_Months ) )
            Payment_Array.append( Payment )
            Loan_Worth_Array.append( Loan_Worth )
            Loan_Cost_Array.append( Loan_Cost )



            Cost_With_Utilities = str( "{:.2f}".format( float( Payment ) + float( Ice_Info[ 'Rough_Cost_Of_Utilities_Month' ] ) ) + "\t" )
            Cost_With_Utilities_Array.append( Cost_With_Utilities )

            Units_Sold_To_Profit = str( "{:.2f}".format( ( float( Cost_With_Utilities ) / float( Ice_Info[ 'Cost_Per_Unit' ] ) ) * 12 / 365 ) + "\t" )
            #print( Units_Sold_To_Profit )

            Units_Sold_To_Profit_Array.append( Units_Sold_To_Profit )

            pass

        #For_The_Record( Cost_With_Utilities_Array, Payment_Array  )
        For_The_Record( Payment_Array, Payment_Array  )
        For_The_Record( Loan_Cost_Array, Payment_Array )
        For_The_Record( Units_Sold_To_Profit_Array, Payment_Array )
        #For_The_Record( Units_Sold_To_Profit_Array, Payment_Array )

        print()
        """
        # Print out contents of Loan_Cost_Array
        print( "\t", end="" )
        # Print out contents of Loan_Cost_Array
        for thing in range( len( Payment_Array ) ):
            if( float( Payment_Array[ thing ] ) <= float( Loan_Info[ 'Target_Monthly_Payment' ] ) ):
                print( colored( str( Payment_Array[ thing ] ), 'green' ) + "\t", end="" )
            elif( float( Payment_Array[ thing ] ) >= float( Loan_Info[ 'Target_Monthly_Payment_Max' ] ) ):
                print( colored( str( Payment_Array[ thing ] ), 'red' ) + "\t", end="" )
            else:
                print( Payment_Array[ thing ] + "\t", end="" )

        print()
        print( "\t", end="" )
        for thing in range( len( Loan_Cost_Array ) ):
            if( float( Payment_Array[ thing ] ) <= float( Loan_Info[ 'Target_Monthly_Payment' ] ) ):
                print( colored( str( Loan_Cost_Array[ thing ] ), 'green' ) + "\t", end="" )
            elif( float( Payment_Array[ thing ] ) >= float( Loan_Info[ 'Target_Monthly_Payment_Max' ] ) ):
                print( colored( str( Loan_Cost_Array[ thing ] ), 'red' ) + "\t", end="" )
            else:
                print( Loan_Cost_Array[ thing ] + "\t", end="" )

        print(  )
        print(  )
        """

def Assign_Interval_Array( Min, Max, Interval ): # INT, INT, INT -> Array[ INT ]
    #print( Min, Max, Interval )
    Ammount_Array = [  ]

    for Ammount in np.arange( float( Min ), float( Max ), float( Interval ) ):
        #print( "{:.3f}".format(Ammount) )
        Ammount_Array.append( "{:.3f}".format(Ammount) )

    return Ammount_Array

Loan_Info = {
	"Loan_Interval": 10000,
	"Loan_Max": 80001,
	"Loan_Min": 10000,
	"Year_Interval": 1,
	"Year_Max": 5,
	"Year_Min": 1,
	"Year": 5,
	"Interest_Rate_Interval": 0.005,
	"Interest_Rate_Max": 0.081,
	"Interest_Rate_Min": 0.05,
    "Target_Monthly_Payment_Max": 1500,
    "Target_Monthly_Payment": 600
}


Ice_Info = {
    "Cost_Of_Electricity": 0.11,
    "Cost_Of_Unit_Water": 1.48,
    "Water_Unit": 748,
    "One_Gallon_Ice_INT": 8.35,
    "Gallons_Per_10_LBS": 1.19,
    "ICE_Unit_Weight": 10,
    "ICE_Unit_Per_Water_Unit": 628.57,
    "Average_KWH": 158.4,
    "Machine_Watts": 6600,
    "Bin_Size": 550,
    "Prod_Rate_Per_Day": 640,
    "Rough_Cost_Of_Utilities_Month": 529.25,
    "Cost_Per_Unit": 2.50
}

#
# -
# - =
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
# - =
# -
#

"""
import math
principal = input("How much money do you currently have in the bank?")
rate = input("What is your interest rate?")
time = input("Over how many years is the interest compounded?")
actual_principal = float(principal)
actual_rate = float(rate)
actual_time = int(time)

#TODO: Calculate the total amount and print the result

A = math.pow((1 + actual_rate) , actual_time)
B = actual_principal*A
"""

#print( Loan_Info[ 'Loan_Max' ] )
#print( Loan_Info[ 'Loan_Min' ] )


Loan_Ammount_Array = Assign_Interval_Array( Loan_Info[ 'Loan_Min' ], Loan_Info[ 'Loan_Max' ], Loan_Info[ 'Loan_Interval' ] )

Interest_Rate_Array = Assign_Interval_Array( Loan_Info[ 'Interest_Rate_Min' ], Loan_Info[ 'Interest_Rate_Max' ], Loan_Info[ 'Interest_Rate_Interval' ] )


Formula = "Compound Interest"



for Years in range( Loan_Info[ 'Year_Min' ], Loan_Info[ 'Year_Max' ] + 1, Loan_Info[ 'Year_Interval' ] ):
    print( " -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )
    _Array = Create_Array( Loan_Ammount_Array, Interest_Rate_Array, Years )

#
# -
# - =
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
# - =
# -
#
