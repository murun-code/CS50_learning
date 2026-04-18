#week one of CS50P 
 """ 
  i learned some neat assignment stuff today 
  print()
  input()
  equal sign doesnt mean equal, its assignment
  end=()
  if you wanna use a function, it has to exist already above it

  """
#i played around and changed the code from the CS50 one
def main():
  name = input("What is your name? -  ").strip().title()
  hello(name)
def hello(to="world"):
  print("Cool name!", to)
def love():
  print("What a beautiful world...")
love()
main()
