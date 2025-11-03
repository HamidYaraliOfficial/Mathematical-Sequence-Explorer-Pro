import sys
import os
import math
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QComboBox, QSpinBox,
    QGroupBox, QTabWidget, QFileDialog, QMessageBox,
    QInputDialog, QFrame, QGridLayout, QStyleFactory
)
from PyQt6.QtCore import Qt, pyqtSignal, QTimer
from PyQt6.QtGui import QFont, QPalette, QColor, QLinearGradient, QBrush, QIcon, QPixmap

# ------------------- Application Info -------------------
APP_NAME = "Mathematical Sequence Explorer Pro"
APP_VERSION = "3.7"
APP_AUTHOR = "xAI Advanced Labs"

# ------------------- Translation Strings -------------------
translations = {
    "en": {
        "title": "Mathematical Sequence Explorer",
        "description": "Explore famous mathematical sequences: Fibonacci, Lucas, Pell, Triangular, Square, and more.",
        "generate": "Generate",
        "clear": "Clear All",
        "copy": "Copy Output",
        "export": "Export to File",
        "language": "Language",
        "theme": "Theme",
        "sequence": "Sequence Type",
        "count": "Number of Terms:",
        "start": "Start Value (for custom):",
        "output": "Sequence Output",
        "properties": "Mathematical Properties",
        "formula": "Formula",
        "closed_form": "Closed-Form",
        "sum_formula": "Sum of First n Terms",
        "relation": "Recurrence Relation",
        "system_theme": "System Default",
        "light_theme": "Light Mode",
        "dark_theme": "Dark Mode",
        "red_theme": "Crimson Fire",
        "blue_theme": "Ocean Depth",
        "green_theme": "Emerald Forest",
        "purple_theme": "Amethyst Glow",
        "orange_theme": "Sunset Blaze",
        "fibonacci": "Fibonacci Sequence",
        "lucas": "Lucas Sequence",
        "pell": "Pell Numbers",
        "triangular": "Triangular Numbers",
        "square": "Square Numbers",
        "cube": "Cube Numbers",
        "factorial": "Factorial Sequence",
        "catalan": "Catalan Numbers",
        "harmonic": "Harmonic Series (Partial Sums)",
        "prime": "Prime Numbers",
        "collatz": "Collatz Sequence (3n+1)",
        "custom": "Custom Linear Recurrence",
        "rtl": False
    },
    "fa": {
        "title": "کاوشگر دنباله‌های ریاضی",
        "description": "کاوش دنباله‌های معروف ریاضی: فیبوناچی، لوکاس، پل، مثلثی، مربع و بیشتر.",
        "generate": "تولید",
        "clear": "پاک کردن همه",
        "copy": "کپی خروجی",
        "export": "خروجی به فایل",
        "language": "زبان",
        "theme": "تم",
        "sequence": "نوع دنباله",
        "count": "تعداد اعضا:",
        "start": "مقدار اولیه (برای سفارشی):",
        "output": "خروجی دنباله",
        "properties": "ویژگی‌های ریاضی",
        "formula": "فرمول",
        "closed_form": "فرم بسته",
        "sum_formula": "مجموع n عضو اول",
        "relation": "رابطه بازگشتی",
        "system_theme": "پیش‌فرض سیستم",
        "light_theme": "روشن",
        "dark_theme": "تیره",
        "red_theme": "آتش سرخ",
        "blue_theme": "عمق اقیانوس",
        "green_theme": "جنگل زمردین",
        "purple_theme": "درخشش آمتیست",
        "orange_theme": "غروب آتشین",
        "fibonacci": "دنباله فیبوناچی",
        "lucas": "دنباله لوکاس",
        "pell": "اعداد پل",
        "triangular": "اعداد مثلثی",
        "square": "اعداد مربع",
        "cube": "اعداد مکعب",
        "factorial": "دنباله فاکتوریل",
        "catalan": "اعداد کاتالان",
        "harmonic": "سری هارمونیک (جمع جزئی)",
        "prime": "اعداد اول",
        "collatz": "دنباله کولاتز (3n+1)",
        "custom": "بازگشت خطی سفارشی",
        "rtl": True
    },
    "zh": {
        "title": "数学序列探索器",
        "description": "探索著名数学序列：斐波那契、卢卡斯、佩尔、三角形、平方等。",
        "generate": "生成",
        "clear": "全部清除",
        "copy": "复制输出",
        "export": "导出到文件",
        "language": "语言",
        "theme": "主题",
        "sequence": "序列类型",
        "count": "项数：",
        "start": "起始值（自定义）：",
        "output": "序列输出",
        "properties": "数学性质",
        "formula": "公式",
        "closed_form": "闭合形式",
        "sum_formula": "前n项和",
        "relation": "递推关系",
        "system_theme": "系统默认",
        "light_theme": "浅色模式",
        "dark_theme": "深色模式",
        "red_theme": "赤红之火",
        "blue_theme": "海洋深渊",
        "green_theme": "翡翠森林",
        "purple_theme": "紫水晶光辉",
        "orange_theme": "落日烈焰",
        "fibonacci": "斐波那契数列",
        "lucas": "卢卡斯数列",
        "pell": "佩尔数",
        "triangular": "三角形数",
        "square": "平方数",
        "cube": "立方数",
        "factorial": "阶乘序列",
        "catalan": "卡特兰数",
        "harmonic": "调和级数（部分和）",
        "prime": "质数",
        "collatz": "科尔拉茨序列 (3n+1)",
        "custom": "自定义线性递推",
        "rtl": False
    },
    "ru": {
        "title": "Исследователь математических последовательностей",
        "description": "Исследуйте известные математические последовательности: Фибоначчи, Лукаса, Пелля, треугольные, квадраты и др.",
        "generate": "Сгенерировать",
        "clear": "Очистить всё",
        "copy": "Копировать вывод",
        "export": "Экспорт в файл",
        "language": "Язык",
        "theme": "Тема",
        "sequence": "Тип последовательности",
        "count": "Количество членов:",
        "start": "Начальное значение (для кастомной):",
        "output": "Вывод последовательности",
        "properties": "Математические свойства",
        "formula": "Формула",
        "closed_form": "Замкнутая форма",
        "sum_formula": "Сумма первых n членов",
        "relation": "Рекуррентное соотношение",
        "system_theme": "По умолчанию системы",
        "light_theme": "Светлая",
        "dark_theme": "Тёмная",
        "red_theme": "Багровый огонь",
        "blue_theme": "Глубины океана",
        "green_theme": "Изумрудный лес",
        "purple_theme": "Аметистовое сияние",
        "orange_theme": "Пламя заката",
        "fibonacci": "Последовательность Фибоначчи",
        "lucas": "Последовательность Лукаса",
        "pell": "Числа Пелля",
        "triangular": "Треугольные числа",
        "square": "Квадратные числа",
        "cube": "Кубические числа",
        "factorial": "Факториальная последовательность",
        "catalan": "Числа Каталана",
        "harmonic": "Гармонический ряд (частичные суммы)",
        "prime": "Простые числа",
        "collatz": "Последовательность Коллатца (3n+1)",
        "custom": "Пользовательская линейная рекурренция",
        "rtl": False
    }
}

