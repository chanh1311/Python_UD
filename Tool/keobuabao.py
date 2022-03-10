import random
print("Nhap vao: Keo,Bua,Bao!")
player = input()
while player != "Keo" and player != "Bua" and player != "Bao":
	print("Ban da nhap sai,Nhap lai!")
	player = input()
computer = random.randint(0,2)
if computer == 0:
	computer = "Keo"
elif computer == 1:
	computer = "Bua"
else:
	computer = "Bao"
print("Player :" + player)
print("Computer:" + computer)
print("Ket Qua:")
if player == computer:
	print("Hoa")
else:
	if player == "Keo":
		if computer == "Bua":
			print("Thua")
		else :
			print("Thang")

	elif player == "Bua":
		if computer == "Keo":
			print("Thang")
		else :
			print("Thua")

	elif player == "Bao":
		if computer == "Keo":
			print("Thua")
		else :
			print("Thang")
	

		