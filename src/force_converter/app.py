import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


class ForceConverter(toga.App):
    def startup(self):
        # Inisialisasi jendela utama terlebih dahulu
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Bangun halaman menu utama
        self.build_main_menu()

        # Tampilkan jendela utama
        self.main_window.show()

    def build_main_menu(self):
        # Buat box utama
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

        title = toga.Label(
            "Select the Force Value Unit",
            style=Pack(padding_bottom=20, font_size=20, font_weight='bold')
        )
        main_box.add(title)

        units = ['Newton', 'dyne', 'kgf', 'lbf']
        for unit in units:
            button = toga.Button(
                f"Convert From {unit}",
                on_press=lambda w, u=unit: self.show_converter(u),
                style=Pack(padding=5, width=250, background_color='#007BFF', color='white')
            )
            main_box.add(button)

        # Set tampilan konten ke main menu
        self.main_window.content = main_box

    def show_converter(self, from_unit):
        # GUNAKAN LAYOUT BARU untuk halaman konversi
        converter_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

        title = toga.Label(
            f"Convert From {from_unit}",
            style=Pack(font_size=18, font_weight='bold', padding_bottom=15)
        )

        input_row = toga.Box(style=Pack(direction=ROW, padding_bottom=10, alignment=CENTER))
        input_box = toga.TextInput(placeholder='Enter value', style=Pack(width=200, padding_right=10))
        convert_button = toga.Button('Convert', style=Pack(width=100, background_color='#28a745', color='white'))
        input_row.add(input_box)
        input_row.add(convert_button)

        result_output = toga.MultilineTextInput(
            readonly=True,
            style=Pack(height=100, width=300, padding=(10, 0))
        )

        back_button = toga.Button(
            "Back",
            on_press=lambda w: self.build_main_menu(),
            style=Pack(padding_top=10, width=100, background_color='#dc3545', color='white')
        )

        # Tambahkan ke box baru
        converter_box.add(title)
        converter_box.add(input_row)
        converter_box.add(result_output)
        converter_box.add(back_button)

        # Tampilkan box baru
        self.main_window.content = converter_box

        # Fungsi konversi
        def convert_action(widget):
            try:
                value = float(input_box.value)
                newton_val = self.to_newton(value, from_unit)
                result_lines = []
                for unit in ['Newton', 'dyne', 'kgf', 'lbf']:
                    if unit != from_unit:
                        converted = self.from_newton(newton_val, unit)
                        result_lines.append(f"{converted:.5f} {unit}")
                result_output.value = "\n".join(result_lines)
            except ValueError:
                result_output.value = "Please enter a valid number."

        convert_button.on_press = convert_action

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
    return ForceConverter('Force Converter', 'org.example.forceconverter')