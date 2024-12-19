##################################################################################
#   Medical Chatbot System For the AI Final Assignment using Top-down approach   #
##################################################################################

def menu():
    print("\nWelcome to the Diabetes Guidance Chatbot!")
    print("Please select a category:")
    print("1. Learn about diabetes")
    print("2. Understand diabetes risk factors")
    print("3. Get healthy lifestyle advice")
    print("4. Explanation of prediction results")
    print("5. Exit")

def subMenu(option):
    if option == 1:
        print("\nLearn about diabetes:")
        print("1. What is diabetes?")
        print("2. What are the types of diabetes?")
        print("3. Back to main menu")
    elif option == 2:
        print("\nUnderstand diabetes risk factors:")
        print("1. What are the common risk factors?")
        print("2. Am I at risk of diabetes?")
        print("3. Back to main menu")
    elif option == 3:
        print("\nHealthy lifestyle advice:")
        print("1. How can I manage my blood sugar?")
        print("2. What foods should I eat?")
        print("3. Back to main menu")
    elif option == 4:
        print("\nExplanation of prediction results:")
        print("1. What does my prediction mean?")
        print("2. What should I do with my result?")
        print("3. Back to main menu")

def detailedRes(option, subOption):
    responses = {
        (1, 1): "Diabetes is a chronic condition where the body cannot effectively use insulin to regulate blood sugar.",
        (1, 2): "There are three main types of diabetes: Type 1, Type 2, and gestational diabetes during pregnancy.",
        (2, 1): "Common risk factors include obesity, lack of exercise, unhealthy diet, genetics, and high blood pressure.",
        (2, 2): "You may be at risk if you have a family history, are overweight, or live a sedentary lifestyle.",
        (3, 1): "To manage blood sugar, maintain a healthy diet, exercise regularly, monitor your blood sugar, and consult your doctor.",
        (3, 2): "Focus on whole grains, vegetables, lean proteins, and avoid sugary and processed foods.",
        (4, 1): "Your result indicates your diabetes risk. High scores suggest a need for lifestyle changes or a check-up.",
        (4, 2): "You should consult a healthcare provider for accurate advice based on your prediction result.",
    }
    return responses.get((option, subOption), "[!] Invalid selection, please try again...")

def chatbot():
    while True:
        menu()
        try:
            option = int(input("\n[+] Please enter your choice (1-5): "))
            if option == 5:
                print("Thank you for using the Diabetes Guidance Chatbot. Goodbye!")
                break
            elif option in [1, 2, 3, 4]:
                while True:
                    subMenu(option)
                    subOption = int(input("\n[+] Please enter your choice (1-3): "))
                    if subOption == 3:
                        break
                    response = detailedRes(option, subOption)
                    print("\nBot:", response)
            else:
                print("[!] Invalid choice, Please enter a number between 1 and 5...")
        except ValueError:
            print("[!] Invalid input, please enter a number...")

if __name__ == "__main__":
    chatbot()
