"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    dict = {'Как дела?' : 'Хорошо!' , 'Что делаешь?' : 'Программирую' , 
        'Получается?' : 'Вроде да' , 'Нравится?' : 'Огонь!'
    }

    def ask_user_dict():
        try:
            while True:
                user_ask = input('Введите вопрос: ')
                if bool(dict.get(f'{user_ask}')) == True: 
                    return dict.get(f'{user_ask}') 
                    break
        except KeyboardInterrupt:
            return f'Пока!'
    print(ask_user_dict())
    
if __name__ == "__main__":
    ask_user()
