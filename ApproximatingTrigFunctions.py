import numpy as np;
import math;
PI = np.pi;
CHOICES = ["sin", "cos", "tan"];

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

def calculateFunction(choice, angle):
    if (choice == 1):
        return sin(angle);
    elif (choice == 2):
        return cos(angle);
    else:
        return tan(angle);

def sin(angle):
    polynomial = np.array([]);
    for i in range(15):
        sign = (-1)**i;
        coefficient = 1/math.factorial(2*i + 1);
        degree = 2*i + 1;
        polynomial = np.append(polynomial, sign*coefficient*angle**degree);
    approximation = sum(polynomial);
    return approximation;

def cos(angle):
    return sin(PI/2 - angle);

def tan(angle):
    threshold = 0.001;
    if (abs(PI/2 - angle) < threshold):
        print("The tangent of this angle is undefined.");
    else:
        return sin(angle)/cos(angle);
    
##def getSinReference(angle):
    
printIntro();
choice = getChoice();
angle = getAngle();
print(CHOICES[choice - 1] + "(" + str(angle) + ") = " + str(calculateFunction(choice, angle)));
