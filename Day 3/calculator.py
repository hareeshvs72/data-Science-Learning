


print("welcome to calculator")



def calculator() :
    try:
        
      a = float(input("Enter First Number"))
      b = float(input("Enter Second  Number"))
      
      op = input("Choose operation (+, -, *, /): ")
      
      if op not in ['+', '-', '*', '/'] :
          raise ValueError("Invalid operation selected")
      if op == '+':
            print("Result:", a + b)

      elif op == '-':
            print("Result:", a - b)

      elif op == '*':
            print("Result:", a * b)

      elif op == '/':
            if b == 0:
             raise ZeroDivisionError("Cannot divide by zero")
            print("Result:", a / b)
    except ValueError :
     print("Invalid input! Please enter numbers only.")
    except TypeError :
        print("Type error occurred")
    except ZeroDivisionError:
      print("Cannot divide by zero")

    finally:
        print("Calculator finished execution")

calculator()