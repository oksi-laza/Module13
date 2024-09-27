import asyncio


async def start_strongman(name, power):
    """
    :param name: имя силача (str)
    :param power: подъёмная мощность силача (int)
    """
    print(f'Силач {name} начал соревнования.')
    for number in range(1, 6):
        await asyncio.sleep(1 / power)    # задержка, обратно пропорциональная силе('power') силача
        print(f'Силач {name} поднял {number} шар.')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 4))
    task2 = asyncio.create_task(start_strongman('Denis', 6))
    task3 = asyncio.create_task(start_strongman('Apollon', 8))
    await task1    # ожидание результата выполнения задачи
    await task2
    await task3


asyncio.run(start_tournament())    # запуск асинхронной функции 'start_tournament'
