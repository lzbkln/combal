def dfs(v, color, graph):
    for neighbour in graph[v]:
        if color[neighbour] == 0:  # Вершина не раскрашена
            color[neighbour] = 3 - color[v]  # Красим в противоположный цвет
            if not dfs(neighbour, color, graph):
                return False
        elif color[neighbour] == color[v]:  # Вершины одного цвета, граф не двудольный
            return False
    return True


def main():
    file = open("in.txt", "r")
    file2 = open("out.txt", "w")

    n = int(file.readline())
    graph = {}
    for i in range(1, n + 1):
        temp = list(map(int, file.readline().strip().split()))
        temp.remove(0)
        graph[i] = temp
    color = [0] * (n + 1)  # Массив цветов: 0 - не раскрашена, 1 - первый цвет, 2 - второй цвет
    for i in range(1, n + 1):
        if color[i] == 0:  # Найдена новая компонента связности
            color[i] = 1  # Красим в первый цвет
            if not dfs(i, color, graph):
                file2.write('N')
                return
    # Граф является двудольным, выводим ответ
    file2.write('Y'+'\n')
    part1 = [i for i in range(1, n + 1) if color[i] == 1]
    part2 = [i for i in range(1, n + 1) if color[i] == 2]
    file2.write(' '.join(map(str, part1)) + '\n')
    file2.write(' '.join(map(str, part2)))


if __name__ == '__main__':
    main()

