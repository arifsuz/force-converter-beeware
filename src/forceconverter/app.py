import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


class ForceConverterApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20, alignment="center"))

        # Judul (Bold, Center)
        title = toga.Label(
            "Select the Force Value Unit",
            style=Pack(
                padding=(0, 0, 20, 0),
                font_size=20,
                font_weight='bold',
                text_align='center'
            )
        )
        main_box.add(title)

        # Tombol pilihan satuan dengan warna
        for unit in ['Newton', 'dyne', 'kgf', 'lbf']:
            button = toga.Button(
                f"Convert From {unit}",
                on_press=lambda w, u=unit: self.open_converter(u),
                style=Pack(
                    padding=5,
                    width=250,
                    background_color='#007BFF',
                    color='white'
                )
            )
            main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def open_converter(self, from_unit):
        box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        input_row = toga.Box(style=Pack(direction=ROW, padding_bottom=10))
        input_box = toga.TextInput(placeholder='Input Value', style=Pack(flex=1, padding_right=10))
        convert_button = toga.Button('Convert', style=Pack(width=100, background_color='#007BFF', color='white'))

        result_label = toga.Label('', style=Pack(padding_top=10))

        input_row.add(input_box)
        input_row.add(convert_button)

        box.add(toga.Label(f"Convert From {from_unit}", style=Pack(font_size=18, font_weight='bold', padding_bottom=10)))
        box.add(input_row)
        box.add(result_label)

        def convert_action(widget):
            try:
                value = float(input_box.value)
                newton_value = self.to_newton(value, from_unit)
                result_text = ''
                for unit in ['Newton', 'dyne', 'kgf', 'lbf']:
                    if unit != from_unit:
                        converted = self.from_newton(newton_value, unit)
                        result_text += f"{converted:.5f} {unit}\n"
                result_label.text = result_text.strip()
            except ValueError:
                result_label.text = "Enter a valid number"

        convert_button.on_press = convert_action

        conv_window = toga.Window(title=f"Convert From {from_unit}")
        conv_window.content = box
        conv_window.show()

    def to_newton(self, value, unit):
        conversion = {
            'Newton': 1,
            'dyne': 1e-5,
            'kgf': 9.80665,
            'lbf': 4.44822
        }
        return value * conversion[unit]

    def from_newton(self, value, unit):
        conversion = {
            'Newton': 1,
            'dyne': 1e5,
            'kgf': 1 / 9.80665,
            'lbf': 1 / 4.44822
        }
        return value * conversion[unit]


def main():
    return ForceConverterApp('Force Converter', 'org.example.forceconverter')