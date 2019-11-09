import numpy as np
max_bits = 10
x_bits = 4
y_bits = 4
length = x_bits + y_bits +1
print("Enter 1 to multiply and 2 to divide")
choice = int(input())
if(choice == 1):
	print("Enter numbers to be multiplied")
	x = int(input())  
	y = int(input())
	if(x < y):  # x should be the larger of the two numbers
		temp = y
		y = x
		x = temp
	x_binary = np.binary_repr(x, x_bits)  # convert x to binary
	y_binary = np.binary_repr(y, y_bits)  # convert y to binary
	neg_x_binary = np.binary_repr(-1*x, x_bits)  # convert -x to binary
	print(x_binary, neg_x_binary, y_binary)
	A = x_binary + '00000'  # A = x_binary + (y_bits + 1) 0
	S = neg_x_binary + '00000'  # S = negative_x_binary + (y_bits + 1) 0
	P = '0000' + y_binary + '0'  # P = (x_bits) 0 + y_binary + 0
	print("A", A, "S", S, "P", P)
	count = 0
	while(count < y_bits):
		print("count", count)
		righ_bits_P = P[-2:]  # find rightmost 2 bits of P
		if(righ_bits_P == "01"):  
			sum_val_decimal = int(P,2) + int(A,2)  # add P and A in decimal form
			print('P={}'.format(P))
			print('S={}'.format(S))
			print('sum_val_decimal={}'.format(sum_val_decimal))  # convert back to binary
			sum_val = np.binary_repr(sum_val_decimal, length)
			print('sum_val={}'.format(sum_val))
		if(righ_bits_P == '10'):
			sum_val_decimal = int(P,2) + int(S,2)  # add P and S in decimal form
			print('P={}'.format(P))
			print('S={}'.format(S))
			print('sum_val_decimal={}'.format(sum_val_decimal))
			sum_val = np.binary_repr(sum_val_decimal, length)  # convert back to binary
			print('sum_val={}'.format(sum_val))
		else:  # if rightmost bits are 00 or 11
			sum_val = P
		print("sum_val", sum_val)

		if(sum_val[0] == '1'): 
			P = '1' + sum_val[:-1]  # rightward shift of P
		if(sum_val[0] == '0'):
			P = '0' + sum_val[:-1]  # rightward shift of P
		print("P", P)
		count += 1

	ans_binary = P[:-1]  # remove the rightmost bit in P
	temp = ''
	neg = False
	if(ans_binary[0] == '1'):  # if most significant bit is 1 then answer is negative
		neg = True
	print("ans_binary", ans_binary)
	for i in range(len(ans_binary)):
		if(ans_binary[i] == '1'):
			temp += '0'
		if(ans_binary[i] == '0'):
			temp += '1'
	print("temp", temp)
	ans_decimal = int(temp, 2) + 1
	if(neg):
		ans_decimal = -1 * ans_decimal

	print("Binary answer: ", ans_binary)
	print("Decimal answer ", ans_decimal)

else:
	print("Enter numbers to be divided")
	x = int(input())
	y = int(input())
