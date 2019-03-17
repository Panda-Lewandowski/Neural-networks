import random




class Perceptron:
    def __init__(self, input_layer, weights=None, bias=7):
        # Инициализация весов сети
        if weights is None:
            self.weights = [0 for i in range(15)]
        else: 
            self.weights = weights

        # Порог функции активации(вот вообще любой, но от настроения берем 7)
        self.bias = bias
        self.input = input_layer


    # Является ли данное число 5 ? мы это проверяем
    def proceed(self, number):
        # Рассчитываем взвешенную сумму (подсуммируем сумму , которая будет являться инпутами, умноженными на веса)
        net = 0
        for i in range(15):
            net += int(number[i]) * self.weights[i]
    
        # Превышен ли порог? (Да - сеть думает, что это 5. Нет - сеть думает, что это другая цифра)
        return net >= self.bias # по сути return 1 или 0


    #Делаем еще 2 вспомогательные функции
    # Уменьшение значений весов, если сеть ошиблась и выдала 1
    def decrease(self, number):
        for i in range(15):
            # Возбужденный ли вход
            if int(number[i]) == 1: # преобразование ,так как самому перцептону мы подаем в строковом виде
                # Уменьшаем связанный с ним вес на единицу (вообще ,не обязательно на 1, мы это делаем в зависимости от настроения, ничего не мешает взять нам 0.2, но мы берем 1)
                self.weights[i] -= 1


    # Увеличение значений весов, если сеть ошиблась и выдала 0
    def increase(self, number):
        for i in range(15):
            # Возбужденный ли вход
            if int(number[i]) == 1: #насчет приведения ты тоже , должно быть, помнишь)
                # Увеличиваем связанный с ним вес на единицу(ну ты помнишь)
                self.weights[i] += 1


    def train(self, times=10000):
        # Тренировка сети
        for i in range(times): # решая обучать, мы 1к раз пробегаемся циклом по выполняемым функциям
            # Генерируем случайное число от 0 до 9
            option = random.randint(0, 9)
        
            # Если получилось НЕ число 5
            if option != 5:
                # Если сеть выдала True/Да/1, то это заслуживает наказания(так как не 5, но она распознала его , как 5)
                if self.proceed(self.input[option]):
                    self.decrease(self.input[option])
            # Если получилось число 5
            else:
                # Если сеть выдала False/Нет/0, то показываем, что эта цифра - то, что нам нужно, и увеличиваем значение веса. Наше поощрение, так сказать
                if not self.proceed(num5):
                    self.increase(num5)


if __name__ == "__main__":
    # Цифры (Обучающая выборка)
    num0 = list('111101101101111')
    num1 = list('001001001001001')
    num2 = list('111001111100111')
    num3 = list('111001111001111')
    num4 = list('101101111001001')
    num5 = list('111100111001111')
    num6 = list('111100111101111')
    num7 = list('111001001001001')
    num8 = list('111101111101111')
    num9 = list('111101111001111')

    # Список всех вышеуказанных цифр - т.е весь наш входной слой собран в одну кучу
    nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

    # Виды цифры 5 (Тестовая выборка) - куча кривых картинок
    num51 = list('111100111000111')
    num52 = list('111100010001111')
    num53 = list('111100011001111')
    num54 = list('110100111001111')
    num55 = list('110100111001011')
    num56 = list('111100101001111')

    per = Perceptron(input_layer=nums)
    per.train()

    # Вывод значений весов
    print(per.weights)
    
    # Прогон по обучающей выборке
    print("Обучающая выборка")
    print("0 это 5? ", per.proceed(num0))
    print("1 это 5? ", per.proceed(num1))
    print("2 это 5? ", per.proceed(num2))
    print("3 это 5? ", per.proceed(num3))
    print("4 это 5? ", per.proceed(num4))
    print("6 это 5? ", per.proceed(num6))
    print("7 это 5? ", per.proceed(num7))
    print("8 это 5? ", per.proceed(num8))
    print("9 это 5? ", per.proceed(num9), '\n')
    
    # Прогон по тестовой выборке
    print("Тестовая выборка")
    print("Узнал 5? ", per.proceed(num5))
    print("Узнал 5 - 1? ", per.proceed(num51))
    print("Узнал 5 - 2? ", per.proceed(num52))
    print("Узнал 5 - 3? ", per.proceed(num53))
    print("Узнал 5 - 4? ", per.proceed(num54))
    print("Узнал 5 - 5? ", per.proceed(num55))
    print("Узнал 5 - 6? ", per.proceed(num56))





