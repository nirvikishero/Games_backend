import random
import Truth_question
import dare_question
import google.generativeai as genai
import os
import google.generativeai as genai
#remove the below comment for ur use and use your api code from google api
# GOOGLE_API_KEY= genai.configure(api_key=os.environ('<your api code>')) #input your api code
# genai.configure(api_key=GOOGLE_API_KEY)


print('''
    This game is initial version made by Nirvik Nepal
                    version :1.0.0
                copyright@nirviknepal2024
                Play wisely and enjoy...   
                using limited day api code please help me to  get mine    
    ''')

try :
    for i in range(1,1000) :
        computer = random.randint(0,1)
        you = input("Enter Truth or Dare [Exit for exiting game and \"Your turn\" so that computer play] : ")
        if you.lower() == "truth" :
            truth_choice = random.randint(1,100)
            print(Truth_question.truth[truth_choice])
            truth_answer = input("Enter your Answer : ")
            with open("Truth_answers","a") as file :
                file.write(truth_answer+ "\n")
        elif you.lower() == "dare" :
            dare_choice = random.randint(1,100)
            print(dare_question.dare[dare_choice])
            dare_answer = input("complete your dare!!!!")
        elif you.lower() == "your turn" :
            if computer == 0 :
                print("Computer choosed  : truth ")
                comp_truth_question = input("Enter the quesstion you want to  ask the computer : ")
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(comp_truth_question)
                print(response.text)
            else :
                print("Computer choosed : dare ")
                comp_dare = input("Enter the task : ")
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(comp_dare)
                print(response.text)
        elif you.lower() == "exit" :
            exit()
        else :
            print("Invalid input !!!.\n\nChoose between Truth and Dare or \"Your turn\" for computer to play or Exit to exit the game.")
    
except Exception as e :
    print("An error occured while running the program:",e)
    
