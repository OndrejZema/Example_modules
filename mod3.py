def write_text(text):
    with open("txt.txt", "a+") as file:
        if len(file.readlines()) < 20:
            file.write(text)
        else:
            return -1