# для удобного 
def print_mark(marks):
    ball=[]
    print("вашы оценки")
    if not marks or not isinstance(marks,list):
        print("нет данных")
        return
    for item in marks:
        date = item['mark_date']
        mark = item['mark']
        theme = item['theme']
        ball.append(int(mark))
        print(f"{date}\t|\tоценка: {mark}\t|\tтема: {theme}")
    print(f'средное значения оценок:{sum(ball) / len(ball)}')   
    
        
def print_rsp(rsp):
    date_1=rsp["start_day"]
    date_2=rsp['end_date']
    print(f"{date_1}\t|\t{date_2}")
        