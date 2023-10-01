import os
TEKKEN_SERIES = ["1", "2", "3", "4", "5", "6", "7", "8", "tt1", "tt2"]
TEKKEN_CHARACTER = {"7":{ # tekken_character = {series:{number:character}, series:{number:character}}
    "1" : "Ganryu", "2" : "Gigas", "3" : "Geese", "4" : "Negan", "5" : "Noctis", 
    "6" : "Nina", "7" : "Devil_Jin", "8" : "Dragunov", "9" : "Lars", "10" : "Chloe", 
    "11" : "Leo", "12" : "Lei_Wulong", "13" : "Law", "14" : "Lee_Chaolan", "15" : "Lidia", 
    "16" : "Leroy", "17" : "Lili", "18" : "Master_Raven", "19" : "Marduk", "20" : "Miguel" 
    }}
PATH = "/Users/gangchanhwi/Desktop/PERSONAL_PROJECT/tekken_command_list" # 유저 개인 파일 저장 경로
TEXT = "made_by_chanhwi___"

def isCorrectSeries():
    while True:
        inputSeries = input("시리즈 입력(예: 6, 7, tt2): ")
        seriesFolderPath = os.path.join(PATH, inputSeries)
        if inputSeries in TEKKEN_SERIES:
            makeSeriesFolder(seriesFolderPath, inputSeries) # 시리즈 폴더 생성
            return inputSeries
        else:
            print("올바른 시리즈 입력바람")

def makeSeriesFolder(seriesFolderPath, inputSeries):
    try:
        os.makedirs(seriesFolderPath)
        print(f"폴더 '{inputSeries}'가 '{PATH}' 디렉토리 내에 생성되었습니다.")
    except FileExistsError:
        print(f"폴더 '{inputSeries}'가 '{PATH}' 디렉토리 내에 존재합니다.")
    except Exception as e:
        print(f"폴더를 만들던 중 에러 발생. 찬휘를 찾아주세요.\n{e} ")

def printCharacterList(series):
    if series == "7":
        print("\
-----------------------------------------------------------------------------\n\
                                    TEKKEN7\n\
 1 : Ganryu  2 : Gigas       3 : Geese           4 : Negan        5 : Noctis \n\
 6 : Nina    7 : Devil_Jin   8 : Dragunov        9 : Lars        10 : Chloe \n\
11 : Leo    12 : Lei_Wulong 13 : Law            14 : Lee_Chaolan 15 : Lidia \n\
16 : Leroy  17 : Lili       18 : Master_Raven   19 : Marduk      20 : Miguel\n\
-----------------------------------------------------------------------------")
    elif series == "6":
        pass  # 다른 시리즈 캐릭터 입력 필요

def isCorrectCharacter():
    while True:
        inputCharacter = input("캐릭터 선택(예: 간류를 원한다면 1 입력): ")
        
        if inputCharacter in TEKKEN_CHARACTER[seriesChoice]:
            characterFilePath = os.path.join(PATH, seriesChoice, TEKKEN_CHARACTER[seriesChoice][inputCharacter]+".txt")
            makeCharacterFile(characterFilePath)
            return inputCharacter
        else:
            print("올바른 캐릭터의 번호를 입력바람")

def makeCharacterFile(characterFilePath):
    if os.path.isfile(characterFilePath): 
        pass
    else:
        with open(characterFilePath, "a+") as file:
            file.write(TEXT)

def ReadWriteCommand(characterFilePath):
    print(characterFilePath)
    with open(characterFilePath, "r+") as file:
        print(file.write())
stage = 0
seriesChoice = 0
characterNameChoice = ""
characterFileName = ""
characterFilePath = ""
while True:
    if stage == 0:  # 시리즈 확인
        seriesChoice = isCorrectSeries()
        stage += 1
    elif stage == 1: # 해당 시리즈의 캐릭터 리스트 출력
        printCharacterList(seriesChoice)
        stage += 1
    elif stage == 2: # 캐릭터 선택
        characterNumChoice = isCorrectCharacter()
        stage += 1
    elif stage == 3: # 커맨드 리스트 확인 및 편집
        ReadWriteCommand(characterFilePath)