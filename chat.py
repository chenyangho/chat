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

def show(new_message):
	for line in new_message:
		print(line)

def main():
	read_file("input.txt")
	change_message(message)
	show(new_message)

main()