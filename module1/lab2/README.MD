# Лабораторная работа 2. Создание онтологии в Protege

Целью этой лабораторной работы является знакомство со средой разработки онтологий Protege и перевод базы знаний, созданной в предыдущей лабораторной работе в онтологическую форму в Protege.

## Задание

Преобразовать факты и отношения из Prolog в концепты и свойства в онтологии. Описать классы и свойства в онтологии, которые соответствуют объектам и отношениям из базы знаний. Например, если у были классы "Человек" и "Машина" и свойство "возраст", создайте аналогичные классы и свойства в онтологии в Protege.

## Критерии оценки

- Корректное создание онтологии в Protege на основе базы знаний в Prolog.
- Качество перевода фактов, предикатов и отношений из Prolog в онтологию.
- Определение классов, свойств и иерархии классов в Protege.
- Тестирование онтологии и демонстрация ее функциональности.

## Реализация

### Отобразим факты базы знаний на предикаты онтологии (ObjectProperties/DataProperties):

|                       Предикат                       |
|:----------------------------------------------------:|
| <img alt="predicate1.png" src="img/predicate1.png"/> |            
| <img alt="predicate2.png" src="img/predicate2.png"/> |
| <img alt="predicate3.png" src="img/predicate3.png"/> |
| <img alt="predicate4.png" src="img/predicate4.png"/> |
| <img alt="predicate5.png" src="img/predicate5.png"/> |
| <img alt="predicate6.png" src="img/predicate6.png"/> |
| <img alt="predicate7.png" src="img/predicate7.png"/> |

### На основании предикатов определим Individuals:

|               Individuals                |
|:----------------------------------------:|
| <img alt="ind1.png" src="img/ind1.png"/> |  
| <img alt="ind2.png" src="img/ind2.png"/> |
|                   ...                    |

### В связи с особенностями строения онтологии, определим правила базы знаний как классы, используя определенные ранее предикаты. Помимо этого, для отображения рекурсии предков, определим причастие (ярлык) также через класс:

|                    Класс                     |
|:--------------------------------------------:|
| <img alt="class1.png" src="img/class1.png"/> |
| <img alt="class2.png" src="img/class2.png"/> |
| <img alt="class3.png" src="img/class3.png"/> |
| <img alt="class4.png" src="img/class4.png"/> |
| <img alt="class5.png" src="img/class5.png"/> |
| <img alt="class6.png" src="img/class6.png"/> |
| <img alt="class7.png" src="img/class7.png"/> |
| <img alt="class8.png" src="img/class8.png"/> |
| <img alt="class9.png" src="img/class9.png"/> |

### Запустим Reasoner и выполним запросы:

|                 Запрос                 |            Комментарий             |
|:--------------------------------------:|:----------------------------------:|
| <img alt="ex1.png" src="img/ex1.png"/> |             Все матери             |
| <img alt="ex2.png" src="img/ex2.png"/> | Все матери, являющиеся Ассассинами |
| <img alt="ex3.png" src="img/ex3.png"/> | Пират, Маг и Ассассин одновременно |
| <img alt="ex4.png" src="img/ex4.png"/> |     Является ли Maud женщиной      |
| <img alt="ex5.png" src="img/ex5.png"/> |  Является ли William_Miles мамой   |

## Для подготовки повторить:
1) [syntax](http://protegeproject.github.io/protege/class-expression-syntax/)
2) [manual](https://docs.google.com/document/d/1kKOom1gBV5uvji62Z0fhQpbhclNBNAPZIPZmjk-n-zU/edit)
3) [videos](https://www.youtube.com/playlist?list=PLMDuaURn3ViYuD2HLtf0u4WTTGRFS-dIN)

## Вывод

В результате работы я создал онтологию в Protege на основе базы знаний в Prolog путём отображения фактов, предикатов и отношений из Prolog в онтологию. Также я выполнил запросы в онтологию для обнаружения скрытых фактов.
