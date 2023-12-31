# Методы машинного обучения

## Лабораторная работа 1. Метод линейной регрессии

### Введение

#### Цель работы

Реализация метода линейной регрессии

#### Задачи работы

- Получение и визуализация статистики по датасету
- Проведение предварительной обработки данных
- Разделение данных на обучающую и тестовую выборки
- Реализация метода линейной регрессии с использованием метода МНК без использования сторонних библиотек (кроме NumPy и Pandas)
- Построение 3-х моделей с различными наборами признаков
- Проведение оценки производительности (коэффициент детерминации)
- Выводы о наилучшей совокупности признаков
- Бонусное задание: введение синтетического признака

### Описание метода

Метод линейной регрессии - это статистический метод, используемый для анализа связи между зависимой переменной и одной или несколькими независимыми переменными. Его основное назначение заключается в предсказании значений зависимой переменной на основе значений независимых переменных.

Принцип работы метода линейной регрессии заключается в поиске линейной зависимости между переменными. Для этого строится уравнение линейной регрессии, которое представляет собой прямую линию, наилучшим образом соответствующую распределению точек на графике. Далее, используя это уравнение, можно предсказать значения зависимой переменной для новых значений независимых переменных.

### Псевдокод метода

Ниже представлен код обучения модели на тренировочных данных

```python
n = len(X_train_matrix)
width = len(X_train_matrix[0])
A = []
B = []

# B:
B.append(sum(Y_train_matrix))
for i in range(width):
  B.append(sum(Y_train_matrix * X_train_matrix[:, i]))

# A:

A.append([])
tmp = A[0]
tmp.append(n)
for i in range(width):
  tmp.append(sum(X_train_matrix[:, i]))

for i in range(width):
  A.append([])
  tmp = A[i+1]
  tmp.append(sum(X_train_matrix[:, i]))
  for j in range(width):
    tmp.append(sum(X_train_matrix[:, i] * X_train_matrix[:, j]))

solution = np.linalg.solve(A, B)
```

### Результаты выполнения

В качестве результата работы метода получаем вектор коэффициентов, который в дальнейшем используем для предсказания на тестовых данных:

```python
scalar_method_prediction = np.dot(X_test_matrix, solution)
```

### Примеры использования метода

- Экономика: анализ зависимости между уровнем дохода, районом проживания, ... и *расходами на потребительские товары*
- Социология: анализ влияния образования, семейного положения, ... и *дохода на уровень счастья людей*
- Биология: анализ зависимости между количеством употребляемых калорий, подвижностью, ... и *изменением веса организма*
- и проч.

## Лабораторная работа 2. Метод k-ближайших соседей (k-NN)

### Введение

#### Цель работы

Реализация метода k-ближайших соседей

#### Задачи работы

- Проведение предварительной обработки данных
- Реализация метода k-ближайших соседей без использования сторонних библиотек (кроме NumPy и Pandas)
- Построение двух моделей k-NN с различными наборами признаков
    - Модель 1: Признаки отбираются случайно.
    - Модель 2: Фиксированный набор признаков, который выбирается заранее.
- Оценка моделей при разных значениях k, построение матрицы ошибок.

### Описание метода

Метод k-ближайших соседей (k-nearest neighbors) - это метод машинного обучения, который используется для классификации и регрессии. Его основное назначение - предсказание значения целевой переменной на основе значений ближайших к ней соседей в пространстве признаков.

Принцип работы метода заключается в том, что для нового объекта предсказывается значение целевой переменной на основе значений этой переменной у k ближайших к нему соседей. Для классификации выбирается наиболее часто встречающийся класс среди соседей, а для регрессии - вычисляется среднее или медианное значение целевой переменной среди соседей.

### Псевдокод метода

#### Расчет Евклидова расстояния между объектами

```python
def euclidean_distance(X_1, X_2):
  distance = 0
  for i in range (len(X_1)):
    distance += (X_1[i] - X_2[i]) ** 2
  return math.sqrt(distance)
```

#### Поиск k ближайших соседей

```python
def get_neighbors(X_train, Y_train, X_test_values, k):
  X_train_values = X_train.values
  Y_train_values = Y_train.values
  distances = []
  for i in range (len(X_train_values)):
    distances.append((Y_train_values[i], euclidean_distance(X_train_values[i], X_test_values)))

  distances.sort(key=lambda elem: elem[1])

  neighbors = []
  for i in range(k):
    neighbors.append(distances[i][0])

  return neighbors
```

