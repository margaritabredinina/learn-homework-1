"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_scores  = [
                        {'school_class': '4a', 'scores': [3,4,4,5,2]}, 
                        {'school_class': '3b', 'scores': [4,5,4,3,2]},
                        {'school_class': '5c', 'scores': [5,4,5,5]},
                        {'school_class': '4b', 'scores': [4,4,4,3]}
    ]

    scores_sum_school = 0
    scores_no = 0
    for number in range(len(school_scores)):
        scores_sum_class = 0
        scores_no += len(school_scores[number]['scores'])
        for scores in school_scores[number]['scores']:
            scores_sum_school += scores
            scores_sum_class += scores
        scores_avg_class = scores_sum_class / len(school_scores[number]['scores'])
        print(f"Средняя оценка класса {school_scores[number]['school_class']}: {scores_avg_class}")
    scores_avg_school = scores_sum_school / scores_no
    print(f"Средняя оценка школы: {scores_avg_school}")
    
if __name__ == "__main__":
    main()
