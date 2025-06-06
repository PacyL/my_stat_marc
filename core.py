import requests

from config import tocen,TimeOut # свалка переменных
import time

# исползвано в основном библиотека requests
def get_auth(login,pas):#post url,headers,data дата то что я отправляю на сервер.функ для сохронения токена для акк
    time.sleep(TimeOut)# библиоткека time для пауз между запросами
    url = "https://mapi.itstep.org/v1/mystat/auth/login" 
        
    headers={
            'accept' : 'application/json, text/plain, */*',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            'x-language':'ru'
        }
    data={
            "login":login,
            'password':pas
        }
    response=requests.post(url,headers=headers,data=data)
    with open("tocen.txt",'w') as f:
        f.write(response.text)
    if response.status_code==200:
        return True
    else:
        return False

            
def get_mark():#get url , headers для запросов оценок
    time.sleep(TimeOut)
    url = 'https://mapi.itstep.org/v1/mystat/aqtobe/statistic/marks'

    headers={'authorization':f"Bearer {tocen}"}
    response=requests.get(url,headers=headers)
    print(response.status_code)
    return response.json()
     
def get_rsp(week):#get для запросов учебных дней
    time.sleep(TimeOut)
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