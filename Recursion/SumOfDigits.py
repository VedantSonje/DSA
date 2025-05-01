
#number = 521
# return 8

#1s approach -  while to recusrsion

number = 4723
#s = 0
def Sum_Of_Digit(number):
    
    if number == 0:
        #
        
        #print("he")
        return 0
  
    reminder = number % 10
    reminder
    
    print(reminder)
    
    return  Sum_Of_Digit(number//10) + reminder
    
    
    
print(Sum_Of_Digit(number))

print(str(number))