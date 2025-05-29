from logic import calculate_calories_container
from verify_input import check_value
from format_output import format_output
def main():
    #gather user input
    input_name = input("Input the name of the cat food: ")   
    input_grams_per_container = check_value("Input the amount of food in grams per container label: ")
    input_calories_per_kg = check_value("Input the number of calories/kg from your cat food: ")

    calories_per_container = calculate_calories_container(input_calories_per_kg, input_grams_per_container)
    
    print(format_output(input_name, calories_per_container))

    
if __name__ == "__main__":
    main()