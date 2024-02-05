# MultiParser
    
    parser = Parser()    
    parser.proxies.add(Proxy('HTTP', 'localhost'))
    parser.services.add(Service('site', 50))

    await parser.run_manager()
    
    tasks = [Task('http://site.com', 'site') for i in range(100)]

    # Sequential execution, with Task 2 starting only after Task 1 completes
    for task in tasks:
        res = await parser.run_task(task)
        print(res) -> [Request]


    # Parallel execution, starting all tasks simultaneously.
    tasks = [parser.run_task(task) for task in tasks]
    for task in asyncio.as_completed(tasks):
        res = await task
        print(res) -> [Request]
