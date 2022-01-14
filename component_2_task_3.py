from random import choice

#heading printed
print("Welcome to Popchat\nOne of our operators will be pleased to help you today.")

#List of helpdesk operators
Ask_me = ["Aamir","Abrar","Amzad","Anwar","Ansari"]      

#List to check for network error
probability_list = [7,7,7,7,3,7,7,7,7]               

 #Input email from user
university_email = input("Please enter your Poppleton email address: ")    #Input email from user
count = 0

valid = False

#condition for email validation
if "@" in university_email:           
    s = university_email.split("@")    

    #counter variables for characters
    count = 0     

    #for loop to extract characters before "@"          
    for i in s[0]:         
        count += 1          

   
    if count >=2 and s[1] == "pop.ac.uk":   
        valid = True 

        #choosing random operator
        operator = choice(Ask_me)     

        #showing possibility of any random number from the list        
        probability = choice(probability_list)  

        #printing user prompt input
        print("Hi,",s[0].capitalize()," Thank you, and welcome to PopChat!")   
        print("My name is",operator,", and it will be my pleasure to help you.")
        
        #condition for network error 
        if probability == 3:    
            print("*** NETWORK ERROR ***")
            print("Thanks,",s[0].capitalize(),"for using PopChat. See you soon!")
            exit()

        #loop executes only when the email is valid
        while True:
            #input for what user wants
            user_input = input("----> ")  

            #list to be printed other than user_input 
            invalid_prompt = ["Mmmmmm","Sorry sir!","I didn't understand","Match doesn't found","Oh yes i see"]


            #ending the chat whenever user wants
            exit_input = ["EXIT","STOP","QUIT","END","GOODBYE","BYE"]


            #random reply from the user_input
            random_reply = choice(exit_input)

            #conditions to meet the parameters
            if "WIFI" in user_input.upper():
                print("The wifi is excellent around campus.")
            elif "LIBRARY" in user_input.upper():
                print("The library is closed today.")
            elif "DEADLINE" in user_input.upper():
                print("Your deadline has been extended by two working days.")
            elif "FOOD" in user_input.upper() or "CAFETERIA" in user_input.upper() or "LUNCH" in user_input.upper():
                print("The cafeteria is on the ground floor right infront of the bank.")
            elif "WASHROOM" in user_input.upper():
                print("The washroom is around the far-west corner of each floor.")
            elif "GYM" in user_input.upper():
                print("The GYM is next to the main building.")
            elif "SERVER ROOM" in user_input.upper():
                print("The server room is off-limits. Authorized personnel only!")
            else:

            #loop to end chat if any condition matches
                for j in exit_input:
                    if j in user_input.upper():
                        print("Thanks,",s[0].capitalize(),"for using PopChat. See you soon!")
                        exit()
                else:
                    print(random_reply)
    else:
        #printing the message if email is invalid
        print("Email is invalid")      
else:
    #prints message if @ is not matches
    print("Email is invalid")           
    exit()

