import operator

saved_string = ''

def remove_letter():	#remove a selected letter from a string
	print "Remove Letter"
	return 0

def num_compare():	#Compare 2 numbers to determine the larger
	print "Num Compare"
	return 0

def print_string():	#print the preivously stored string
	print "Print String"
	print saved_string
	return 0

def calculator(): #basic calculator (add, substract, multiplication, division)
	print "Calculator"
	
	sign_dict = {'+': operator.add(), '-': operator.minus(), '*': operator., '%': %}
	num1 = int(raw_input("first number: "))
	sign = str(raw_input("Action: "))
	num2 = int(raw_input("Input second number: "))
	
	num1 sign_dict(sign) num2
	
	return 0

def accept_and_store():	#Accept and store a string
	print "Accept and store"
	global saved_string
	saved_string = str(raw_input("Input String: "))
	return 0

def main():	#Menu goes here
	opt_list = [accept_and_store,
				calculator, 
				print_string,	
				num_compare, 
				remove_letter]

	while(True):
		print "Select Option:"
		print "1\t Accept and Store"
		print "2\tCalculator"
		print "3\tPrint String"
		print "4\tNumber Comparison"
		print "5\tLetter Remover"
		opt_choice = int(raw_input("Selection: "))
		opt_choice -= 1
		opt_list[opt_choice]()
 
	return 0


main()
