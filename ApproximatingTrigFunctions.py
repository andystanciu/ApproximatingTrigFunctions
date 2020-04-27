## Aditya S., Andy S., Hanae VW., Phillip MY., Honors Precalculus, 4/26/20
## Programming Assignment 5.10: Approximating Trig Functions
## This program will approximate trig functions using huge polynomials

##Imports
import numpy as np;
import math;

##Class constants
PI = np.pi;
DEGREE = 15;
CHOICES = ["sin", "cos", "tan"];

#####FUNCTIONS#####

"""
prints the intro
@param: none
@return: void
"""
def printIntro():
    print("This program finds the values of trigonometric functions.");
    print("1. sin(x)");
    print("2. cos(x)");
    print("3. tan(x)");

"""
gets the user's choice for the trig function
@param: none
@return: choice (int)
"""
def getChoice():
    choice = 0;
    while (choice != 1 and choice != 2 and choice != 3):
        choice = int(input("Enter the number of the function you want to evaluate: "));
        
    return choice;
   
"""
gets the angle from the user
@param: none
@return: angle (float)
"""
def getAngle():
    return float(input("Enter the angle x in radians: "));

"""
calculates a given function depending on the user choice
@param choice: the user's choice
@param angle: the user's angle
@return: the calculated function
"""
def calculateFunction(choice, angle):
    if (choice == 1):
        return outOfRangeSin(angle);
    elif (choice == 2):
        return outOfRangeCos(angle);
    else:
        return outOfRangeTan(angle);

"""
approximates the sine of a given angle
@param angle: the angle
@return: the approximation of the angle
"""
def sin(angle):
    polynomial = np.array([]);
    for i in range(DEGREE):
        sign = (-1)**i;
        coefficient = 1/math.factorial(2*i + 1);
        degree = 2*i + 1;
        polynomial = np.append(polynomial, sign*coefficient*angle**degree);
    approximation = sum(polynomial);
    return approximation;

"""
approximates the cosine of a given angle using it's sine
@param angle: the angle
@return: the approximation of the angle
"""
def cos(angle):
    return sin(PI/2 - angle);

"""
ensures that the angle that passes into sin() is within range
@param angle: the angle
@return: the approximation of the angle (uses sin())
"""
def outOfRangeSin(angle):
    
    ##Brings all angles in range 0 to 2pi
    if (angle > 2*PI):
        while (angle > 2*PI):
            angle = angle - 2*PI;
    elif (angle < 0):
        while (angle < 0):
            angle = angle + 2*PI;
    
    ##Gets sign of angle        
    if (angle > PI):
        sign = -1;
    else:
        sign = 1;
    
    ##Brings all angles in range 0 to pi/2
    if (angle > PI/2 and angle < 3*PI/2):
        angle = abs(PI - angle);
        
    elif (angle > 3*PI/2 and angle < 2*PI):
        angle = 2*PI - angle;
    
    ##Uses double angle formula and sin() function    
    answer = sign*2*sin(angle/2)*cos(angle/2);
     
    return answer;

"""
ensures that the angle that passes into sin() is within range when calculating a cos()
@param angle: the angle
@return: the approximation of the angle (uses sin())
"""
def outOfRangeCos(angle):
    
    ##Brings all angles in range 0 to 2pi
    if (angle > 2*PI):
        while (angle > 2*PI):
            angle = angle - 2*PI;
    elif (angle < 0):
        while (angle < 0):
            angle = angle + 2*PI;
    
    ##Gets sign of angle 
    if (angle > PI/2 and angle < 3*PI/2):
        sign = -1;
    else:
        sign = 1;
    
    ##Brings all angles in range 0 to pi/2
    if (angle > PI/2 and angle < 3*PI/2):
        angle = PI - angle;
        
    elif (angle > 3*PI/2 and angle < 2*PI):
        angle = 2*PI - angle;
    
    ##Uses double angle formula and sin() function     
    answer = sign*(1-2*(sin(angle/2)**2));
     
    return answer;

"""
ensures that the angle that passes into sin() is within range when calculating a tan()
@param angle: the angle
@return: the approximation of the angle (uses outOfRangeSin() and outOfRangeCos())
"""
def outOfRangeTan(angle):
    return outOfRangeSin(angle)/outOfRangeCos(angle);

#####MAIN#####
    
printIntro();
choice = getChoice();
angle = getAngle();
result = calculateFunction(choice, angle);

if type(result) != str: ##Case when tangent is undefined
    print(CHOICES[choice - 1] + "(" + str(angle) + ") = " + str(result));
else:
    print(result);