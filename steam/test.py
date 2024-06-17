import requests

# 발급받은 Steam API 키
steam_api_key = 'B41669D5D8FAAEB2B1CB5F5DAA7E1B28'

# API 엔드포인트
api_url = 'http://store.steampowered.com/api/salepage/'

# API 호출 및 응답 받기
response = requests.get(api_url)
data = response.json()

# 모든 앱의 정보 가져오기
apps = data

# 할인 중인 게임 목록 출력
for app in apps:
    # 여기에서 게임 정보를 원하는 방식으로 처리합니다.
    # 예를 들어, 할인 정보가 있는지 여부를 확인하거나, 특정 기준으로 필터링할 수 있습니다.
    # print(f"App ID: {app['appid']}, Name: {app['name']}")
    print(app)
    