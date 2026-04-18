#square calculator
"""
cool math things
int stands for integer (negative infinity to postive infinity, only whole number 1,2,3 etc)
def stands for define  (very useful, i think it will be used in like everything)
im still bit confused about where to place the def for program to actually work 
return literally returns your values (you can adjust if you want your input transformed or no)
math is pretty easy with this, i might show my friends a calculator i made
you should always put int if you are dealing with numbers or the program will think its a text and will just do 3+4=34
pow function helps you do exponent stuff like pow(3, 4) (three to the power of 4), really interested to see what would happen if you
code square root of -1, maybe i or error? 
"""
def main():#defining main with command it doesnt run till commanded so you can put many def where ever you want i think
  x = int(input("What's x? "))
  print("x squared is", square(x))
def square(n):
  return int(pow(n, 2)) #dunno if the integer is necessary or not             
main()
