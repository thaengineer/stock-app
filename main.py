#!/usr/bin/env python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from time import sleep
import sys
from StockBrain import BrainStock


stock         = BrainStock()
stock.api_key = 'XNJN1FCL3284O9WT' # need to remove at some point

widgetCSS = """
    QMainWindow {
        background-color: #181C27;
    }

    QScrollBar {
        background-color: rgba(0, 0, 0, 0.0);
    }

    QScrollBar::handle {
        background-color: #758696;
    }

    QScrollBar::handle::pressed {
        background-color: #81C784;
    }

    QLineEdit {
        font-family: hack;
        font-size: 12px;
        color: #181C27;
        background-color: #D1D4DC;
    }

    QPushButton {
        font-family: hack;
        font-size: 12px;
        border-radius: 14px;
        background-color: #758696;
    }

    QPushButton:hover {
        background-color: #81C784;
    }

    QLabel {
        font-family: hack;
        font-size: 12px;
    }
"""


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(80, 100, 1280, 720)
        self.setMinimumSize(1280, 720)
        self.setWindowTitle("Stock Screener")
        self.setStyleSheet(widgetCSS)
        self.initUI()
        self.show()

    def initUI(self):
        self.textbox = QLineEdit(self)
        self.textbox.setText('')
        self.textbox.move(24, 12)
        self.textbox.resize(128, 28) # 12px font -> 17 chars
        self.textbox.setStyleSheet(widgetCSS)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Lookup")
        self.button.move(168, 12)
        self.button.resize(96, 28)
        self.button.setStyleSheet(widgetCSS)
        self.button.clicked.connect(self.button_handler)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('Symbol:')
        self.label1.setWordWrap(True)
        self.label1.move(24, 48)
        self.label1.resize(168, 28) # 12px font -> 17 chars
        self.label1.setStyleSheet(widgetCSS)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText('Open:')
        self.label2.setWordWrap(True)
        self.label2.move(24, 72)
        self.label2.resize(168, 28) # 12px font -> 17 chars
        self.label2.setStyleSheet(widgetCSS)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText('High:')
        self.label3.setWordWrap(True)
        self.label3.move(24, 96)
        self.label3.resize(168, 28) # 12px font -> 17 chars
        self.label3.setStyleSheet(widgetCSS)

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText('Low:')
        self.label4.setWordWrap(True)
        self.label4.move(24, 120)
        self.label4.resize(168, 28) # 12px font -> 17 chars
        self.label4.setStyleSheet(widgetCSS)

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setText('Close:')
        self.label5.setWordWrap(True)
        self.label5.move(24, 144)
        self.label5.resize(168, 28) # 12px font -> 17 chars
        self.label5.setStyleSheet(widgetCSS)

        self.label6 = QtWidgets.QLabel(self)
        self.label6.setText('Change:')
        self.label6.setWordWrap(True)
        self.label6.move(24, 168)
        self.label6.resize(168, 28) # 12px font -> 17 chars
        self.label6.setStyleSheet(widgetCSS)

        self.label7 = QtWidgets.QLabel(self)
        self.label7.setText('% Change:')
        self.label7.setWordWrap(True)
        self.label7.move(24, 192)
        self.label7.resize(168, 28) # 12px font -> 17 chars
        self.label7.setStyleSheet(widgetCSS)

        self.label8 = QtWidgets.QLabel(self)
        self.label8.setText('Bias:')
        self.label8.setWordWrap(True)
        self.label8.move(24, 216)
        self.label8.resize(168, 28) # 12px font -> 17 chars
        self.label8.setStyleSheet(widgetCSS)

        self.label9 = QtWidgets.QLabel(self)
        self.label9.setText('Call Strike:')
        self.label9.setWordWrap(True)
        self.label9.move(24, 240)
        self.label9.resize(168, 28) # 12px font -> 17 chars
        self.label9.setStyleSheet(widgetCSS)

        self.label10 = QtWidgets.QLabel(self)
        self.label10.setText('Put Strike:')
        self.label10.setWordWrap(True)
        self.label10.move(24, 264)
        self.label10.resize(168, 28) # 12px font -> 17 chars
        self.label10.setStyleSheet(widgetCSS)

    def button_handler(self):
        if self.textbox.text() == '':
            # stock.ticker = 'SPY'
            pass
        else:
            try:
                self.textbox.setText(self.textbox.text().upper())
                stock.ticker = self.textbox.text()
                stock.stockData()
                stock.getSentiment()
                stock.getStrikePrices()
                self.label1.setText(f'Symbol:      {stock.ticker}')
                self.label2.setText(f'Open:        {stock.open}')
                self.label3.setText(f'High:        {stock.high}')
                self.label4.setText(f'Low:         {stock.low}')
                self.label5.setText(f'Close:       {stock.close}')
                self.label6.setText(f'Change ($):  {stock.change:.2f}')
                self.label7.setText(f'Change (%):  {stock.pctchange:.2f}')
                #self.label8.setText(f'Bias:        {stock.sentiment}')
                self.label9.setText(f'Call Strike: {stock.callStrike:.2f}')
                self.label10.setText(f'Put Strike:  {stock.putStrike:.2f}')
            except:
                pass


app    = QApplication(sys.argv)
window = Window()

sys.exit(app.exec_())
