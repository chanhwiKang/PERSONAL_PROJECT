import os
TEKKEN_CHARACTER = {"7":{ # tekken_character = {series:{number:character}, series:{number:character}}
    "1" : "Ganryu", "2" : "Gigas", "3" : "Geese", "4" : "Negan", "5" : "Noctis", 
    "6" : "Nina", "7" : "Devil_Jin", "8" : "Dragunov", "9" : "Lars", "10" : "Chloe", 
    "11" : "Leo", "12" : "Lei_Wulong", "13" : "Law", "14" : "Lee_Chaolan", "15" : "Lidia", 
    "16" : "Leroy", "17" : "Lili", "18" : "Master_Raven", "19" : "Marduk", "20" : "Miguel" 
    }}
PATH = "/Users/gangchanhwi/Desktop/PERSONAL_PROJECT/tekken_command_list" # 유저 개인 파일 저장 경로
seriesChoice = "7"

characterFilePath = os.path.join(PATH, seriesChoice, "Geese.txt")

print(characterFilePath)
with open(characterFilePath, "r") as file:
    content = file.read()
    print(f"{content} 1차")
with open(characterFilePath, 'w+') as file:
    file.write("aaaaaaaa")
    content = file.read()
    print(f"{content} 2차")
with open(characterFilePath, 'a') as file:
    file.write("bbbbbbb")
    print(f"{content} 3차")
with open(characterFilePath, 'a+') as file:
    file.write("cccccccc")

    print(f"{content} 4차")
    # print(f"{content} 1차")
    # print(f"{content} 1차")
