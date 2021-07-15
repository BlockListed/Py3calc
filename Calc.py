import math
# this is the selection code! codename part SELECT
def selector():
    global select
    select = input('''Please select what function you want to use
    + for Addition
    - for Subtraction
    / for Devision
    * for Multiplication
    SQRT for squareroot please change second number to zero
    HYPO for hypotenuse solver
    TTPO for to the power of
    PIB2N for percentage increase between 2 Numbers
    DIS for Degrees in a shape with a certain amount of corners (leave NUM2 empty)
    Here : ''') 

#this is were the user input's the numbers
def numselect():
    global NUM1
    global NUM2
    NUM1 = float(input("Please put first number here : "))
    NUM2 = float(input("Please put second number here : "))

#all results are calculated here because if it's in the "if" part's the program will not 

#run codename part CALC

#addition
def add():
 ADD3 = float(NUM1) + float(NUM2)
 print (ADD3)




#subtraction
def sub():
 SUB3 = float(NUM1) - float(NUM2)
 print (SUB3)




#devition
def dev():
 DEV3 = float(NUM1) / float(NUM2)
 print (DEV3)




#multiplication
def mul():
 MUL3 = float(NUM1) * float(NUM2)
 print (MUL3)




#SQRT
def sqrt():
 SQRT = math.sqrt(float(NUM1))
 print (SQRT)


#HYPO
def hypo():
 HYPO1 = float(NUM1) ** 2
 HYPO2 = float(NUM2) ** 2
 HYPO3 = float(HYPO1) + float(HYPO2)
 HYPO4 = math.sqrt(float(HYPO3))
 print (HYPO4)


#TTPO
def ttpo():
 rettpo = float(NUM1) ** int(NUM2)
 print (rettpo)


#PIB2N
def pib2n():
    PD1 = NUM2 * 100
    PD2 = PD1 / NUM1
    REPD = PD2 - 100
    print (REPD)


#DIS
def dis():
    DS1 = NUM1 - 2
    REDS = DS1 * 180
    print (REDS)


#Main0
def main():
    selector()
    numselect()
    #using dict as switch statement
    value = {
        "+" : add,
        "-" : sub,
        "/" : dev,
        "*" : mul,
        "sqrt" : sqrt,
        "hypo" : hypo,
        "ttpo" : ttpo,
        "pib2n" : pib2n,
        "dis" : dis,
    }[select.casefold()]()

main()
