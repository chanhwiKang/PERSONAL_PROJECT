while True:
    a = list(input())
    if a == "#":
        break
    print(a.count("a")+a.count("e")+a.count("i")+a.count("o")+a.count("u")+a.count("A")+a.count("E")+a.count("I")+a.count("O")+a.count("U"))
