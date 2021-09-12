#########################################################################
### A pratical exercise in converting base 10 number into hexidecimal ###
### Written by: 0pt10n2 9-12-2121                                     ###
#########################################################################

#a dictionary containing the double digit values for hex
dictA = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

#the final result will be stored here and added to the prepositioned string indicating a hex value
finalValue = "0x"

#the list used to store the itteration 
hexNum = []

#base number, added this so that i can expand the function of the program if needed
base = 16

#Gathering the user input
print("What is the base 10 number to convert to hexidecimal: ")

#Storing the user input as a whole number for processing
a = float(input())


#######################################
###functions above, loop code below###
#######################################

while a > 0:
	b = a/base  #divide the input number by the base number to start the process
	c = int(b)  #this is your whole value
	d = b - c   #this is your decimal value
	hexUnit = d * base  #multiply the decimal by base number to get the hex unit

	#processing when the number will be converted to a letter
	if hexUnit > 9:
		#storing the key value so we can pull the appropriat letter from dictA
		findLetter = dictA[hexUnit]
		#lets add it to the list that we will parse to make the hex value
		hexNum.insert(0, findLetter)
	#actions to take place when the number is a single digit
	else: hexNum.insert(0, int(hexUnit))
		
	#this is the new whole value
	a = c  

for i in range(0, len(hexNum)):
	value = hexNum[i]
	finalValue = finalValue + str(hexNum[i])

#we made it! Printing the result.	
print("The hexidecimal conversion is: ", finalValue)
	
	
	


