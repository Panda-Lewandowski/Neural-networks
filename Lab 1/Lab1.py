import random

class Perceptron:
    def __init__(self, input_layer, weights=None, bias=0, learining_rate=0.01):
        if weights is None:
            self.weights = [random.random() * 2 - 1 for _ in range(len(input_layer))]
        else: 
            self.weights = weights

        self.bias = bias
        self.input = input_layer
        self.learning_rate = learining_rate
        self.size = len(self.input)


    def proceed(self, number):
        net = sum([int(number[i]) * self.weights[i] \
            for i in range(self.size)])

        return 1 if net >= self.bias else -1 


    def update_weights(self, data, iter_error): # FIXME что должно быть в data?
        self.weights = \
            [i + self.learning_rate * iter_error * data for i in self.weights]


    def train(self, max_iter=100):
        learned = False
        iterations = 0
        while not learned: 
            global_error = 0
            option = random.randint(0, 9)
            response = self.proceed(self.input[option])

            if response != option:
                iter_error = -1 # FIXME
                self.update_weights(option, iter_error)
                global_error += abs(iter_error)
            iterations += 1
            if global_error == 0.0 or iterations >= max_iter:
                print(f'iterations: {iterations}')
                learned = True


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





