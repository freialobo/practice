"""this takes a string input like ' New York ' and returns it as my friend Subhankar Ghosh would use it in an instagram caption - like New York | 2015.
This also automatically pulls the current year"""

from datetime import date
def  shubhify (before) :
    """a function that takes in a string and returns the Shubhified version"""
    after =  before + " | " + str(date.today().year)
    return after
a = input( "Enter a string to be shubhified ... ")
print (shubhify(a))
