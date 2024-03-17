import calendar
import datetime
from expenses import Expense


def main():
    print(f"👇Running Expense Tracker!")
    expense_file_path="expense.csv"
    budget=2000

    # Get user input for expense
    expense=get_user_expense()
    

    # Write their expense to a file
    save_expense_to_file(expense,expense_file_path)

    # Read file and summarise expenses
    summarize_expenses(Expense,expense_file_path)
    
def get_user_expense():
   print(f"Getting user Expense")
   expense_name= input("Enter expense name:")
   expense_amount=float( input("Enter expense amount:"))
   expense_categories=[
      "🍔Food",
      "🏠Home",
      "🧑‍⚕️Work",
      "🤩Fun",
      "🌟Misc",
   ]

   while True:
      print("Select a category:")
      for i,category_name in enumerate(expense_categories):
         print(f"{i+1}.{category_name}")

         value_range =f"[1-{len(expense_categories)}]"
         selected_index=int(input(f"Enter a category number{value_range}"))

         if selected_index in range(len(expense_categories)):
           selected_category=expense_categories[selected_index]
           new_expense=Expense(name=expense_name,category=selected_category,amount=expense_amount)
         return new_expense
      else:
         
         print("Invalid Category.Please try again!")

      
   
def save_expense_to_file(expense,expense_file_path):
   print(f"Saving user Expense: {expense} to {expense_file_path}")
   with open(expense_file_path,'a') as f:
      f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path,budget):
   print(f"Summarizing user Expense")
   expenses:list[Expense]=[]
   with open(expense_file_path,'r') as f:
      lines=f.readlines()
      for line in lines:
         stripped_line=line.strip()
         expense_name,expense_amount,expense_category=stripped_line.split(",")
         line_expense=Expense(name=expense_name,amount=expense_amount,category=expense_category)
         print(line_expense)
         summarize_expenses.append(line_expense)



         amount_by_category={}
         for expense in summarize_expenses:
            key=expense.category 
            if key in amount_by_category:
               amount_by_category[key]+=expense_amount
            else:
               amount_by_category[key]=expense_amount

               print("Expenses By category:")
               for key,amount in amount_by_category.items():
                  print(f"  {key}:$(amount:.2f)" )

               total_spent=sum({x.amount for x in expenses})
               print(f"You've spent ${total_spent:.2f} this month!")

               remaining_budget=budget - total_spent
               print(f"✅Budget Remainng:${total_spent:.2f}this month!")

                 
               now=datetime.datetime.now()
               days_in_month=calendar.monthrange(now.year,now.month)[1]
               remaining_days=days_in_month-now.day
               print("Remaining days in the current month:",remaining_days)

               daily_budget=remaining_budget/remaining_days
               print(f"✅Budget per day: ${daily_budget:.2f}")
if __name__=="__main__":
  main()