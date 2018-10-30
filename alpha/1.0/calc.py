import math
# this is the selection code! codename part SELECT
select = input('''Please select what function you want to use
+ for Addition
- for Subtraction
/ for Devision
* for Multiplication
SQRT for squareroot please change second number to one
HYPO for hypotenuse solver
Here : ''') 

#this is were the user input's the numbers
NUM1 = input("Please put first number here : ")
NUM2 = input("Please put second number here : ")

#all results are calculated here because if it's in the "if" part's the program will not #run codename part CALC
ADD3 = float(NUM1) + float(NUM2)
SUB3 = float(NUM1) - float(NUM2)
DEV3 = float(NUM1) / float(NUM2)
MUL3 = float(NUM1) * float(NUM2)
SQRT = math.sqrt(float(NUM1))
HYPO1 = NUM1 ** 2
HYPO2 = NUM2 ** 2
HYPO3 = HYPO1 + HYPO2
HYPO4 = math.sqrt(float(HYPO3))

#this is the if part for addition it just print's the result. codename part A
if select == '+':
    
 print (ADD3) 

#this is the subtraction part always just print's the result. codename part S
if select == '-':

 print (SUB3) 

#codename part D
if select == '/':

 print (DEV3) 

#codename part M
if select == '*':

 print (MUL3)

#codename part SQRT
if select == 'SQRT':
 print (SQRT)

#codename part HYPO
if select == 'HYPO':
 print (HYPO4)
