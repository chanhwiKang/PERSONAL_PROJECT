import psutil
import subprocess 
import time

def Search_and_distroy(game_name):
    global magnet_pid
    is_game_running = False
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'Magnet':
            magnet_pid = process.info['pid']
        if process.info['name'] == game_name:
            is_game_running = True

    return is_game_running

def close_magnet():
    try:
        psutil.Process(magnet_pid).terminate()
        print("Magnet을 종료하였습니다.")
    except:
        print("Magnet이 실행중이 아닙니다.")

def execution_magnet():
    if magnet_pid == 0:
        try:
            subprocess.run(["open", "-a", "Magnet"])
            print("Magnet을 실행하였습니다.")
        except:
            print("Magnet실행 중 에러 발생.")
    else:
        print("Magnet 작동중.")

magnet_pid = 0
game_name = "Darkest"
while True:

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    
    if Search_and_distroy(game_name):
        print(game_name,"이 실행중입니다.")
        close_magnet()
    else :
        print(game_name,"이 실행중이 아닙니다.")
        execution_magnet()
    print('-'*30)
    magnet_pid = 0
    
    time.sleep(60)