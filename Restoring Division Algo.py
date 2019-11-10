import random

def subtract(Rem, div):
	Ans = []
	C = 0
	for j in range(len(Rem)):
		i = len(Rem) - 1 - j;
		A = int(Rem[i])
		B = int(div[i]);
		Ans = [str((A^B)^C)] + Ans
		C = (A^1)*(B or C) or (B*C)
	# print(ToString(Ans))
	return Ans


def ToString(Arr):
	ans = ''
	for i in Arr:
		ans += i
	return ans


def RestoreDivision(dividend, divisor):

	case = 0

	if(dividend > 0 and divisor<0):
		case = 1
	if(dividend < 0 and divisor > 0):
		case = 2
	if(dividend < 0 and divisor < 0):
		case = 3

	divisor = abs(divisor)
	dividend = abs(dividend)

	if divisor > dividend:
		Quotient = 0
		Remainder = dividend

	else:
		# Restoring Algo
		# Div is the divisor register
		# Rem is the remainder register
		# Quo is the Quotient register 
		# Restore is the register that stores restoration bit


		# Step 1 - Initializing values
		Div = [i for i in format(divisor, "b")];
		Quo = [i for i in format(dividend, "b")];
		n = len(Quo);
		Rem = ["0"]
		for i in range(n):
			Rem+=["0"];
		for i in range(n - len(Div) + 1):
			Div = ["0"] + Div;
		Restore = 0
		# print(n, ToString(Div), ToString(Rem), ToString(Quo), Restore)


		#Algo start
		while n  > 0:
			# Shift remainder left
			for i in range(len(Rem) - 1):
				Rem[i] = Rem[i+1]
			Rem[len(Rem) - 1] = Quo[0]

			# Subracting Divisor from Remainder
			PossibleRem = subtract(Rem, Div)
			if PossibleRem[0] == '1':
				Restore = 0
			else:
				Restore = 1
				Rem = PossibleRem

			# Shifting quotient while restoring the last bit
			for i in range(len(Quo) - 1):
				Quo[i] = Quo[i+1]
			Quo[len(Quo) - 1] = str(Restore)
			# print(n, ToString(Div), ToString(Rem), ToString(Quo), Restore)

			n -= 1

		Remainder = ''
		Quotient = ''
		for i in Rem:
			Remainder += i

		for i in Quo:
			Quotient += i

		# Converting back to decimal
		Quotient = int(Quotient, 2)
		Remainder = int(Remainder, 2)

	# Checking for negative numbers explicitly
	if(case == 1 ):
		Quotient = (-1)*Quotient
		if(Remainder != 0):
			Quotient -= 1
			Remainder -= divisor
	if(case == 2):
		Quotient = (-1)*Quotient
		if(Remainder != 0):
			Quotient -= 1
			Remainder = (-1)*Remainder + divisor
	if(case == 3):
		Remainder = (-1)*Remainder 

	return (Quotient, Remainder)






if __name__ == '__main__':

	passed = True

	print("Enter the value of dividend and enter")
	try:
		dividend = int(input());
	except:
		print("Not a valid dividend")
		passed = False
	print("Enter the value of divisor and enter")
	try:
		divisor = int(input());
	except:
		print("Not a valid divisor")
		passed = False

	if divisor == 0:
		print("ERROR : Division by 0 ")
	elif passed != False:
		Quotient, Remainder = RestoreDivision(dividend, divisor);

		print("Quotient is ", Quotient)
		print("Remainder is ", Remainder)
	# Testing Portion
	# passed = 0
	# failed = 0
	# for i in range(8000):
	# 	dividend = random.randint(-1001,1000)
	# 	divisor = random.randint(-1001,1000)
	# 	if(divisor != 0):
	# 		Quotient1, Remainder1 = RestoreDivision(dividend,divisor)
	# 		Quotient2 = dividend // divisor
	# 		Remainder2 = dividend % divisor
			
	# 		if(Quotient1 == Quotient2 and Remainder1 == Remainder2):
	# 			# print(i+1, " Pass")
	# 			passed += 1
	# 		else:
	# 			print(i+1, dividend, divisor, Quotient1, Quotient2,Remainder1, Remainder2);
	# 			print(i+1 , " Fail")
	# 			failed += 1
	# print(passed)
	# print(failed)



