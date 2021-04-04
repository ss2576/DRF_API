# Тестирование API
import requests


city_dict = {'Moscow': 1, 'Tokio': 2, 'Paris': 3, 'Habana': 4, 'Penza': 5, 'Canberra': 6}

url_1 = 'http://127.0.0.1:8000/api/city_all'
request_1 = requests.get(url_1)
print('все города :', request_1.text)
print('*' * 200)

for key in city_dict:
    request_2 = requests.get(f'http://127.0.0.1:8000/api/city/{key}')
    print(f'город {key} :', request_2.text)
print('*' * 200)

for key in city_dict:
    request_3 = requests.get(f'http://127.0.0.1:8000/api/city/{city_dict[key]}')
    print(f'город {key} :', request_3.text)
print('*' * 200)
