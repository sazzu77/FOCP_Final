#printing the heading
print("Swallow Speed Analysis: Version 1.0\n")

 #empty list to store data
x = [] 

 #taking input from the user
user_input = input("Enter the Next Reading: ") 

#condition for no data entered
if user_input == "":
    print("No readings entered. Nothing to do.")
    exit()
else:

    #loop begins for the input validation
    while user_input != "":

        #condition checking for alphabet u
        if user_input[0] == "u" or "U":
            print("Reading saved")

            #adding data to the new list after calculation
            x.append(float(user_input[1:])*1.61)
            user_input = input("Enter the Next Reading: ")

        #condition checking for alphabet e
        elif user_input[0] == "e" or "E":
            print("Reading saved")

            #adding the new data to new list after calculation
            x.append(float(user_input[1:]))
            user_input = input("Enter the Next Reading: ")
        else:
            break
    #condition checking if new list is non-empty
    if (len(x)!= 0):           
        print("\nResults summary\n")

        #printing the data after condition is fulfilled 
        print(len(x), "Reading Analysed\n")
        print(f"Max Speed: {max(x)/1.61:.1f} MPH,  {max(x):.1f} KPH")
        print(f"Min Speed: {min(x)/1.61:.1f} MPH,  {min(x):.1f} KPH")

        #initially average is set to 0
        average = 0
        
        #loop to check and prints average and time
        for i in range(len(x)):
            average = average + x[i]
        time = average/len(x)
        print (f"Avg Speed: {time/1:.1f} MPH,  {time:.1f} KPH.")
    else:
        print("Invalid")





