with open("pr1.txt", "r") as f:
    content = f.read()
newContent = content.replace("Whatsapp", "YouTube")
with open("pr1.txt", "w") as f:
    f.write(newContent)