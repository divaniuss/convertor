class Converter:
    def __init__(self):
        self.distances = {
            1: 1000,
            2: 100,
            3: 1,
            4: 0.001
        }
        self.time = {
            1: 1,
            2: 60,
            3: 3600,
            4: 86400
        }

    def convert_distance(self):
        print("1. Миллиметр\n"
              "2. Сантиметр\n"
              "3. Метр\n"
              "4. Километр\n")

        choice_from = int(input("Введите вашу начальную единицу измерения (1-4): "))
        choice_into = int(input("Введите вашу конечную единицу измерения (1-4): "))
        value = float(input("Введите значение для конвертации: "))

        if choice_from not in self.distances or choice_into not in self.distances:
            print("Ошибка: некорректный ввод единиц измерения.")
            return

        result = value / self.distances[choice_from] * self.distances[choice_into]

        print(f"Результат: {result}")

    def convert_time(self):
        print("1. Секунда\n"
              "2. Минута\n"
              "3. Час\n"
              "4. День\n")

        choice_from = int(input("Введите вашу начальную единицу измерения (1-4): "))
        choice_into = int(input("Введите вашу конечную единицу измерения (1-4): "))
        value = float(input("Введите значение для конвертации: "))

        if choice_from not in self.time or choice_into not in self.time:
            print("Ошибка: некорректный ввод единиц измерения.")
            return

        result = value / self.time[choice_from] * self.time[choice_into]

        print(f"Результат: {result}")

c = Converter()


while True:
    choice = str(input("Вы хотите конвертировать дистанции(1) или время(2): "))

    if choice == "1":
        c.convert_distance()
        break
    elif choice == "2":
        c.convert_time()
        break
    else:
        print("Введите правильные значения")