# ------------------- Theme Engine -------------------
def apply_light_theme(app):
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(245, 247, 250))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(20, 20, 35))
    palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(248, 250, 252))
    palette.setColor(QPalette.ColorRole.Text, QColor(20, 20, 35))
    palette.setColor(QPalette.ColorRole.Button, QColor(235, 238, 242))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(20, 20, 35))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(0, 120, 215))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Link, QColor(0, 100, 180))
    app.setPalette(palette)

def apply_dark_theme(app):
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(28, 28, 35))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(230, 230, 240))
    palette.setColor(QPalette.ColorRole.Base, QColor(40, 40, 48))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(50, 50, 58))
    palette.setColor(QPalette.ColorRole.Text, QColor(230, 230, 240))
    palette.setColor(QPalette.ColorRole.Button, QColor(55, 55, 65))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(230, 230, 240))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(80, 160, 255))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
    palette.setColor(QPalette.ColorRole.Link, QColor(100, 180, 255))
    app.setPalette(palette)

def apply_red_theme(app):
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(40, 10, 15))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 200, 200))
    palette.setColor(QPalette.ColorRole.Base, QColor(60, 15, 20))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(80, 20, 25))
    palette.setColor(QPalette.ColorRole.Text, QColor(255, 220, 220))
    palette.setColor(QPalette.ColorRole.Button, QColor(120, 30, 40))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 230, 230))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(255, 90, 100))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)

