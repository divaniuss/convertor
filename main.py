class Converter:
    def __init__(self):
        self.units = {
            1: 1000,
            2: 100,
            3: 1,
            4: 0.001
        }

    def convert(self):
        print("1. Миллиметр\n"
              "2. Сантиметр\n"
              "3. Метр\n"
              "4. Километр\n")

        choice_from = int(input("Введите вашу начальную единицу измерения (1-4): "))
        choice_into = int(input("Введите вашу конечную единицу измерения (1-4): "))
        value = float(input("Введите значение для конвертации: "))

        if choice_from not in self.units or choice_into not in self.units:
            print("Ошибка: некорректный ввод единиц измерения.")
            return


        result = value / self.units[choice_from] * self.units[choice_into]

        print(f"Результат: {result}")

c = Converter()
c.convert()
