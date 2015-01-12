#Jen Anderson
#anderjen@onid.oregonstate.edu
#CS311-400
#Homework2
#Problem6

##################################################################
#  							         #
#  This function takes the 1000 digit number and seperates each  #
#  number into its own string element with the list method,      #
#  then converts each string element back to a int. 		 #
#						                 #
##################################################################

def numIntoArray():
	number = 5369781797784617406495514929086256932197846862248282166370484403199890008895243450658541227588666881164271714799244429282308634656748139191231628245861786645835912456652947654568284891288314260769004265727333001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553970719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606058861164671094050775410022569831552000559357297252421902267105562632111110937054421750694165896040812540698747158523863050715693290963295227443043557668966489504452445231617318564030987111217223831136222989342338030813533627661428280644448664523874930358907296290491560440772390713810515859307960866701724271218839987979087922749219016997208880937767163626956188267042825248360082325753042075296345073167176531330624919225119674426574742355349194934839722413756570560574902614079729686524145351004749698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511
	number_string_array = list(str(number))
	intsArray = []
	x = 0
	while x < len(number_string_array):
		numAsInt = int(number_string_array[x])
		intsArray.append(numAsInt)
		x += 1
	return intsArray

##################################################################
#								 #  
#  This method finds all the products of five consequtive        #
#  numbers and returns the products in an array called           #
#  products							 #
#						                 #
##################################################################

def getProducts(arrayOfInts):
	products = []
	for i in range(len(arrayOfInts)):
		if len(arrayOfInts) > i + 4:
			product = arrayOfInts[i] * arrayOfInts[i+1] * arrayOfInts[i+2] * arrayOfInts[i + 3] * arrayOfInts[i+4]
			products.append(product)
	return products

##################################################################
#								 #
#  This section calls out the functions to output the 		 #
#  greatest int from the products array				 #
#								 #
##################################################################

myArray = numIntoArray()
myProducts = getProducts(myArray)
print max(myProducts)
