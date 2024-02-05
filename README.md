# MultiParser

# utils
проверка запущенного менеджера



# Security
1. maybe save and print proxy passport in hash



    # последовательный запуск, пока таска 1 не закончит выполнение 2 не начнёт
    for i in tasks:
        t = await parser.run_task(i)
        print(t)

    # пааралельный запуск сразу всех задач
    async_tasks = [parser.run_task(i) for i in tasks]
    for completed_task in asyncio.as_completed(async_tasks):
        completed_task_result = await completed_task
        print(completed_task_result)