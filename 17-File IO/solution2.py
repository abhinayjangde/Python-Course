with open("poem.txt", "r") as f:
    content = f.read()
    if "twinkle" in content:
        print("Twinkle is present")
    else:
        print("Twinkle is not present")