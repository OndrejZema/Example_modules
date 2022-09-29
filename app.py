from operator import mod
import mod1

def main():
    txt = input("Zadejte text")
    res = mod1.text_process(txt)
    print(res)


if __name__ == "__main__":
    main()