### Результаты выполнения

В результате работы обучения мы получаем модель, предсказывающую класс объекта на основе его признаков.

#### Предсказание класса

```python
def predict_class(neighbors):
  counter = {}

  for neighbor in neighbors:
    if neighbor in counter:
        counter[neighbor] += 1
    else:
        counter[neighbor] = 1

  max_count = max(counter.values())
  return [key for key, value in counter.items() if value == max_count][0]
```

### Примеры использования метода

- В экономике: анализ кредитного скоринга (можно ли доверить выдачу кредита заемщику)
- В медицине: диагностика болезней на основе симптомов и проч.
- Обработка естественного языка: спам для почты, отзывы для товаров (на основе слов определяем положительный или отрицательный)
- и прочие задачи классификации


## Лабораторная работа 3. Деревья решений

### Введение

#### Цель работы

Реализация древа принятия решений

#### Задачи работы

- Отбор случайным образром sqrt(n) признаков
- Реализация древа принятия решений без использования сторонних библиотек (кроме NumPy и Pandas)
- Провести оценку реализованного алгоритма с использованием accuracy, precision и recall
- Построить AUC-ROC и AUC-PR

### Описание метода

Метод дерева принятия решений является одним из методов машинного обучения, который используется для прогнозирования или классификации данных. Его назначение заключается в том, чтобы создать модель, которая может предсказывать целевую переменную на основе входных признаков.

Принцип работы метода дерева принятия решений заключается в построении дерева, где каждый узел представляет собой признак, каждое ребро - возможное значение этого признака, а каждый лист - прогноз или классификация. Для построения дерева используется алгоритм, который выбирает оптимальные признаки и значения для разделения данных на более чистые подгруппы.

### Псевдокод метода

#### Класс дерева решений

```python
class TreeNode:

    def __init__(self, left = None, right = None, class_name = None, feature = None, div_value = None):
        self.left = left
        self.right = right
        self.class_name = class_name
        self.feature = feature
        self.div_value = div_value

    def __str__(self):
        return f'(left = {self.left}; right  = {self.right}; class_name = {self.class_name}; feature = {self.feature}; div_value = {self.div_value})'
```

#### Вычисление энтропии для определения чистоты подмножества

```python
def calculate_entropy(Y_values):
    if len(Y_values) == 0:
        return 0

    p1 = np.mean(Y_values == Y_values[0])
    p2 = 1 - p1

    if (p1  == 1 or p2 == 1):
        return 0

    return -(p1 * math.log2(p1) + p2 * math.log2(p2))
```

#### Вычисление информационного выигрыша при разбиении по данному признаку X

```python
def calculate_gain(X, Y):
    #  энтропия до разделения
    before = calculate_entropy(Y.values)

    #  находим уникальные значения признака и количество вхождений каждого уникального признака
    values, occurrences = np.unique(X, return_counts=True)
    total = len(Y.values)

    #  массив энтропий для того, чтобы получить взвешанную энтропию (ВЭ потом будет использоваться для определения выгоды от разделения по данному признаку)
    entropies = []
    #  пробегаюсь по всем уникальным значениям признака
    for i, value in enumerate(values):

        #  вычисляю вероятность (количество объектов с таким признаком / общее количество объектов)
        prob = occurrences[i] / total

        #  все метки данного значения X
        cur_labels = Y[X == value]

        #  выщитываю энтропию меток полученных значений меток для данного уникального значения
        tmp_entropy = prob * calculate_entropy(cur_labels.values)

        #  добавляю в массив энтропий
        entropies.append(tmp_entropy)

    return before - sum(entropies)
```

#### Построение модели

