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

## Функции functions - именованный блок кода, который мы можем вызвать

```bash
def my_func():
    print("Мы вызвали функцию")
    
my_func()
my_func()
my_func()
```

```bash
Функция с позиционными аргументами: 

def sum_numbers(a: int,b: int):
    print(a + b)
    
sum_numbers(5, 15)
sum_numbers(20, 30)
sum_numbers(14, 17)

Если мы хотим использовать дальше результат функции, то используем return: 

def sum_numbers(a: int,b: int):
    return a + b

И можем присвоить результат переменной для использования в дальнейшем:

n = sum_numbers(10, 5)
```

```bash
Функция с именованными аргументами: 

sum_numbers(b=5, a=15)
```


```bash
Функция с аргументами по-умолчаню, который в дальнейшем можно или не указывать вовсе или заменить значение

def multiply(n, mult: int = 2):
    print(n * mult)
    
multiply(10)
multiply(10, mult=5)

```

```bash
Возвращаем из функции несколько значений:

def return_tuple():
    return 1,2,3 
    
t = return_tuple()
print(t) // - вернет нам (1, 2, 3)

Либо мы можем сразу разложить по элементам:

t1, t2, t3 = return_tuple()
print(t1, t2, t3) // вернет нам 1 2 3


Если мы укажем t1, t2 = return_tuple(), это вызовет ошибку Value Error: too many values to unpack (expected 2)

Чтобы ее избежать, можно сделать с.о.:

t1, *t2 = return_tuple()
print(t1, t2) // вернет нам 1, [2, 3]. Он помещает в первое значение его так же, а все остальные списком распакуется во второе t2

либо 

t1, t2, *t3 = return_tuple()
print(t1, t2, t3) // вернет 1 2 [3]
```

```bash
Еще пример - если нам функция возвращает несколько переменных, а нам нужна только одна 

def return_tuple():
    return 1,2,3 
    
t1, _, _ = return_tuple()

Либо если много значений для игнора: 

t1, *_ = return_tuple()
```

## Args и Kwargs - переменное количество аргументов на примере print

```bash

*args - означает, что данная функция имеет переменное количество аргументов в ней. Мы можем передать сколько угодно аргументов и они все поместятся в одну переменную как tuple


def custom_print(*args):
    for arg in args:
        print(arg)
        
    print(args)
        
custom_print(1, 2, 3, 4, 5) - мы можем передать сколько угодно аргументов

def custom_print(*args):
    print(args) / так мы получим просто tuple из 5 элементов (1, 2, 3, 4, 5)
    print(*args) / так произойдет распаковка кортежа на отдельные элементы, т.е. 1 2 3 4 5

custom_print(1, 2, 3, 4, 5) 
```

```bash
Переменное количество именованных аргументов kwargs:

def custom_named_print(*args, **kwargs)
    print(args) // здесь будет также тапл из элементов
    print(kwargs) // а здесь словарик из элементов в виде {ключ: значение}
    
    print(*args, **kwargs) // так мы получим распакованные args и kwargs, 1 | 2 | 3 | 4 | 5!
    
custom_named_print(1, 2, 3, 4, 5, end = '!\n', sep = ' | ')

в kwargs будет {'end': '!\n', 'sep': ' | '}
```

## Область видимости - у функций она другая, чем у условий и циклов

```bash

v = 123

def my_awesome_func():
        v = 456
        print(v)

print(v) // получим 123
my_awesome_func() // получим 456
print(v) // получим 123

```

## Сортировка словаря с передачей функции в другую функцию


```bash
users = [
    {'name': 'Oleg', 'age': 32},
    {'name': 'Sergey', 'age': 24},
    {'name': 'Stanislav', 'age': 15},
    {'name': 'Olga', 'age': 45},
    {'name': 'Maria', 'age': 18}
]

def get_age(user):
    return user['age']

users.sort(key = get_age)

Либо можем отсортировать в обратную сторону: 
users.sort(key = get_age, reverse = True)

pprint(users)

```
```bash
Либо еще наша же функция аналог на безымянной lambda фукнции: 

users = [
    {'name': 'Oleg', 'age': 32},
    {'name': 'Sergey', 'age': 24},
    {'name': 'Stanislav', 'age': 15},
    {'name': 'Olga', 'age': 45},
    {'name': 'Maria', 'age': 18}
]

users.sort(key = lambda user: user['age'])

pprint(users) // получим такой же ответ, как у функции выше 



```