from datetime import date
def  shubhify (before) :
    """a function that takes in a string and returns the Shubhified version"""
    after =  before + " | " + str(date.today().year)
    return after
a = input( "Enter a string to be shubhified ... ")
print (shubhify(a))