```python
def build_nodes(X, Y, cur_depth, max_depth):
    Y_values = Y.values

    #  если все метки одинаковые, то энтропия == 0, значит нашли лист
    if len(np.unique(Y_values)) == 1:
        return TreeNode(class_name = Y_values[0])

    #  если текущая длина превысила предельную, то опеределяем класс по принципу большинства
    if (cur_depth >= max_depth):
        labels = np.unique(Y_values)
        label = Y_values[0]
        l1_count = 0
        for i in range(len(Y_values)):
            if Y_values[i] == label:
                l1_count += 1
        l2_count = len(Y_values) - l1_count
        return TreeNode(class_name = labels[0] if l1_count >= l2_count else labels[1])

    max_gain = 0
    final_feature_ind = None
    final_div_value = None

    # print(X)
    #  для каждого признака признакам
    for cur_column_ind in range(X.shape[1]):
        #  рассматриваем возможность разделения по каждому уникальному значению
        for div_value in np.unique(X.iloc[:, cur_column_ind]):
            #  делим
            left = X.iloc[:, cur_column_ind] < div_value
            right = X.iloc[:, cur_column_ind] >= div_value

            #  если нет смысла в разделении, пропускаем значение признака
            if (sum(left) == 0 or sum(right) == 0):
                continue

            #  высчитываем выигрыш
            cur_gain = calculate_gain(left, Y)
            #  запоминаем
            if cur_gain > max_gain:
                max_gain = cur_gain
                final_feature_ind = cur_column_ind
                final_div_value = div_value

    #  если выигрыша не обнаружено, поступаем как в случае с превышением глубины (большинство)
    if (max_gain == 0 or final_feature_ind is None or final_div_value is None):
        labels = np.unique(Y_values)
        label = Y_values[0]
        l1_count = 0
        for i in range(len(Y_values)):
            if Y_values[i] == label:
                l1_count += 1
        l2_count = len(Y_values) - l1_count
        return TreeNode(class_name = labels[0] if l1_count >= l2_count else labels[1])

    #  определяем индексы разделений
    left_X_ind = X.iloc[:, final_feature_ind] < final_div_value
    rigth_X_ind = X.iloc[:, final_feature_ind] >= final_div_value

    #  строим левое и правое деревья
    left_tree_node = build_nodes(X[left_X_ind], Y[left_X_ind], cur_depth + 1, max_depth)
    right_tree_node = build_nodes(X[rigth_X_ind], Y[rigth_X_ind], cur_depth + 1, max_depth)

    return TreeNode(left = left_tree_node,
                    right = right_tree_node,
                    feature = final_feature_ind,
                    div_value = final_div_value)
```

### Результаты выполнения

В качестве результата выполнения получаем модель (root ноду), благодаря которой классифицируем тестовые объекты:

```python
def predict(X_object_values, root):
    if root.class_name is not None:
        return root.class_name

    if (X_object_values[root.feature] < root.div_value):
        return predict(X_object_values, root.left)
    else:
        return predict(X_object_values, root.right)
```

### Примеры использования метода

- Экономика: прогнозирование тенденций рынка, принятие инвестиционных решений, анализ кредитного скоринга и проч.
- Медицина: диагностика заболеваний, выбор оптимального лечения, прогнозирование результатов лечения и проч.
- Маркетинг: сегментация потребителей, прогнозирование спроса на товары и проч.

## Лабораторная работа 4. Логистическая регрессия

### Введение

#### Цель работы

Реализация метода логистической регрессии

#### Задачи работы

- Выполнить предварительную обработку данных
- Разделить данные на обучающий и тестовый наборы в выборанном соотношении
- Реализация метода линейной регрессии без использования сторонних библиотек (кроме NumPy и Pandas)
    - Функция для вычисления гипотезы (sigmoid function)
    - Функция для вычисления функции потерь (log loss)
    - Метод обучения, который включает в себя градиентный спуск
    - Возможность варьировать гиперпараметры, такие как коэффициент обучения (learning rate) и количество итераций
- Исследовать гиперпараметры (варьировать)
    - Коэффициент обучения (learning rate)
    - Количество итераций обучения
    - Метод оптимизации (например, градиентный спуск или оптимизация Ньютона)
- Оценка модели
    - Для каждой комбинации гиперпараметров оценить производительность модели на тестовом наборе данных, используя метрики, такие как accuracy, precision, recall и f1-score
- Сделать выводы о наилучшей комбинации гиперпараметров

### Описание метода

Логистическая регрессия - это статистический метод, используемый для прогнозирования вероятности возникновения определенного события на основе одного или нескольких предикторов. Основное назначение логистической регрессии - моделирование зависимости между категориальной зависимой переменной и одной или несколькими независимыми переменными.

