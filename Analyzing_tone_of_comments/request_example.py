import requests


# Пример данных
data = input("Введите комментарий: ")
print(data)

# формируем запрос
def send_json(x):
    comment = x
    body = {'comment':comment
            }
    myurl = 'http://127.0.0.1:8080/' +'predict'
    headers = {'content-type': 'application/json; charset=utf-8'}
    response = requests.post(myurl, json=body, headers=headers)
    return response.json()['predictions']

# обращение к серверу с запросом из одного набора
if __name__ == '__main__':
    response = send_json(data)
    print(f'Вероятность токсичности: {round(response,2)*100}%')