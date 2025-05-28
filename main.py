from logic import calculate_calories_container

def main():
    #gather user input
    input_name = input("Input the name of the cat food: ")
    input_calories_per_kg = input("Input the number of calories/kg from your cat food: ")
    input_grams_per_container = input("Input the amount of food in grams per container: ")
    

    calories_per_container = calculate_calories_container(input_calories_per_kg, input_grams_per_container)
    formated_response = "Cat food:  " + input_name + " has " + str(calories_per_container) + "calories per container" 
    print(formated_response)
    
if __name__ == "__main__":
    main()