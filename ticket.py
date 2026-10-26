age=int(input("Enter your age"))
if age<=17:
	price="free"
elif age<=12:
	price="100rs"
elif age<=25:
	is_student=input("you are student?(yes/no)").lower()
	if is_student=="yes":
		price="200rs"
	else:
		price="500rs"
elif age<=64:
	is_disbality=input("you are physically disability?(yes/no)").lower()
	if is_disbality=="yes":
		price="250rs"
	else:
		price="1000rs"
elif age>=65:
	is_disbality=input("you are physically disability?(yes/no)").lower()
	if is_disbality=="yes":
		price="250rs"
	else:
		price="500"
else:
	price="1000"
print("ticket price is:", price)