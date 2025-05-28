

def main():
    #gather user input
    input_name = input("Input the name of the cat food: ")
    input_calories_per_kg = input("Input the number of calories/kg from your cat food: ")
    input_grams_per_container = input("Input the amount of food in grams per container: ")
    
    calories_per_container = calculate_calories_container(input_calories_per_kg, input_grams_per_container)
    formated_response = "Cat food:  " + input_name + " has " + str(calories_per_container) + " calories per container." 
    print(formated_response)

def calculate_calories_container(calories_per_kg, grams_per_container):
    calories_per_container = ((int(calories_per_kg) / 1000)*int(grams_per_container))
    return calories_per_container

if __name__ == "__main__":
    main()