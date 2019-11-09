import numpy as np

x_bits = 11
y_bits = 11
length = x_bits + y_bits +1
print("Enter 1 to multiply and 2 to divide")
choice = int(input())
if(choice == 1):
	print("Enter numbers to be multiplied")
	x = int(input())  
	y = int(input())

	x_binary = np.binary_repr(x, x_bits)  # convert x to binary
	y_binary = np.binary_repr(y, y_bits)  # convert y to binary
	neg_x_binary = np.binary_repr(-1*x, x_bits)  # convert -x to binary
	# print("x", x_binary, "-x", neg_x_binary, 'y', y_binary)
	y_zero_string = ''
	x_zero_string = ''
	for i in range(0, y_bits+1):
		y_zero_string += '0'
	for i in range(0, x_bits):
		x_zero_string += '0'
	A = x_binary + y_zero_string  # A = x_binary + (y_bits + 1) 0
	S = neg_x_binary + y_zero_string  # S = negative_x_binary + (y_bits + 1) 0
	P = x_zero_string + y_binary + '0'  # P = (x_bits) 0 + y_binary + 0
	# print("A", A, "S", S, "P", P)
	count = 0

	while(count < y_bits):
		# print("count", count)
		righ_bits_P = P[-2:]  # find rightmost 2 bits of P

		if(righ_bits_P == "01"):  
			sum_val_decimal = int(P,2) + int(A,2)  # add P and A in decimal form
			# print('P={}'.format(P))
			# print('A={}'.format(A))
			# print('sum_val_decimal={}'.format(sum_val_decimal)) 
			sum_val = np.binary_repr(sum_val_decimal, length)  # convert back to binary
			# print('sum_val={}'.format(sum_val))

		elif(righ_bits_P == '10'):
			sum_val_decimal = int(P,2) + int(S,2)  # add P and S in decimal form
			# print('P={}'.format(P))
			# print('S={}'.format(S))
			# print('sum_val_decimal={}'.format(sum_val_decimal))
			sum_val = np.binary_repr(sum_val_decimal, length)  # convert back to binary
			# print('sum_val={}'.format(sum_val))

		else:  # if rightmost bits are 00 or 11
			sum_val = P
		# print("sum_val", sum_val)
		sum_val = sum_val[-1*length:]

		if(sum_val[0] == '1'): 
			P = '1' + sum_val[:-1]  # rightward shift of P
		if(sum_val[0] == '0'):
			P = '0' + sum_val[:-1]  # rightward shift of P
		# print("P", P)
		count += 1

	ans_binary = P[:-1]  # remove the rightmost bit in P
	temp = ''
	neg = False
	if(ans_binary[0] == '1'):  # if most significant bit is 1 then answer is negative
		neg = True
		for i in range(len(ans_binary)):
			if(ans_binary[i] == '1'):
				temp += '0'
			if(ans_binary[i] == '0'):
				temp += '1'
		ans_decimal = int(temp, 2) + 1
		ans_decimal = -1 * ans_decimal
	else:
		ans_decimal = int(ans_binary, 2)  # else answer is positive

	print("Binary answer: ", ans_binary)
	print("Decimal answer ", ans_decimal)

else:
	print("Enter numbers to be divided")
	x = int(input())
	y = int(input())
