def tryIt(func, *args, **kwargs):
    try:
        print(*args, kwargs)
        return func(*args, **kwargs)
    except Exception as e:
        print(f'\n\n\n\n{e}\n\n\n\n')