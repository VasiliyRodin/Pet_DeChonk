##this is  used to check if the input of cal/kg or grams/container is a float or int. if user inputs text it returns false
##The prompt gets passed from main to make it easier to understand in main what that function will ask for.

def check_value(prompt):
    while True:
        try:
            value = float(input(prompt)) ## Can't turn letters into float
            if value <= 0:
                print("Use a number greater than 0")
                continue   ## Goes back to start.
            return value
        except ValueError: ##Goes back to start.
            print("Please input a number")
