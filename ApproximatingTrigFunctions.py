import numpy as np;

def printIntro():
    print("This program finds the values of trigonometric functions.");
    print("1. sin(x)");
    print("2. cos(x)");
    print("3. tan(x)");


def getChoice():
    choice = 0;
    while (choice != 1 and choice != 2 and choice != 3):
        choice = int(input("Enter the number of the function you want to evaluate: "));
        
    return choice;
    
def getAngle():
    return float(input("Enter the angle x in radians: "));


printIntro();
getChoice();
getAngle();