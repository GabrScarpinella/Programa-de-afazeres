while True:
    c=str(input(""))
    if c=="q":
        break
    elif c=="a":
        arq=open("afazeres.txt", "a")
        t=str(input(""))
        arq.write(t)
        arq.write("\n")
        arq.close()
    elif c=="r":
        arq=open("afazeres.txt", "r")
        t=arq.readlines()
        arq=open("afazeres.txt", "w")
        for i in range(1, len(t)):
            arq.write(t[i])
        arq.close()
    elif c=="l":
        arq=open("afazeres.txt", "w")
        arq.write("")
        arq.close()
    elif c=="m":
        arq=open("afazeres.txt", "r")
        t=arq.readlines()
        for i in range(len(t)):
            print(f"{i}: {t[i]}")