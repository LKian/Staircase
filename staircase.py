step = raw_input("What character do you want to use for the steps?\n")
levels = input("How many floors do you like to build? \n")
floor = 1
while floor <= levels:
	print step*floor
	floor+=1