
scorenumber = input("How many numbers shall I average? ") 


counter = 0 
tempnumber1 = 0 
tempnumber2 = 0.0 
 

while counter < scorenumber: 
    counter = counter + 1 
    tempnumber1 = input("Provide one of the numbers to average. ") 
    tempnumber2 = tempnumber1 + tempnumber2 
    print (tempnumber2) 
scoresum = tempnumber2 
print ("The sum of your scores") is  + str(scoresum) 

average = scoresum / scorenumber 
print ("The average is ") + str(average)