Принцип работы логистической регрессии заключается в том, что она использует логистическую функцию для преобразования взвешенной суммы предикторов в вероятность возникновения события. Затем эта вероятность может быть использована для классификации наблюдений на основе установленного порога. Логистическая регрессия также может использоваться для оценки влияния каждого предиктора на вероятность возникновения события.

### Псевдокод метода

#### Сигмоидная функция

```python
def sig(t):
    return 1 / (1 + np.exp(-t))
```
#### Функция потерь

```python
def cost(Y_actual, Y_predicted):
    return -np.mean(Y_actual * np.log(Y_predicted) + (1 - Y_actual) * np.log(1 - Y_predicted))
```

#### Метод градиентного спуска

```python
def gradient_descent(X_train, Y_train, iterations, learning_rate):
    objects_num, characteristics_num = X_train.shape

    weights = np.zeros(characteristics_num)
    losses = []
    bias = 0

    for iteration in range(1, iterations + 1):

        t = np.dot(X_train, weights) + bias
        #  prediction
        z = sig(t)

        #  ЧП стоимости по весам
        dw = (1 / objects_num) * np.dot(X_train.T, (z - Y_train))
        #  ЧП стоимости по смещению
        db = (1 / objects_num) * np.sum(z - Y_train)

        weights -= learning_rate * dw
        bias -= learning_rate * db

        if iteration % 100 == 0:
            loss = cost(Y_train, z)
            losses.append(loss)
            # print(f'{iteration}) cost = {loss}')

    coeff = {'weights': weights, 'bias': bias}
    return coeff, losses
```

#### Оптимизация Ньютона

```python
def newton_optimization(X_train, Y_train, iterations):
    objects_num, characteristics_num = X_train.shape

    weights = np.zeros(characteristics_num)
    losses = []
    bias = 0

    for iteration in range(1, iterations + 1):

        t = np.dot(X_train, weights) + bias
        #  prediction
        z = sig(t)

        #  ЧП стоимости по весам
        dw = (1 / objects_num) * np.dot(X_train.T, (z - Y_train))
        #  ЧП стоимости по смещению
        db = (1 / objects_num) * np.sum(z - Y_train)

        hessian = (1 / objects_num) * (X_train.T @ ((z * (1 - z)) * X_train.T).T)

        weights -= np.linalg.inv(hessian) @ dw
        bias -= db

        if iteration % 100 == 0:
            loss = cost(Y_train, z)
            losses.append(loss)
            # print(f'{iteration}) cost = {loss}')

    coeff = {'weights': weights, 'bias': bias}
    return coeff, losses
```

### Результаты выполнения

В качестве результата выполнения получаем модель, которая, подобно линейной регрессии, с помощью коэффициентов получает предсказания (но уже в качестве вероятности). Отсается дело за малым -- определить пороговое значение для отнесения объекта к тому или иному классу:

```python
def predict(X_test, coeff):
    weights = coeff['weights']
    bias = coeff['bias']

    t = np.dot(X_test, weights) + bias

    z = sig(t)

    return (z > 0.6).astype(int)
```

### Примеры использования метода

- Экономика: прогнозирование вероятности дефолта кредитного заемщика на основе его финансовых показателей, таких как доход, задолженность и проч.
- Медицина: анализ факторов, влияющих на вероятность заболевания определенной болезнью
- Маркетинг: прогнозирование вероятности покупки продукта или услуги на основе демографических и поведенческих данных потребителей
- Социология: вероятность голосования за определенного кандидата на выборах

## Сравнение методов

### Сравнительный анализ методов

#### Приемущества

- Линейная регрессия
    - Легко интерпретируется, что позволяет понять влияние каждого признака на целевую переменную
    - Эффективна на больших выборках данных
- k-NN
    - Не делает предположений о распределении данных, что делает его универсальным
    - Простота в реализации
- Древо решений
    - Может обрабатывать нелинейные отношения между признаками и целевой переменной
    - Устойчиво к выбросам в данных
- Логистическая регрессия
    - Позволяет интерпретировать влияние каждого признака на вероятность принадлежности к определенному классу
    - Эффективна при большом количестве признаков, особенно если они линейно независимы

#### Ограничения

