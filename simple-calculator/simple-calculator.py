#BASIC CALCULATOR:-
class color:
 BOLD='\033[1m'
 RED='\033[91m'
 END='\033[0m'
 YELLOW='\033[93m'
name=input("Enter your name:")
print(f"{color.BOLD}{color.YELLOW}Hello! {name}{color.END} welcome to simple calculator.")

#for addition use'+' or 'add'
#for subtaction use'-' or 'subtact'
#for multiplication use'*' or multiple'or 
#for division use'/' or 'divide'
#for percentage use '%' or 'percent'

num1=float(input("Enter first number:"))
op =input("Enter the opperation")
num2=float(input("Enter second number:"))

if op =="+" or op=="add":
    print(f"{num1} + {num2} ={num1 + num2}")
if op =="-" or op=="subtact":
    print(f"{num1} - {num2} ={num1 - num2}")
if op =="*" or op=="mulitple":
    print(f"{num1} x {num2} = {num1 * num2:.2f}")
if op =="/" or op=="divide":
    if num2 ==0:
        print(f"{color.BOLD}{color.RED}ERROR! INVALID{color.END}")
    else:
        print(f"{num1} / {num2} = {num1/num2:.2f}")
if op =="%" or op=="percent":
    if num2==0:
        print(f"{color.BOLD}{color.RED}ERROR! INVALD {color.END}")
    else:
        print(f"({num1} / {num2})x100={(num1/num2)*100:.1f}%")
else:
    print(f"{color.BOLD}{color.RED} ERROR {op} this operator is not valid .{color.END}")