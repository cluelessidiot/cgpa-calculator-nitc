def file():
    f=open("a.txt","r")
    a=int(f.readline())
    print(a)
    a=int(f.readline())
    a=str(f.readline())
    print(a)


if __name__ == '__main__': 
    file()