import random

print("-----------------------------------------------")


status=("CONTINUE", "WON", "LOST")
#The following constants represent commmon rolls of the dice
SNAKE_EYES = 2
TREY = 3
SEVEN = 7
YO_LEVEN = 11
BOX_CARS = 12

print("-----------------------------------------------") 
gamestatus=status[0]
mypoint=0
def rolldice():
	die1=random.randint(1,6)
	die2=random.randint(1,6)
	sum=die1+die2
	print ("Player rolled %d + %d = %d\n"%(die1,die2,sum))
	return sum
	
print("-----------------------------------------------")    
r=rolldice()   


if r==SEVEN or r==YO_LEVEN :
	  gamestatus== status[1]
	  print("Player wins")
	  exit()
	  
elif r==SNAKE_EYES or r==TREY or r==BOX_CARS:
	 
	 gamestatus==status[2]
	 print("Player loses")
	 exit()
	 
     
	
else:
	gamestatus==status[0]
	mypoint=r 
print("MY POINT1")
print("Point is %d"%(mypoint))	
    	
    


print("----------------------------------------")  
      
while gamestatus==status[0]:
	   r=rolldice()
	   if r==mypoint:
		   gamestatus=status[1]
	   elif r==SEVEN:
		   gamestatus= status[2]
	  
		    
		 
  

if gamestatus==status[1]:  
                print("Player wins")
else:
	         print ("Player loses ") 
      
    
		 




