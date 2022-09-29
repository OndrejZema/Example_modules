def write_number(text):
    with open("num.txt", "a") as file:
        if int(text) > 100:
            file.write(text)
        else:
            return -1