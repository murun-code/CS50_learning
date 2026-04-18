"""
Homework of Week 0 - made my first python program!
Made this to calculate how many months it will take to 
save up for a goal based on my current situation
i really want a MBP M4 and IPhone 16 pro so 
hope i can save up for them in time!!
used some ai to help me find errors but mainly i wrote them all
"""
import math

def main():
    name = input("hello! what is your name? - ").strip().title()
    print("Cool name!", name)
    monthly = input("How much are you gonna save up monthly? - ")
    summer_cash = input("And how much are you gonna earn from summer jobs? - ")
    goal = input("What is the price of your goal? - ")
    months = calculate_months(goal, monthly, summer_cash)
    print(f"you will reach your goal in approximately {months} months!")
    pass

def calculate_months(goal, monthly, summer_cash):
    months = math.ceil((float(goal) - float(summer_cash)) / float(monthly))
    return months  

main()
