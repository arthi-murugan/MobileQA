# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Guys')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("welcome to the TipCalculatorprogramm")
# "Calculating the total bill of the each person need to pays"
bill = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10,12, or 15?"))
people = int(input("How many people to split the bill?"))
tip_percent = tip/100
total_tip_amount = bill*tip_percent
total_bill = bill+total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: €{final_amount}")










