message = []
new_message = []

def read_file(file):
	with open(file, "r", encoding = "utf-8-sig") as chat_file:
		for line in chat_file:
			message.append(line.strip())

def change_message(message):
	name = None
	for line in message:
		if line == "Allen" or line == "Tom":
			name = line
			continue
		if name:
			new_message.append(name + ": " + line)

def print_file(output):
 	with open(output, "r", encoding = "utf-8-sig") as new_chat_file:
 		for line in new_chat_file:
 			print(line.strip())

def write_file(file):
	with open(file, "w", encoding = "utf-8-sig") as new_file:
		for line in new_message:
				new_file.write(line + "\n")

def main():
	read_file("input.txt")
	change_message(message)
	write_file("output.txt")
	print_file("output.txt")

if __name__ == '__main__':
	main()
