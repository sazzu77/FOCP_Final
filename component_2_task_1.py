#printing the heading
print("Stop! Who would cross the Bridge of Death. \nMust answer me these questions three, 'ere the other side he see.")

#taking input from the user
Question_1 = input("What is your name? ")

#processing input
if("Arthur" in Question_1 or "arthur" in Question_1):
    print("My liege! You may pass!")
else:
    Question_2 = input("What do you seek? ") #taking input for the quest

    #Question_2 processed
    if ("Grail" in Question_2 or "grail" in Question_2):  

        #input taken to match color with Question_1's first letter 
        Question_3 = input("What is your favorite colour? ") 
        if (Question_1.lower()[0] == Question_3.lower()[0]):
            print("You may pass!")
        else:
            print("Incorrect! Now you face the Gorge of Eternal Peril.")

    else:
        print("Only those who seek the grail may pass!")