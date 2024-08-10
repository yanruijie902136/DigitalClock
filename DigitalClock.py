import sys

from PySide6.QtCore import QTime, QTimer, Slot
from PySide6.QtWidgets import QApplication, QLCDNumber


class DigitalClock(QLCDNumber):
    def __init__(self):
        super().__init__()
        self.setDigitCount(8)   # 6 digits and 2 colons.

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_time)
        self.timer.start(1000)  # Emit timeout signal every 1000 milliseconds.

        self.display_time()

    @Slot()
    def display_time(self):
        self.display(QTime.currentTime().toString("hh:mm:ss"))


def main():
    app = QApplication(sys.argv)

    clock = DigitalClock()
    clock.setWindowTitle("Digital Clock")
    clock.resize(1000, 240)
    clock.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
