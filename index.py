try:
    calulate=input('Список операций калькулятора: "+" - сложение\n "-" - вычитание \n "*" - умножение\n "/"- деление\n'
                'Введите нужную вам операцию:')

    a=float(input('Введите первое число: '))
    b=float(input('Введите второе число: '))

    if calulate not in ('+','-','/'):
        raise Exception("Вы ввели неккоректную операцию")


    if calulate == '+':
        print(f'Результат вычесления: {a+b}')
    elif calulate == '-':
        print(f'Результат вычесления: {a-b}')
    elif calulate == '*':
        print(f'Результат вычесления: {a*b}')
    elif calulate == '/':
        print(f'Результат вычесления: {a/b}')    
except ZeroDivisionError: 
    print("Вы не можете делить на ноль!!!")    
    # Исключаем ошибку деления на 0
except ValueError:
    print("вы должны вводить цифры")
except Exception as exs:    
    print(exs)
except: 
    print("Неизвестная ошибка")
finally:
    print("Калькулятор завершил работу")    
