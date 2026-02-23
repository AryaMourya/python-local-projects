#Expense Tracker Application Project

expenses = []
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

    expenses{
      "date":date,
      "category":category,
      "amount":amount
    }
  if (Choice == 2):
  if (Choice == 3):
  if (Choice == 4):