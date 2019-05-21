from math import ceil, floor
import random

random.seed(228)

def get_unique_ids():
    # Уникальные ID пользователей
    graph = open("./data/train.txt", "r").read().split("\n")
    graph = [[int(i) for i in edge.split()] for edge in graph]
    ids = set()
    for edge in graph:
        ids.add(edge[0])
        ids.add(edge[1])
    return ids

def prepare_dataset():
    # Чтение графа из текстового файла
    raw_graph_file = open("./data/fb-wosn-friends.edges", "r")
    raw_graph = raw_graph_file.read()
    raw_graph = raw_graph.split("\n")[2:]

    # Удаление последних двух столбиков из таблицы
    graph = []
    for edge in raw_graph[:-1]:
        graph.append(" ".join(edge.split(" ")[:2]))

    # Преобразование в числа
    graph = [[int(number) for number in edge.split(" ")] for edge in set(graph)]
    
    # Разделение датасета на выборки
    random.shuffle(graph)
    L = len(graph)
    ntrain = ceil(L*0.9)
    ntest = int(L*0.1)

    train = graph[:ntrain]
    test = graph[-ntest:]

    # Запись обработаного датасета в файлы
    train_file = open("./data/train.txt", "w")
    test_file = open("./data/test.txt", "w")
    train_file.write(
        "\n".join([
            " ".join([str(elem) for elem in edge]) \
            for edge in train
        ])
    )

    train_file.write(
        "\n".join([
            " ".join([str(elem) for elem in edge]) \
            for edge in test
        ])
    )

    train_file.close()
    test_file.close()
    raw_graph_file.close()
    a = 2
   
a = 1
