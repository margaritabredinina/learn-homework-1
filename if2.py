"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    def string(one , two):
        if one != str(one) or two != str(two):
            return(0)
        elif one == two :
            return(1)
        elif one != two and two == 'learn':
            return(3)    
        elif one != two and len(one) > len(two):
            return(2)
        else:
            return(4)    
    
    print(string(0        , 'learn'))
    print(string('learn'  , 'learn'))
    print(string('python' , 'learn'))
    print(string('learn'  , 'math'))
    print(string('learn'  , 'geography'))
        
if __name__ == "__main__":
    main()
