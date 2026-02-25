#Expense Tracker Application Project

expensesList = []
print("Welcome to Expense Tracker")

while True:
  print("====MENU====")
  print ("1.Add Expense")
  print("2.View All Expenses")
  print("3.View Total Spending")
  print("4.Exit ")
  print("============")

  Choice = int(input("Enter your choice (1-4)"))

#ADD Expense 
  if (Choice == 1):
    date=input("Enter the date when expense is made(dd/mm/yy):")
    category =input("which kind of expense is made:")
    amount =float(input("Enter the amount of expense is made: Rs"))

    expenses={
      "date":date,
      "category":category,
      "amount":amount
    }
    expensesList.append(expenses)
    print("\n Expense is added succesfully !")

#View Expense
  elif (Choice == 2):
    if(len(expenses)==0 ):
      print("No Expenses recorded.")
    else:
      print("*****This is the total expenses******") 
      count=1
      for each_expense in expensesList:
        print(f"{count}EXPENSE => {each_expense["date"]},{each_expense["category"]},{each_expense["amount"]} ")
        count=count

#View total Expense      
  elif (Choice == 3):
    total= 0
    for each_expense in expensesList:
      total =total + each_expense["amount"]

    print("\n TOTAL EXPENSE =", total)

#Exit
  elif(Choice == 4):
    print("Thank You ! for using this finance tracker")
    break
  else:
    print("INVALID CHOICE")