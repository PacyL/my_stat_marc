import requests
import json
from config import tocen


def get_auth(ogin,pas):
    url = "https://mapi.itstep.org/v1/mystat/auth/login"
        
    headers={
            'accept' : 'application/json, text/plain, */*',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            'x-language':'ru'
        }
    data={
            "login":ogin,
            'password':pas
        }
    response=requests.post(url,headers=headers,data=data)
    with open("tocen.txt",'w') as f:
        f.write(response.text)
            
def get_mark():
    url = 'https://mapi.itstep.org/v1/mystat/aqtobe/statistic/marks'

    headers={'authorization':f"Bearer {tocen}"}
    response=requests.get(url,headers=headers)
    print(response.status_code)
    return response.json()
     
def get_rsp(week):
    if week == True:
        url = 'https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?type=week'
        headers={'authorization':f"Bearer {tocen}"}
        response=requests.get(url,headers=headers)
        print("учебные неделя")
        return response.json()
    else:
        url="https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?"
        headers={'authorization':f"Bearer {tocen}"}
        response=requests.get(url,headers=headers)
        print('учебный месяц')
        return response.json()