def apply_blue_theme(app):
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(10, 25, 45))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(200, 230, 255))
    palette.setColor(QPalette.ColorRole.Base, QColor(15, 35, 65))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(20, 45, 85))
    palette.setColor(QPalette.ColorRole.Text, QColor(200, 230, 255))
    palette.setColor(QPalette.ColorRole.Button, QColor(25, 60, 110))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(220, 240, 255))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(80, 160, 255))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)

def apply_green_theme(app):
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(10, 40, 20))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(200, 255, 200))
    palette.setColor(QPalette.ColorRole.Base, QColor(15, 60, 30))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(20, 80, 40))
    palette.setColor(QPalette.ColorRole.Text, QColor(200, 255, 200))
    palette.setColor(QPalette.ColorRole.Button, QColor(30, 100, 50))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(220, 255, 220))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(100, 200, 100))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)

def apply_purple_theme(app):
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(35, 15, 50))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(230, 200, 255))
    palette.setColor(QPalette.ColorRole.Base, QColor(50, 25, 70))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(65, 35, 85))
    palette.setColor(QPalette.ColorRole.Text, QColor(230, 200, 255))
    palette.setColor(QPalette.ColorRole.Button, QColor(90, 50, 120))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(240, 220, 255))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(180, 120, 255))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)

def apply_orange_theme(app):
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(50, 25, 10))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 220, 180))
    palette.setColor(QPalette.ColorRole.Base, QColor(70, 35, 15))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(90, 45, 20))
    palette.setColor(QPalette.ColorRole.Text, QColor(255, 220, 180))
    palette.setColor(QPalette.ColorRole.Button, QColor(130, 65, 30))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 240, 200))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(255, 160, 80))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)

def apply_system_theme(app):
    app.setStyle("WindowsVista")
    app.setPalette(QApplication.style().standardPalette())

