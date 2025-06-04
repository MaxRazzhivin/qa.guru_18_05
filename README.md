# Заметки к занятию "Основы Python - часть 2"

## Conditions - условия: 

```bash
if users_list:
    pass
    
Краткая запись для условий типа "если такой-то список не пустой", т.е. != False

Любое число кроме 0 будет равно True 
Строки "" - если пустая, то это False, любой символ внутри - True 
Списки [] - если пустой, то это False, любое значение внутри - True

```

## Loops - циклы: 

'''bash
Пример циклов while и random: 

required_number = 7
user_number = random.randint(0, 10)

while required_number != user_number:
        user_number = random.randint(0, 10)
        print(f'Пользователь ввел число {user_number}')
'''

```bash
Либо циклы с заранее определенным счетчиком итераций: 

iterations_count = 10
i = 0

while i < iterations_count:
    print("Текущая итерация {i}")
    i += 1
    
Такие циклы могут использоваться на форме ввода пароля от пользователя. Например, 5 раз дает ввести пароль, дальше блок.
```

```bash
И цикл for - позволяет итерироваться по каким-либо коллекциям (спискам, словарям, строкам)

users = [
    {"name": 'Oleg', "age": 32},
    {"name": 'Sergey', "age": 24},
    {"name": 'Stanislav', "age": 15},
    {"name": 'Olga', "age": 45},
    {"name": 'Maria', "age": 18},
]  
    
    from pprint import pprint
    
    for user in users:
        pprint(f'Пользователю {user['name']} {user['age']} лет')
        
        
Аналогичный пример для словарей: 

    d = {
      'first': 1,
      'second': 2,
      'third' : 3
    }
    
    for item in d: // 'это равнозначно for item in d.keys():'
      pprint(item) // вернет ключи из словаря только, без значений 
      
    for item in d.values(): - вернет значения без ключей 
        pprint(item)
        
    for item in d.items(): - самое частое использование, позволит вывести и ключи и значения
        pprint(item) - вернет нам пары ключ + значение в виде кортежа ('first', 1), ('second', 2), ('third', 3)
        
    Поэтому удобнее для словарей сразу писать:
    
    for key, value in d.items():
        pprint(f'Ключ {key} значение {value}') 
 
```

```bash
Цикл с итератором for i in range

Аналог этому циклу:

iterations_count = 10
i = 0

while i < iterations_count:
    print("Текущая итерация {i}")
    i += 1
    
    
В версии с for i in range: 


iterations_count = 10

for i in range(iterations_count):
    print('Текущая итерация {i}')
    
range(10) - здесь диапазон от 0 до 9, который мы можем преобразовать для наглядности в list(range(10)) // получим [0,1,2,3,4,5,6,7,8,9]
В range внутри мы можем указать 3 значения - начальное, конечное и шаг между ними
```

## Break, Continue, Else - прерывание цикла 

```bash
for i in range(10):
    if i % 2 == 0:
        continue - пропустит эту часть, продолжит дальше 
        print("Никогда не выполнится")
    print(f"Точно нечетное число {i}")

    if i > 7:
        break - прерывает наш цикл и больше не продолжаем


Цикл в цикле:
  for i in range(5):
      for j in range(5):
        print(i , j)
        
        if j == 3:
          continue
          
        if j == 4:
          break
```


## Enumerate - используется для того, чтобы пронумеровать уже какой-то существующий список

```bash
cities = ['Екатеринбург', "Москва", "Сочи"]

i = 1
for city in cities:
    print(f"{city} на {i} месте по загрязнению воздуха")
    i += 1
    
    
Enumerate позволяет избавиться от счетчика для городов: 

for city in enumerate(cities):
    print(f"{city} на месте по загрязнению воздуха") 
    
Так мы получим кортежи вида: 
(0, "Екатеринбург")
(1. "Москва")
(2, "Сочи")


Можем переделать тогда в вид:

for i, city in enumerate(cities):
    print(f"{city} на {i+1} месте по загрязнению воздуха") 


```