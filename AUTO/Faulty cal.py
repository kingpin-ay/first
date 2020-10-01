# faulty calculator
print('Please select (S) for sum , (E) for extract ,(M) for multiply ,(D) for divide ')
oparation = str(input('Please select your operator ')).upper()
numb_input = int(input('please enter your number : '))
numb_input2 = int(input('please enter your second number :'))
plus = 0
extract = 0
multiply = 0
divide = 0

if oparation == "M" and numb_input2 == 3 and numb_input == 45:
    print('555')
elif oparation == "S" and numb_input2 == 9 and numb_input == 56:
    print('77')
elif oparation == "D" and numb_input2 == 6 and numb_input == 56:
    print('4')
elif oparation == "S":
    plus = numb_input + numb_input2
    print(plus)
elif oparation == "E":
    extract = numb_input-numb_input2
    print(extract)
elif oparation == "M":
    multiply = numb_input * numb_input2
    print(multiply)
elif oparation == "D":
    divide = numb_input /numb_input2
    print(divide)
