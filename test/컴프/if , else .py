score = int(input("input Score: "))

if(score < 0 or 100 < score):
    print("Please input the number between 0 - 100 ")

else:
    if(score >= 95):
        print("Your grade is 'A+'")
    elif(90 <= score < 95):
        print("Your grade is 'A'")
    elif(85 <= score and score < 90):
        print("Your grade is 'B+'")
    elif(80 <= score) and (score < 85):
        print("Your grade is 'B'")
    elif(75 <= score < 80):
        print("Your grade is 'C+'")
    elif(70 <= score < 75):
        print("Your grade is 'C'")
    else:
        print("Plse Take this class again")
        
