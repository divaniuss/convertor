
import tkinter as tk
from tkinter import ttk


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
        self.mass = {
            1: 1,
            2: 1000,
            3: 1000000
        }

    def convert_distance(self, choice_from, choice_into, value):
        if choice_from not in self.distances or choice_into not in self.distances:
            return "Ошибка: некорректные единицы измерения"

        try:
            value = float(value)
            result = value / self.distances[choice_from] * self.distances[choice_into]
            return f"Результат: {result}"
        except ValueError:
            return "Ошибка: введите число"

    def convert_time(self, choice_from, choice_into, value):
        if choice_from not in self.time or choice_into not in self.time:
            return "Ошибка: некорректные единицы измерения"

        try:
            value = float(value)
            result = value * self.time[choice_from] / self.time[choice_into]
            return f"Результат: {result}"
        except ValueError:
            return "Ошибка: введите число"

    def convert_mass(self, choice_from, choice_into, value):
        if choice_from not in self.mass or choice_into not in self.mass:
            return "Ошибка: некорректные единицы измерения"

        try:
            value = float(value)
            result = value * (self.mass[choice_from] / self.mass[choice_into])
            return f"Результат: {result}"
        except ValueError:
            return "Ошибка: введите число"


class ConverterApp:
    def __init__(self, root):
        self.converter = Converter()
        self.dark_mode = False

        root.title("Конвертер")
        root.geometry("400x350")

        self.dark_mode_var = tk.BooleanVar()
        self.theme_switch = tk.Checkbutton(root, text="Тёмная тема", variable=self.dark_mode_var, command=self.toggle_theme)
        self.theme_switch.pack()

        self.label_category = tk.Label(root, text="Категория:")
        self.label_category.pack()

        self.category = ttk.Combobox(root, values=["Расстояние", "Время", "Масса"])
        self.category.pack()
        self.category.current(0)
        self.category.bind("<<ComboboxSelected>>", self.update_units)

        self.label_from = tk.Label(root, text="Из:")
        self.label_from.pack()

        self.from_unit = ttk.Combobox(root)
        self.from_unit.pack()

        self.label_to = tk.Label(root, text="В:")
        self.label_to.pack()

        self.to_unit = ttk.Combobox(root)
        self.to_unit.pack()

        self.label_value = tk.Label(root, text="Значение:")
        self.label_value.pack()

        self.entry_value = tk.Entry(root)
        self.entry_value.pack()

        self.button_convert = tk.Button(root, text="Посчитать", command=self.calculate)
        self.button_convert.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack()

        self.unit_mapping = {
            "Расстояние": {
                "Миллиметр": 1,
                "Сантиметр": 2,
                "Метр": 3,
                "Километр": 4
            },
            "Время": {
                "Секунда": 1,
                "Минута": 2,
                "Час": 3,
                "День": 4
            },
            "Масса": {
                "Грамм": 1,
                "Килограмм": 2,
                "Тонна": 3
            }
        }

        self.update_units()

    def update_units(self, event=None):
        category = self.category.get()
        if category in self.unit_mapping:
            units = list(self.unit_mapping[category].keys())
        else:
            units = []

        self.from_unit["values"] = units
        self.to_unit["values"] = units

        if units:
            self.from_unit.current(0)
            self.to_unit.current(1)

    def calculate(self):
        category = self.category.get()
        from_unit_name = self.from_unit.get()
        to_unit_name = self.to_unit.get()
        value = self.entry_value.get()

        if category in self.unit_mapping and from_unit_name in self.unit_mapping[category] and to_unit_name in self.unit_mapping[category]:
            from_unit = self.unit_mapping[category][from_unit_name]
            to_unit = self.unit_mapping[category][to_unit_name]

            if category == "Расстояние":
                result = self.converter.convert_distance(from_unit, to_unit, value)
            elif category == "Время":
                result = self.converter.convert_time(from_unit, to_unit, value)
            elif category == "Масса":
                result = self.converter.convert_mass(from_unit, to_unit, value)
            else:
                result = "Ошибка: выберите категорию"
        else:
            result = "Ошибка: некорректные единицы измерения"

        self.result_label.config(text=result)
    def toggle_theme(self):
        if self.dark_mode_var.get():
            bg_color = "#333333"
            fg_color = "#ffffff"
            btn_color = "#555555"
        else:
            bg_color = "white"
            fg_color = "black"
            btn_color = "lightgray"

        root.config(bg=bg_color)

        for widget in [self.label_category, self.label_from, self.label_to, self.label_value, self.result_label]:
            widget.config(bg=bg_color, fg=fg_color)

        self.button_convert.config(bg=btn_color, fg=fg_color)
        self.theme_switch.config(bg=bg_color, fg=fg_color, selectcolor=bg_color)
        self.entry_value.config(bg=btn_color, fg=fg_color, insertbackground=fg_color)
        self.dark_mode = not self.dark_mode


root = tk.Tk()
app = ConverterApp(root)
root.mainloop()