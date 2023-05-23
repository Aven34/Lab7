def cast(t):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                print(f'Преобразуем {result} из {type(result)} в {t}')
                return t(result)
            except:
                print(f'Ошибка преобразования, нельзя преобразовать тип {type(result)} в {t}')
                return None
        return wrapper
    return decorator
    
    
    
@cast(float)
def func1(a):
    return 26

@cast(int)
def func2():
    return "PoE"
    
if __name__ == '__main__':
    func1 = func1(26)
    print(func1)
    func2 = func2()
    print(func2)
