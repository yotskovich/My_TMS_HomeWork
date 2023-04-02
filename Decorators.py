#!/usr/bin/env python
# coding: utf-8

# In[71]:


"""
1.Напишите декоратор, который измеряет время выполнения функции и выводит его на экран.
Время должно быть выражено в миллисекундах.
"""
import time


def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        ms_result = (end - start) * 1000
        print(f'The result time our function = {ms_result:.5f}ms')
        return result
    return wrapper


@decorator
def number(*elements):
    new_list = [i for i in elements if i % 2 == 0]
    return new_list

input_list = [4, 6, 2, 3, 3, 44, 4, 5, 2, 4, 6, 2, 5, 65, 4, 6, 2, 4]
print(number(*input_list))


# In[21]:


"""2.Напишите декоратор, который проверяет, что функция возвращает корректные значения. 
Для этого декоратор должен принимать на вход ожидаемое значение и, если результат 
выполнения функции не соответствует ожидаемому, выводить сообщение об ошибке."""

def decorator(age):
    def check_func(func):

        def wrapper(*a, **kw):
            result = func(*a, **kw)
            if result >= age:
                print("You are welcome, enjoy watching!")
            else:
                
                print(f"Unfortunately, you have been denied a review.\nYou should be {age}.")
            return result
        return wrapper
    return check_func

@decorator(16)
def check_old():
    
    result_input = int(input('How old are you? '))
    return result_input

check_old()


# In[24]:


"""3.Напишите декоратор, который повторяет выполнение функции заданное
количество раз и выводит на экран время выполнения каждой итерации.
Повторы должны выполняться с небольшой задержкой между ними.
"""
import time


def counter_decorator(num):
    def counter_func(func):
        def wrapper(*a, **k):
            for el in range(1, num + 1):
                start_time = time.time()
                result = func(*a, **k)
                end_time = time.time()
                difference_time = end_time - start_time
                print(f'{el} function {func.__name__}() worked {difference_time}sec.')
                time.sleep(2)

            return result

        return wrapper

    return counter_func


@counter_decorator(5)

def check_number():
    enter_int = int(input("Enter your number "))
    print(enter_int ** 2)


check_number()


# In[ ]:


"""4.Напишите декоратор, который добавляет в функцию возможность кэширования
ее результатов. При повторном вызове функции с теми же аргументами результат
должен браться из кэша, а не вычисляться заново."""

cash_dict = {('4', '3', '-'): 1,
             ('30', '3', '*'): 90}


def cash_decorator(func):
    def wrapper(*args, **kwargs):


        result = func()
        if result[0] in cash_dict:
            print(f"The result of this example is already in cash {cash_dict[result[0]]}")
        else:
            cash_dict[result[0]] = result[1]
            print(f"Ooh, new operation {result[0]}, writing down the result -> {result[1]} ")
        return cash_dict
    return wrapper


@cash_decorator
def your_number():
    our_operation = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "**": lambda x, y: x ** y,
    }

    number_1 = input("Enter your number ")
    number_2 = input("Enter your number ")
    your_operation = input("Enter your operation + - * / ** ")
    result = our_operation.get(your_operation)(int(number_1), int(number_2))
    key_result = (number_1, number_2, your_operation)

    return (number_1, number_2, your_operation), result


your_number()
your_number()
your_number()

print(cash_dict)


# In[13]:


"""5.Напишите декоратор, который преобразует возвращаемое значение функции в строку и
выводит его на экран вместе с названием функции и аргументами вызова.
"""

def decorator(func):
    def wrapper(*a, **kw):
        
        result = func(*a, **kw)
        
        print(f"The result function {func.__name__}(), name = {str(result)}")
        
        return result
    return wrapper

@decorator
def enter_your_name():
    
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    
    return f'{name} {surname}'

enter_your_name()


# In[48]:


"""6.Напишите декоратор, который заменяет аргументы функции на значения из словаря.
Словарь должен передаваться в декоратор в качестве аргумента."""


def first_decoration(user):
    def second_decoration(func):
        def wrapper(*a, **kw):
            result = func(*a, **kw)
            print(result)
            if user['e-mail'] == result:
                  print("Your have account our website."
                        "\nEnter your password.")
            else:
                 print("You haven't registered on our website, please create a new account")

            return result
        return wrapper
    return second_decoration

user = {
    'name': 'Elena',
    'surname': 'Golovach',
    'e-mail': 'Elena-Golovach-Golovach@gmail.com',
    'id': '213467543',
    'date of regestration': '2022-08-14'
}



@first_decoration(user)
def check_of_registration():

    enter_mail = input("Hello, please enter your e-mail ")
    return enter_mail

check_of_registration()


# In[25]:


"""7.Напишите декоратор, который позволяет отменить выполнение функции с 
определенным аргументом. Декоратор должен принимать на вход список аргументов,
для которых выполнение функции должно быть отменено."""

def decorator(func):
    
    def wrapper(*a, **kw):
        
        text = "Cheat function"
        
        return text
    return wrapper

@decorator
def our_function(text):
    
    return text

our_function("Hello world")


# In[27]:





# In[ ]:




