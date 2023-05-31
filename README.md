# Комбинаторные алгоритмы II курс
# Задача 1. Определить, является ли данный граф ацикличным.

### Метод решения: Поиск в ширину.

### Формат ввода
Первая строка содержит единственное число N — количество вершин в графе. Далее построчно расположена матрица смежности размерности N x N.

### Формат вывода
Для ацикличного графа файл ответа должен содержать единственный символ: "A"(латинское). Если в графе есть цикл, то в первой строке "N", во второй упорядоченный по возрастанию номеров список вершин, входящих в первый найденный цикл. Нумерация вершин графа начинается с единицы.

# Задача 2. Определить, является ли данный связный неориентированный граф двудольным.

### Метод решения: Поиск в глубину.

### Формат ввода
Первая строка содержит единственное число N — количество вершин в графе. Далее последовательно расположены списки смежностей для каждой вершины. Каждый список заканчивается 0. Вершины нумеруются с единицы.

### Формат вывода
Если граф не двудольный, в единственную строку выходного файла запишите "N" (без кавычек). Если графе двудольный, то в первой строке "Y", в следующих двух строках доли графа. Вершины в долях должны быть упорядочены по возрастанию номеров. Первой печатается доля, в состав которой входит вершина с минимальным номером. Нумерация вершин графа начинается с единицы.

# Задача 3. Найти минимальный v-w путь в сети с неотрицательными весами.

### Метод решения: алгоритм Дейкстры.

### Формат ввода
Сеть, заданная списками СЛЕД[].

N - количество вершин. Далее последовательно расположены списки последующих для каждой вершины. В список заносится номер вершины и вес дуги. Список заканчивается 0 (не путать с нулевым весом). В конце файла записаны источник и цель.

### Формат вывода
В случае отсутствия пути в файл результатов необходимо записать "N". При наличии пути - "Y" и далее с новой строки весь путь. Путь начинается источником и заканчивается целью. Узлы отделяются друг от друга пробелами, вес пути вычисляется как сумма весов всех дуг, входящих в него, и записывается в третьей строке.