# ------------------- Sequence Generators -------------------
class SequenceGenerator:
    @staticmethod
    def fibonacci(n):
        if n <= 0: return []
        if n == 1: return [0]
        if n == 2: return [0, 1]
        a, b = 0, 1
        seq = [a, b]
        for _ in range(2, n):
            a, b = b, a + b
            seq.append(b)
        return seq

    @staticmethod
    def lucas(n):
        if n <= 0: return []
        if n == 1: return [2]
        if n == 2: return [2, 1]
        a, b = 2, 1
        seq = [a, b]
        for _ in range(2, n):
            a, b = b, a + b
            seq.append(b)
        return seq

    @staticmethod
    def pell(n):
        if n <= 0: return []
        if n == 1: return [0]
        if n == 2: return [0, 1]
        a, b = 0, 1
        seq = [a, b]
        for _ in range(2, n):
            a, b = b, 2*b + a
            seq.append(b)
        return seq

    @staticmethod
    def triangular(n):
        return [i*(i+1)//2 for i in range(1, n+1)]

    @staticmethod
    def square(n):
        return [i*i for i in range(1, n+1)]

    @staticmethod
    def cube(n):
        return [i*i*i for i in range(1, n+1)]

    @staticmethod
    def factorial(n):
        if n <= 0: return []
        seq = [1]
        for i in range(1, n):
            seq.append(seq[-1] * (i + 1))
        return seq

    @staticmethod
    def catalan(n):
        if n <= 0: return []
        seq = []
        c = 1
        for i in range(n):
            if i == 0:
                seq.append(1)
            else:
                c = c * 2 * (2*i + 1) // (i + 2)
                seq.append(c)
        return seq

    @staticmethod
    def harmonic(n):
        if n <= 0: return []
        return [sum(1.0/k for k in range(1, i+1)) for i in range(1, n+1)]

    @staticmethod
    def prime(n):
        if n <= 0: return []
        primes = []
        num = 2
        while len(primes) < n:
            if all(num % p != 0 for p in primes):
                primes.append(num)
            num += 1
        return primes

    @staticmethod
    def collatz(start, steps):
        seq = [start]
        for _ in range(steps):
            if start % 2 == 0:
                start //= 2
            else:
                start = 3 * start + 1
            seq.append(start)
            if start == 1:
                break
        return seq

    @staticmethod
    def custom_linear(a, b, n):
        if n <= 0: return []
        seq = [a, b]
        for _ in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq

# ------------------- Properties Database -------------------
sequence_properties = {
    "fibonacci": {
        "en": {"formula": "F(n) = F(n-1) + F(n-2)", "closed_form": "F(n) = (φ^n - (-φ)^(-n)) / √5", "sum": "Sum = F(n+2) - 1"},
        "fa": {"formula": "F(n) = F(n-1) + F(n-2)", "closed_form": "F(n) = (φ^n - (-φ)^(-n)) / √5", "sum": "مجموع = F(n+2) - 1"},
        "zh": {"formula": "F(n) = F(n-1) + F(n-2)", "closed_form": "F(n) = (φ^n - (-φ)^(-n)) / √5", "sum": "总和 = F(n+2) - 1"},
        "ru": {"formula": "F(n) = F(n-1) + F(n-2)", "closed_form": "F(n) = (φ^n - (-φ)^(-n)) / √5", "sum": "Сумма = F(n+2) - 1"}
    },
    "lucas": {
        "en": {"formula": "L(n) = L(n-1) + L(n-2)", "closed_form": "L(n) = φ^n + (-φ)^(-n)", "sum": "Sum = L(n+2) - 3"},
        "fa": {"formula": "L(n) = L(n-1) + L(n-2)", "closed_form": "L(n) = φ^n + (-φ)^(-n)", "sum": "مجموع = L(n+2) - 3"},
        "zh": {"formula": "L(n) = L(n-1) + L(n-2)", "closed_form": "L(n) = φ^n + (-φ)^(-n)", "sum": "总和 = L(n+2) - 3"},
        "ru": {"formula": "L(n) = L(n-1) + L(n-2)", "closed_form": "L(n) = φ^n + (-φ)^(-n)", "sum": "Сумма = L(n+2) - 3"}
    },
    "pell": {
        "en": {"formula": "P(n) = 2*P(n-1) + P(n-2)", "closed_form": "P(n) = ((1+√2)^n - (1-√2)^n)/(2√2)", "sum": "No simple closed sum"},
        "fa": {"formula": "P(n) = 2*P(n-1) + P(n-2)", "closed_form": "P(n) = ((1+√2)^n - (1-√2)^n)/(2√2)", "sum": "بدون جمع بسته ساده"},
        "zh": {"formula": "P(n) = 2*P(n-1) + P(n-2)", "closed_form": "P(n) = ((1+√2)^n - (1-√2)^n)/(2√2)", "sum": "无简单闭合和"},
        "ru": {"formula": "P(n) = 2*P(n-1) + P(n-2)", "closed_form": "P(n) = ((1+√2)^n - (1-√2)^n)/(2√2)", "sum": "Нет простой суммы"}
    },
    "triangular": {
        "en": {"formula": "T(n) = n(n+1)/2", "closed_form": "Same", "sum": "Sum of first k = k(k+1)(k+2)/6"},
        "fa": {"formula": "T(n) = n(n+1)/2", "closed_form": "همان", "sum": "مجموع k اولی = k(k+1)(k+2)/6"},
        "zh": {"formula": "T(n) = n(n+1)/2", "closed_form": "相同", "sum": "前k项和 = k(k+1)(k+2)/6"},
        "ru": {"formula": "T(n) = n(n+1)/2", "closed_form": "То же", "sum": "Сумма первых k = k(k+1)(k+2)/6"}
    }
}

# ------------------- Custom Widgets -------------------
class GradientHeader(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(120)
        self.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #667eea, stop:1 #764ba2);
                border-radius: 20px;
                margin: 10px;
            }
        """)

class StyledButton(QPushButton):
    def __init__(self, text, parent=None, primary=False):
        super().__init__(text, parent)
        self.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(42)
        base = "#0078D4" if primary else "#5C5C5C"
        hover = "#106EBE" if primary else "#707070"
        pressed = "#005A9E" if primary else "#505050"
        self.setStyleSheet(f"""
            QPushButton {{
                border-radius: 14px;
                padding: 10px 20px;
                background-color: {base};
                color: white;
                border: none;
            }}
            QPushButton:hover {{
                background-color: {hover};
            }}
            QPushButton:pressed {{
                background-color: {pressed};
            }}
        """)

class StyledComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont("Segoe UI", 10))
        self.setMinimumHeight(40)
        self.setStyleSheet("""
            QComboBox {
                border: 2px solid #CED4DA;
                border-radius: 12px;
                padding: 8px 16px;
                background-color: white;
                color: #212529;
            }
            QComboBox::drop-down {
                border: 0px;
                width: 36px;
            }
            QComboBox::down-arrow {
                width: 16px;
                height: 16px;
            }
            QComboBox QAbstractItemView {
                border: 2px solid #0078D4;
                selection-background-color: #0078D4;
                background-color: white;
                color: #212529;
                padding: 5px;
            }
        """)

class StyledSpinBox(QSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont("Segoe UI", 11))
        self.setRange(1, 500)
        self.setValue(20)
        self.setMinimumHeight(40)
        self.setStyleSheet("""
            QSpinBox {
                border: 2px solid #CED4DA;
                border-radius: 12px;
                padding: 8px 16px;
                background-color: white;
                color: #212529;
            }
            QSpinBox::up-button, QSpinBox::down-button {
                width: 24px;
                border-left: 1px solid #CED4DA;
                background-color: #F8F9FA;
            }
        """)

class OutputTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont("Consolas", 11))
        self.setStyleSheet("""
            QTextEdit {
                border: 2px solid #CED4DA;
                border-radius: 14px;
                padding: 14px;
                background-color: #F8F9FA;
                color: #212529;
            }
        """)

# ------------------- Main Application -------------------
class MathSequenceExplorer(QMainWindow):
    language_changed = pyqtSignal(str)
    theme_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.current_lang = "en"
        self.current_theme = "system"
        self.trans = translations[self.current_lang]
        self.generator = SequenceGenerator()
        self.init_ui()
        self.apply_initial_theme()
        self.language_changed.connect(self.update_language)
        self.theme_changed.connect(self.update_theme)

    def init_ui(self):
        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION}")
        self.setGeometry(100, 100, 1280, 800)
        self.setMinimumSize(1000, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(18)

        # Header
        header = GradientHeader()
        header_layout = QVBoxLayout(header)
        title = QLabel(self.trans["title"])
        title.setFont(QFont("Segoe UI", 26, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: white; margin: 10px;")
        desc = QLabel(self.trans["description"])
        desc.setFont(QFont("Segoe UI", 11))
        desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #E0E0FF; margin: 5px 20px;")
        header_layout.addWidget(title)
        header_layout.addWidget(desc)
        layout.addWidget(header)

        # Tabs
        tabs = QTabWidget()
        tabs.setFont(QFont("Segoe UI", 11))
        tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #DEE2E6;
                border-radius: 12px;
                background-color: #F8F9FA;
            }
            QTabBar::tab {
                padding: 12px 24px;
                margin: 2px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            QTabBar::tab:selected {
                background-color: #0078D4;
                color: white;
            }
        """)

        gen_tab = self.create_generator_tab()
        props_tab = self.create_properties_tab()
        tabs.addTab(gen_tab, "Generator")
        tabs.addTab(props_tab, "Properties")
        layout.addWidget(tabs, stretch=1)

        # Status Bar
        self.statusBar().showMessage(f"{APP_NAME} • {APP_VERSION} • Ready")

    def create_generator_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(16)

        # Control Panel
        control = QGroupBox("Control Panel")
        control.setStyleSheet(self.get_groupbox_style())
        control_layout = QGridLayout(control)

        # Language
        lang_label = QLabel(self.trans["language"] + ":")
        self.lang_combo = StyledComboBox()
        self.lang_combo.addItems(["English", "فارسی", "中文", "Русский"])
        self.lang_combo.currentIndexChanged.connect(self.change_language)

        # Theme
        theme_label = QLabel(self.trans["theme"] + ":")
        self.theme_combo = StyledComboBox()
        themes = [
            self.trans["system_theme"], self.trans["light_theme"], self.trans["dark_theme"],
            self.trans["red_theme"], self.trans["blue_theme"], self.trans["green_theme"],
            self.trans["purple_theme"], self.trans["orange_theme"]
        ]
        self.theme_combo.addItems(themes)
        self.theme_combo.currentIndexChanged.connect(self.change_theme)

        # Sequence Type
        seq_label = QLabel(self.trans["sequence"] + ":")
        self.seq_combo = StyledComboBox()
        sequences = [
            self.trans["fibonacci"], self.trans["lucas"], self.trans["pell"],
            self.trans["triangular"], self.trans["square"], self.trans["cube"],
            self.trans["factorial"], self.trans["catalan"], self.trans["harmonic"],
            self.trans["prime"], self.trans["collatz"], self.trans["custom"]
        ]
        self.seq_combo.addItems(sequences)
        self.seq_combo.currentIndexChanged.connect(self.on_sequence_changed)

        # Term Count
        count_label = QLabel(self.trans["count"])
        self.count_spin = StyledSpinBox()
        self.count_spin.setRange(1, 1000)

        # Start Value
        self.start_label = QLabel(self.trans["start"])
        self.start_spin = StyledSpinBox()
        self.start_spin.setValue(7)
        self.start_spin.setRange(1, 1000000)
        self.start_label.setVisible(False)
        self.start_spin.setVisible(False)

        # Buttons
        self.generate_btn = StyledButton(self.trans["generate"], primary=True)
        self.generate_btn.clicked.connect(self.generate_sequence)
        self.clear_btn = StyledButton(self.trans["clear"])
        self.clear_btn.clicked.connect(self.clear_all)
        self.copy_btn = StyledButton(self.trans["copy"])
        self.copy_btn.clicked.connect(self.copy_output)
        self.export_btn = StyledButton(self.trans["export"])
        self.export_btn.clicked.connect(self.export_to_file)

        # Grid Layout
        control_layout.addWidget(lang_label, 0, 0)
        control_layout.addWidget(self.lang_combo, 0, 1)
        control_layout.addWidget(theme_label, 0, 2)
        control_layout.addWidget(self.theme_combo, 0, 3)

        control_layout.addWidget(seq_label, 1, 0)
        control_layout.addWidget(self.seq_combo, 1, 1)
        control_layout.addWidget(count_label, 1, 2)
        control_layout.addWidget(self.count_spin, 1, 3)

        control_layout.addWidget(self.start_label, 2, 0)
        control_layout.addWidget(self.start_spin, 2, 1)
        control_layout.addWidget(self.generate_btn, 2, 2)
        control_layout.addWidget(self.clear_btn, 2, 3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.copy_btn)
        hbox.addWidget(self.export_btn)
        control_layout.addLayout(hbox, 3, 0, 1, 4)

        layout.addWidget(control)

        # Output
        output_group = QGroupBox(self.trans["output"])
        output_group.setStyleSheet(self.get_groupbox_style())
        output_layout = QVBoxLayout(output_group)
        self.output_text = OutputTextEdit()
        self.output_text.setReadOnly(True)
        output_layout.addWidget(self.output_text)
        layout.addWidget(output_group, stretch=1)

        return widget

    def create_properties_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        self.props_text = QTextEdit()
        self.props_text.setReadOnly(True)
        self.props_text.setFont(QFont("Segoe UI", 11))
        self.props_text.setStyleSheet("""
            QTextEdit {
                border: 2px solid #CED4DA;
                border-radius: 14px;
                padding: 16px;
                background-color: #F8F9FA;
                color: #212529;
            }
        """)
        layout.addWidget(self.props_text)
        return widget

    def get_groupbox_style(self):
        return """
            QGroupBox {
                font-weight: bold;
                font-size: 15px;
                border: 2px solid #DEE2E6;
                border-radius: 16px;
                margin-top: 16px;
                padding-top: 12px;
                background-color: rgba(248, 249, 250, 245);
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 14px;
                color: #495057;
            }
        """

    def apply_initial_theme(self):
        theme_map = {
            0: "system", 1: "light", 2: "dark", 3: "red",
            4: "blue", 5: "green", 6: "purple", 7: "orange"
        }
        theme = theme_map.get(self.theme_combo.currentIndex(), "system")
        self.apply_theme(theme)

    def change_language(self, index):
        lang_map = {0: "en", 1: "fa", 2: "zh", 3: "ru"}
        lang = lang_map.get(index, "en")
        if lang != self.current_lang:
            self.current_lang = lang
            self.trans = translations[lang]
            self.language_changed.emit(lang)

    def change_theme(self, index):
        theme_map = {
            0: "system", 1: "light", 2: "dark", 3: "red",
            4: "blue", 5: "green", 6: "purple", 7: "orange"
        }
        theme = theme_map.get(index, "system")
        if theme != self.current_theme:
            self.current_theme = theme
            self.theme_changed.emit(theme)

    def on_sequence_changed(self, index):
        seq = self.get_current_sequence_key()
        show_start = seq in ["collatz", "custom"]
        self.start_label.setVisible(show_start)
        self.start_spin.setVisible(show_start)
        self.update_properties()

    def get_current_sequence_key(self):
        mapping = {
            0: "fibonacci", 1: "lucas", 2: "pell", 3: "triangular",
            4: "square", 5: "cube", 6: "factorial", 7: "catalan",
            8: "harmonic", 9: "prime", 10: "collatz", 11: "custom"
        }
        return mapping.get(self.seq_combo.currentIndex(), "fibonacci")

    def generate_sequence(self):
        seq_key = self.get_current_sequence_key()
        n = self.count_spin.value()
        output = f"Sequence: {self.seq_combo.currentText()}\n"
        output += f"Terms: {n}\n"
        output += "-" * 50 + "\n"

        try:
            if seq_key == "fibonacci":
                seq = self.generator.fibonacci(n)
            elif seq_key == "lucas":
                seq = self.generator.lucas(n)
            elif seq_key == "pell":
                seq = self.generator.pell(n)
            elif seq_key == "triangular":
                seq = self.generator.triangular(n)
            elif seq_key == "square":
                seq = self.generator.square(n)
            elif seq_key == "cube":
                seq = self.generator.cube(n)
            elif seq_key == "factorial":
                seq = self.generator.factorial(n)
            elif seq_key == "catalan":
                seq = self.generator.catalan(n)
            elif seq_key == "harmonic":
                seq = self.generator.harmonic(n)
                seq = [f"{x:.6f}" for x in seq]
            elif seq_key == "prime":
                seq = self.generator.prime(n)
            elif seq_key == "collatz":
                start = self.start_spin.value()
                seq = self.generator.collatz(start, n)
            elif seq_key == "custom":
                a, ok1 = QInputDialog.getInt(self, "Custom", "Enter first term (a):", 0, -1000000, 1000000)
                if not ok1: return
                b, ok2 = QInputDialog.getInt(self, "Custom", "Enter second term (b):", 1, -1000000, 1000000)
                if not ok2: return
                seq = self.generator.custom_linear(a, b, n)

            for i, val in enumerate(seq):
                output += f"[{i+1:3d}] → {val}\n"
            self.output_text.setPlainText(output)
            self.update_properties()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Generation failed: {str(e)}")

    def clear_all(self):
        self.output_text.clear()
        self.props_text.clear()

    def copy_output(self):
        text = self.output_text.toPlainText()
        if text:
            QApplication.clipboard().setText(text)
            self.statusBar().showMessage("Output copied to clipboard!", 3000)

    def export_to_file(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export Sequence", "", "Text Files (*.txt);;All Files (*)")
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.output_text.toPlainText())
                self.statusBar().showMessage(f"Exported to {path}", 5000)
            except Exception as e:
                QMessageBox.critical(self, "Export Failed", str(e))

    def update_properties(self):
        seq_key = self.get_current_sequence_key()
        props = sequence_properties.get(seq_key, {})
        lang_props = props.get(self.current_lang, props.get("en", {}))
        text = f"Properties of {self.seq_combo.currentText()}\n"
        text += "=" * 50 + "\n\n"
        if lang_props:
            text += f"Formula: {lang_props.get('formula', 'N/A')}\n\n"
            text += f"Closed Form: {lang_props.get('closed_form', 'N/A')}\n\n"
            text += f"Sum Formula: {lang_props.get('sum', 'N/A')}\n"
        else:
            text += "No detailed properties available.\n"
        self.props_text.setPlainText(text)

    def update_language(self, lang):
        rtl = translations[lang]["rtl"]
        direction = Qt.LayoutDirection.RightToLeft if rtl else Qt.LayoutDirection.LeftToRight
        self.setLayoutDirection(direction)
        self.retranslate_ui()

    def update_theme(self, theme):
        app = QApplication.instance()
        theme_functions = {
            "system": apply_system_theme,
            "light": apply_light_theme,
            "dark": apply_dark_theme,
            "red": apply_red_theme,
            "blue": apply_blue_theme,
            "green": apply_green_theme,
            "purple": apply_purple_theme,
            "orange": apply_orange_theme
        }
        func = theme_functions.get(theme, apply_system_theme)
        func(app)
        self.statusBar().showMessage(f"Theme changed to {theme.title()}", 2000)

    def retranslate_ui(self):
        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION}")
        self.generate_btn.setText(self.trans["generate"])
        self.clear_btn.setText(self.trans["clear"])
        self.copy_btn.setText(self.trans["copy"])
        self.export_btn.setText(self.trans["export"])
        self.start_label.setText(self.trans["start"])
        self.update_properties()

    def apply_theme(self, theme):
        self.update_theme(theme)

# ------------------- Application Entry -------------------
def main():
    # Removed High DPI attributes - PyQt6 handles it automatically
    # No need for AA_EnableHighDpiScaling or AA_UseHighDpiPixmaps

    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setOrganizationName("xAI Labs")

    # Apply system theme initially
    apply_system_theme(app)

    window = MathSequenceExplorer()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

