def read_file(file):
	message = []
	new_message = []
	word = ""
	with open(file, "r", encoding = "utf-8-sig") as chat_file:
		for line in chat_file:
			message = line.split(" ")
			time = message[0]
			name = message[1]
			word = word.join(message[2:]).strip()
			new_message.append([time, name, word])
	return new_message

def check_message(lis):
	countA = 0
	countV = 0
	countPostA = 0
	countPostV = 0
	countimageA = 0
	countimageV = 0
	for data in lis:

		if data[1] == "Allen":
			if data[2] == "貼圖":
				countPostA += 1
			if data[2] == "圖片":
				countimageA += 1
			else:
				countA += len(data[2])

		else:
			if data[2] == "貼圖":
				countPostV += 1
			if data[2] == "圖片":
				countimageV += 1
			else:
				countV += len(data[2])

	print("Allen Words : ", countA, "/ Post : ",countPostA, "/ Image : ",countimageA)
	print("Viki  Words : ", countV, "/ Post : ",countPostV, "/ Image : ",countimageV) 
	
def print_file(lis):
	for line in lis:
		print(line)

def main():
	lis = read_file("LINE-Viki.txt")
	print_file(lis)
	check_message(lis)

if __name__ == '__main__':
	main()
