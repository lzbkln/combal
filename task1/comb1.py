from collections import deque


def bfs(graph):
    n = len(graph)
    visited = [False] * n
    prev = [-1] * n

    for start in range(n):
        if visited[start]:
            continue
        q = deque()
        q.append(start)
        while q:
            node = q.popleft()
            visited[node] = True
            for neighbor in range(n):
                if graph[node][neighbor]:
                    if prev[node] != neighbor:
                        if visited[neighbor]:
                            path = [neighbor]
                            cur = node
                            while cur != neighbor:
                                path.append(cur)
                                cur = prev[cur]
                            path.append(neighbor)
                            return path[::-1]
                        prev[neighbor] = node
                        q.append(neighbor)
    # цикла нет
    return None


def main():
    string = ""
    path = []
    file = open("in.txt", "r")
    file2 = open("out.txt", "w")
    a = int(file.readline())
    while True:
        arr = []
        for i in range(a):
            arr.append(list(map(int, file.readline().split())))
        arrOfPath = bfs(arr)
        if not arrOfPath:
            file2.write("A")
            break
        else:
            file2.write("N" + '\n')
            for i in arrOfPath:
                path.append(i + 1)
            path = path[0:len(path) - 1]
            path = sorted(path)
            for i in path:
                string = string + str(i) + " "
            file2.write(string)
            break


if __name__ == "__main__":
    main()
