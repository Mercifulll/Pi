import math
import random
import threading
import time

def MonteCarloSingle(points):
    insideCircle = 0 #лічильник точок всередині кола
    for i in range(points):
        x, y = random.random(), random.random() #діапазон точок [0; 1)
        if math.sqrt(x**2 + y**2) <= 1:
            insideCircle += 1
    return (insideCircle/points) * 4

def ThreadFunction(points, data, key):
    #nonlocal insideCircle #змінна з батьківської функції
    insideCircleThread = 0
    for i in range(points):
        x, y = random.random(), random.random()
        if math.sqrt(x**2 + y**2) <= 1:
            insideCircleThread += 1
    data[key] = insideCircleThread;


def MonteCarloMulti(pointsPerThread, numThreads):
    insideCircle = 0
    threadList = list()
    shared_data = {}

    for i in range(numThreads):
        thread = threading.Thread(target=ThreadFunction, args=(pointsPerThread, shared_data, i)) #target вказує на функцію, яка буде виконуватися в окремому потоці
        threadList.append(thread)
        thread.start()

    #для кожного потоку з ліста чекаємо поки завершиться
    for thread in threadList:
        thread.join()

    for i in range(numThreads):
        insideCircle = insideCircle + shared_data[i]

    return (insideCircle / (pointsPerThread * numThreads)) * 4

totalPoints = 10000000
startTime = time.time()
print(f'Значення π в одному потоці = {MonteCarloSingle(totalPoints)}')
endTime = time.time()
executionTime = endTime - startTime
print(f'Час виконання: {executionTime:.3f} сек')

numThreads = 8
pointsPerThread = totalPoints // numThreads  #кількість точок на кожен потік
startTime = time.time()
print(f"Значення π з використанням багатопотоковості ({numThreads} потоки) = {MonteCarloMulti(pointsPerThread, numThreads)}")
endTime = time.time()
executionTime = endTime - startTime
print(f'Час виконання: {executionTime:.3f} сек')