- Линейная регрессия
    - Линейная зависимость меджу данными
    - Отсутствие большого количества выбросов
    - Отсутствие мультиколлинеарности (в модели отсутствуют коррелирующие между собой переменные)
- k-NN
    - Большая, разнообразная выборка для эффективной работы
    - Чувствителен к выбору признаков
    - Выская вычислительная сложность: O(n^2)
    - Проклятие размерности (чем больше признаков, тем менее различимы классы)
    - Выбор значения k может существенно влиять на результаты классификации
- Древо решений
    - Неустойчивость к изменениям данных (если тренировочные данные немного изменятся, придется заново перестраивать модель)
    - Имееет проблемы с классификацией в случае, если классы плохо разделимы или имеют сложную структуру
    - Склонность к созданию смещенных моделей при преобладании одного из классов
    - Склонность к переобучению (дерево слишком сильно подстраивается под обучающую выборку и плохо работает на тестовой)
- Логистическая регрессия
    - Требование линейной зависимости между предикторами и логарифмом отношения вероятностей (в противном случае модель может давать неправильные прогнозы)
    - Отсутствие сложных взаимодействий между предикторами
    - Отсутствие мультиколлинеарности между предикторами
    - Отсутствие выбросов

### Примеры лучшего использования каждого метода

- Линейная регрессия
    - Прогнозирование цен на недвижимость на основе различных параметров, таких как площадь, количество спален и расстояние до центра города
    - Оценка влияния факторов, таких как уровень дохода и образования, на результаты студентов на экзаменах
- k-NN
    - Классификация электронных писем в "спам" или "не спам" на основе характеристик письма, таких как наличие определенных слов или фраз
    - Рекомендация фильмов или товаров на основе предпочтений пользователя и данных о ранее просмотренных или купленных элементах
- Древо решений
    - Прогнозирование вероятности успешной продажи продукта на основе характеристик клиента, таких как возраст, доход и местоположение
    - Оценка риска заболевания определенным заболеванием на основе медицинских анализов пациента, таких как уровень холестерина и артериальное давление
- Логистическая регрессия:
    - Прогнозирование вероятности оттока клиентов на основе их исторических данных о покупках и обращениях в службу поддержки
    - Классификация пациентов на "больных" и "здоровых" на основе результатов медицинских тестов и симптомов

## Заключение

Таким образом, выбор метода машинного обучения зависит от конкретной задачи, структуры данных, распределения данных и количества признаков. Каждый метод имеет свои сильные стороны и может быть эффективным в определенных ситуациях.

## Приложения

Google collab'ы по лабам:

1. [Лабораторная №1 (Линейная регрессия)](https://colab.research.google.com/drive/1q-YBjzaADmJp-w60URF6toUQLcWCSSmK?usp=sharing)
1. [Лабораторная №2 (Метод k-ближайших соседей)](https://colab.research.google.com/drive/1jXSCmuo7r0c5Hr2KRCQ3GVlvVvOvoZPJ?usp=sharing)
1. [Лабораторная №3 (Деревья решений)](https://colab.research.google.com/drive/1ZgDt7-MIv5qg3vyd5BuCuXkNQ3nZkaLH?usp=sharing)
1. [Лабораторная №4 (Логистическая регрессия)](https://colab.research.google.com/drive/1ubDFoAJ4ShbfrUqFBE9V30oNfVUzrK1i?usp=sharing)

Либо на github:

1. [Лабораторная №1 (Линейная регрессия)](https://github.com/IndianMax03/ais-labs/blob/6b29fd5744a91009fbe473b1f56972121f897687/module2/lab4/src/ais_lab_4.ipynb)
1. [Лабораторная №2 (Метод k-ближайших соседей)](https://github.com/IndianMax03/ais-labs/blob/084084178e9d5afcbd3571a54b4e761b66fe9e1b/module2/lab5/src/ais_lab_5.ipynb)
1. [Лабораторная №3 (Деревья решений)](https://github.com/IndianMax03/ais-labs/blob/86930df78639dc4767ca1165a62f39be2afcc3f7/module2/lab6/src/ais_lab_6.ipynb)
1. [Лабораторная №4 (Логистическая регрессия)](https://github.com/IndianMax03/ais-labs/blob/ad73d3333846a098eca3631dba54f03f3266278c/module2/lab7/src/ais_lab_7.ipynb)
