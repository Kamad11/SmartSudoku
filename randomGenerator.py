"""Module containing random generator mode gui."""
from PyQt5 import QtCore, QtGui, QtWidgets
import sudukoSolver
from copy import deepcopy

style_sheet_1 = """QPushButton { background-color: #2B3A67;
                               color: #ffffff;
                               border-radius: 10px; }
QPushButton::hover { background-color: #ffffff;
                     color: #2B3A67;
                     border: 1px solid black; }
QPushButton::pressed { background-color: #000000;
                       color: #ffffff; }
QPushButton::disabled { background-color: #ffffff;
                        color: rgba(43, 58, 103, 0.5);
                        border: 1px solid black; }"""

style_sheet_2 = """QSpinBox { border: 2px solid black;
                              font-size: 25px;}
QSpinBox::disabled { background-color: rgba(0, 0, 0, 0.2);
                     color: #000000;}
QSpinBox::hover { background-color: #F76B8A; }"""


class Ui_RandomGenerator(object):
    def setupUi(self, RandomGenerator):
        RandomGenerator.setObjectName("RandomGenerator")
        RandomGenerator.resize(700, 700)
        RandomGenerator.setMinimumSize(QtCore.QSize(700, 700))
        RandomGenerator.setStyleSheet("background-color: #ffffff;")

        self.main_layout = QtWidgets.QGridLayout(RandomGenerator)
        self.main_layout.setContentsMargins(62, 10, 62, 10)
        self.main_layout.setSpacing(5)
        self.main_layout.setObjectName("main_layout")

        # option buttons ##################################################
        self.options = QtWidgets.QWidget(RandomGenerator)
        self.options.setMinimumSize(QtCore.QSize(0, 60))
        self.options.setStyleSheet(style_sheet_1)
        self.options.setObjectName("options")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.options_layout = QtWidgets.QGridLayout(self.options)
        self.options_layout.setObjectName("options_layout")

        # # reset #####
        self.reset_button = QtWidgets.QPushButton(self.options)
        self.reset_button.setMinimumSize(QtCore.QSize(0, 50))
        self.reset_button.setFont(font)
        self.reset_button.setObjectName("reset_button")
        self.options_layout.addWidget(self.reset_button, 0, 0, 1, 1)

        # # see solution #####
        self.solution_button = QtWidgets.QPushButton(self.options)
        self.solution_button.setMinimumSize(QtCore.QSize(0, 50))
        self.solution_button.setFont(font)
        self.solution_button.setObjectName("solution_button")
        self.options_layout.addWidget(self.solution_button, 0, 1, 1, 1)

        # # check solution #####
        self.check_solution_button = QtWidgets.QPushButton(self.options)
        self.check_solution_button.setMinimumSize(QtCore.QSize(0, 50))
        self.check_solution_button.setFont(font)
        self.check_solution_button.setObjectName("check_solution_button")
        self.options_layout.addWidget(self.check_solution_button, 0, 2, 1, 1)
        self.main_layout.addWidget(self.options, 1, 0, 1, 1)

        # board widget #####################################################
        self.sudoku_board = QtWidgets.QWidget(RandomGenerator)
        self.sudoku_board.setMinimumSize(QtCore.QSize(576, 576))
        self.sudoku_board.setStyleSheet(style_sheet_2)
        self.sudoku_board.setObjectName("sudoku_board")
        self.sudoku_board_layout = QtWidgets.QGridLayout(self.sudoku_board)
        self.sudoku_board_layout.setContentsMargins(10, 10, 10, 10)
        self.sudoku_board_layout.setSpacing(10)
        self.sudoku_board_layout.setObjectName("sudoku_board_layout")

        # # horizontal lines #####
        self.hl1 = QtWidgets.QFrame(self.sudoku_board)
        self.hl1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hl1.setLineWidth(5)
        self.hl1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hl1.setObjectName("hl1")
        self.sudoku_board_layout.addWidget(self.hl1, 3, 0, 1, 3)

        self.hl2 = QtWidgets.QFrame(self.sudoku_board)
        self.hl2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hl2.setLineWidth(5)
        self.hl2.setFrameShape(QtWidgets.QFrame.HLine)
        self.hl2.setObjectName("hl2")
        self.sudoku_board_layout.addWidget(self.hl2, 3, 4, 1, 3)

        self.hl3 = QtWidgets.QFrame(self.sudoku_board)
        self.hl3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hl3.setLineWidth(5)
        self.hl3.setFrameShape(QtWidgets.QFrame.HLine)
        self.hl3.setObjectName("hl3")
        self.sudoku_board_layout.addWidget(self.hl3, 3, 8, 1, 3)

        self.hl4 = QtWidgets.QFrame(self.sudoku_board)
        self.hl4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hl4.setLineWidth(5)
        self.hl4.setFrameShape(QtWidgets.QFrame.HLine)
        self.hl4.setObjectName("hl4")
        self.sudoku_board_layout.addWidget(self.hl4, 7, 0, 1, 3)

        self.hl5 = QtWidgets.QFrame(self.sudoku_board)
        self.hl5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hl5.setLineWidth(5)
        self.hl5.setFrameShape(QtWidgets.QFrame.HLine)
        self.hl5.setObjectName("hl5")
        self.sudoku_board_layout.addWidget(self.hl5, 7, 4, 1, 3)

        self.hl6 = QtWidgets.QFrame(self.sudoku_board)
        self.hl6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hl6.setLineWidth(5)
        self.hl6.setFrameShape(QtWidgets.QFrame.HLine)
        self.hl6.setObjectName("hl6")
        self.sudoku_board_layout.addWidget(self.hl6, 7, 8, 1, 3)

        # # vertical lines #####
        self.vl1 = QtWidgets.QFrame(self.sudoku_board)
        self.vl1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vl1.setLineWidth(5)
        self.vl1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vl1.setObjectName("vl1")
        self.sudoku_board_layout.addWidget(self.vl1, 0, 3, 3, 1)

        self.vl2 = QtWidgets.QFrame(self.sudoku_board)
        self.vl2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vl2.setLineWidth(5)
        self.vl2.setFrameShape(QtWidgets.QFrame.VLine)
        self.vl2.setObjectName("vl2")
        self.sudoku_board_layout.addWidget(self.vl2, 0, 7, 3, 1)

        self.vl3 = QtWidgets.QFrame(self.sudoku_board)
        self.vl3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vl3.setLineWidth(5)
        self.vl3.setFrameShape(QtWidgets.QFrame.VLine)
        self.vl3.setObjectName("vl3")
        self.sudoku_board_layout.addWidget(self.vl3, 4, 3, 3, 1)

        self.vl4 = QtWidgets.QFrame(self.sudoku_board)
        self.vl4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vl4.setLineWidth(5)
        self.vl4.setFrameShape(QtWidgets.QFrame.VLine)
        self.vl4.setObjectName("vl4")
        self.sudoku_board_layout.addWidget(self.vl4, 4, 7, 3, 1)

        self.vl5 = QtWidgets.QFrame(self.sudoku_board)
        self.vl5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vl5.setLineWidth(5)
        self.vl5.setFrameShape(QtWidgets.QFrame.VLine)
        self.vl5.setObjectName("vl5")
        self.sudoku_board_layout.addWidget(self.vl5, 8, 3, 3, 1)

        self.vl6 = QtWidgets.QFrame(self.sudoku_board)
        self.vl6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vl6.setLineWidth(5)
        self.vl6.setFrameShape(QtWidgets.QFrame.VLine)
        self.vl6.setObjectName("vl6")
        self.sudoku_board_layout.addWidget(self.vl6, 8, 7, 3, 1)

        # # boxes #####
        self.b1 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b1.setMinimumSize(QtCore.QSize(50, 50))
        self.b1.setAlignment(QtCore.Qt.AlignCenter)
        self.b1.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b1.setMinimum(0)
        self.b1.setMaximum(9)
        self.b1.setObjectName("b1")
        self.sudoku_board_layout.addWidget(self.b1, 0, 0, 1, 1)

        self.b2 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b2.setMinimumSize(QtCore.QSize(50, 50))
        self.b2.setAlignment(QtCore.Qt.AlignCenter)
        self.b2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b2.setMinimum(0)
        self.b2.setMaximum(9)
        self.b2.setObjectName("b2")
        self.sudoku_board_layout.addWidget(self.b2, 0, 1, 1, 1)

        self.b3 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b3.setMinimumSize(QtCore.QSize(50, 50))
        self.b3.setAlignment(QtCore.Qt.AlignCenter)
        self.b3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b3.setMinimum(0)
        self.b3.setMaximum(9)
        self.b3.setObjectName("b3")
        self.sudoku_board_layout.addWidget(self.b3, 0, 2, 1, 1)

        self.b4 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b4.setMinimumSize(QtCore.QSize(50, 50))
        self.b4.setAlignment(QtCore.Qt.AlignCenter)
        self.b4.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b4.setMinimum(0)
        self.b4.setMaximum(9)
        self.b4.setObjectName("b4")
        self.sudoku_board_layout.addWidget(self.b4, 0, 4, 1, 1)

        self.b5 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b5.setMinimumSize(QtCore.QSize(50, 50))
        self.b5.setAlignment(QtCore.Qt.AlignCenter)
        self.b5.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b5.setMinimum(0)
        self.b5.setMaximum(9)
        self.b5.setObjectName("b5")
        self.sudoku_board_layout.addWidget(self.b5, 0, 5, 1, 1)

        self.b6 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b6.setMinimumSize(QtCore.QSize(50, 50))
        self.b6.setAlignment(QtCore.Qt.AlignCenter)
        self.b6.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b6.setMinimum(0)
        self.b6.setMaximum(9)
        self.b6.setObjectName("b6")
        self.sudoku_board_layout.addWidget(self.b6, 0, 6, 1, 1)

        self.b7 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b7.setMinimumSize(QtCore.QSize(50, 50))
        self.b7.setAlignment(QtCore.Qt.AlignCenter)
        self.b7.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b7.setMinimum(0)
        self.b7.setMaximum(9)
        self.b7.setObjectName("b7")
        self.sudoku_board_layout.addWidget(self.b7, 0, 8, 1, 1)

        self.b8 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b8.setMinimumSize(QtCore.QSize(50, 50))
        self.b8.setAlignment(QtCore.Qt.AlignCenter)
        self.b8.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b8.setMinimum(0)
        self.b8.setMaximum(9)
        self.b8.setObjectName("b8")
        self.sudoku_board_layout.addWidget(self.b8, 0, 9, 1, 1)

        self.b9 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b9.setMinimumSize(QtCore.QSize(50, 50))
        self.b9.setAlignment(QtCore.Qt.AlignCenter)
        self.b9.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b9.setMinimum(0)
        self.b9.setMaximum(9)
        self.b9.setObjectName("b9")
        self.sudoku_board_layout.addWidget(self.b9, 0, 10, 1, 1)

        self.b10 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b10.setMinimumSize(QtCore.QSize(50, 50))
        self.b10.setAlignment(QtCore.Qt.AlignCenter)
        self.b10.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b10.setMinimum(0)
        self.b10.setMaximum(9)
        self.b10.setObjectName("b10")
        self.sudoku_board_layout.addWidget(self.b10, 1, 0, 1, 1)

        self.b11 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b11.setMinimumSize(QtCore.QSize(50, 50))
        self.b11.setAlignment(QtCore.Qt.AlignCenter)
        self.b11.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b11.setMinimum(0)
        self.b11.setMaximum(9)
        self.b11.setObjectName("b11")
        self.sudoku_board_layout.addWidget(self.b11, 1, 1, 1, 1)

        self.b12 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b12.setMinimumSize(QtCore.QSize(50, 50))
        self.b12.setAlignment(QtCore.Qt.AlignCenter)
        self.b12.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b12.setMinimum(0)
        self.b12.setMaximum(9)
        self.b12.setObjectName("b12")
        self.sudoku_board_layout.addWidget(self.b12, 1, 2, 1, 1)

        self.b13 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b13.setMinimumSize(QtCore.QSize(50, 50))
        self.b13.setAlignment(QtCore.Qt.AlignCenter)
        self.b13.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b13.setMinimum(0)
        self.b13.setMaximum(9)
        self.b13.setObjectName("b13")
        self.sudoku_board_layout.addWidget(self.b13, 1, 4, 1, 1)

        self.b14 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b14.setMinimumSize(QtCore.QSize(50, 50))
        self.b14.setAlignment(QtCore.Qt.AlignCenter)
        self.b14.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b14.setMinimum(0)
        self.b14.setMaximum(9)
        self.b14.setObjectName("b14")
        self.sudoku_board_layout.addWidget(self.b14, 1, 5, 1, 1)

        self.b15 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b15.setMinimumSize(QtCore.QSize(50, 50))
        self.b15.setAlignment(QtCore.Qt.AlignCenter)
        self.b15.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b15.setMinimum(0)
        self.b15.setMaximum(9)
        self.b15.setObjectName("b15")
        self.sudoku_board_layout.addWidget(self.b15, 1, 6, 1, 1)

        self.b16 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b16.setMinimumSize(QtCore.QSize(50, 50))
        self.b16.setAlignment(QtCore.Qt.AlignCenter)
        self.b16.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b16.setMinimum(0)
        self.b16.setMaximum(9)
        self.b16.setObjectName("b16")
        self.sudoku_board_layout.addWidget(self.b16, 1, 8, 1, 1)

        self.b17 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b17.setMinimumSize(QtCore.QSize(50, 50))
        self.b17.setAlignment(QtCore.Qt.AlignCenter)
        self.b17.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b17.setMinimum(0)
        self.b17.setMaximum(9)
        self.b17.setObjectName("b17")
        self.sudoku_board_layout.addWidget(self.b17, 1, 9, 1, 1)

        self.b18 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b18.setMinimumSize(QtCore.QSize(50, 50))
        self.b18.setAlignment(QtCore.Qt.AlignCenter)
        self.b18.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b18.setMinimum(0)
        self.b18.setMaximum(9)
        self.b18.setObjectName("b18")
        self.sudoku_board_layout.addWidget(self.b18, 1, 10, 1, 1)

        self.b19 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b19.setMinimumSize(QtCore.QSize(50, 50))
        self.b19.setAlignment(QtCore.Qt.AlignCenter)
        self.b19.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b19.setMinimum(0)
        self.b19.setMaximum(9)
        self.b19.setObjectName("b19")
        self.sudoku_board_layout.addWidget(self.b19, 2, 0, 1, 1)

        self.b20 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b20.setMinimumSize(QtCore.QSize(50, 50))
        self.b20.setAlignment(QtCore.Qt.AlignCenter)
        self.b20.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b20.setMinimum(0)
        self.b20.setMaximum(9)
        self.b20.setObjectName("b20")
        self.sudoku_board_layout.addWidget(self.b20, 2, 1, 1, 1)

        self.b21 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b21.setMinimumSize(QtCore.QSize(50, 50))
        self.b21.setAlignment(QtCore.Qt.AlignCenter)
        self.b21.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b21.setMinimum(0)
        self.b21.setMaximum(9)
        self.b21.setObjectName("b21")
        self.sudoku_board_layout.addWidget(self.b21, 2, 2, 1, 1)

        self.b22 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b22.setMinimumSize(QtCore.QSize(50, 50))
        self.b22.setAlignment(QtCore.Qt.AlignCenter)
        self.b22.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b22.setMinimum(0)
        self.b22.setMaximum(9)
        self.b22.setObjectName("b22")
        self.sudoku_board_layout.addWidget(self.b22, 2, 4, 1, 1)

        self.b23 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b23.setMinimumSize(QtCore.QSize(50, 50))
        self.b23.setAlignment(QtCore.Qt.AlignCenter)
        self.b23.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b23.setMinimum(0)
        self.b23.setMaximum(9)
        self.b23.setObjectName("b23")
        self.sudoku_board_layout.addWidget(self.b23, 2, 5, 1, 1)

        self.b24 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b24.setMinimumSize(QtCore.QSize(50, 50))
        self.b24.setAlignment(QtCore.Qt.AlignCenter)
        self.b24.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b24.setMinimum(0)
        self.b24.setMaximum(9)
        self.b24.setObjectName("b24")
        self.sudoku_board_layout.addWidget(self.b24, 2, 6, 1, 1)

        self.b25 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b25.setMinimumSize(QtCore.QSize(50, 50))
        self.b25.setAlignment(QtCore.Qt.AlignCenter)
        self.b25.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b25.setMinimum(0)
        self.b25.setMaximum(9)
        self.b25.setObjectName("b25")
        self.sudoku_board_layout.addWidget(self.b25, 2, 8, 1, 1)

        self.b26 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b26.setMinimumSize(QtCore.QSize(50, 50))
        self.b26.setAlignment(QtCore.Qt.AlignCenter)
        self.b26.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b26.setMinimum(0)
        self.b26.setMaximum(9)
        self.b26.setObjectName("b26")
        self.sudoku_board_layout.addWidget(self.b26, 2, 9, 1, 1)

        self.b27 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b27.setMinimumSize(QtCore.QSize(50, 50))
        self.b27.setAlignment(QtCore.Qt.AlignCenter)
        self.b27.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b27.setMinimum(0)
        self.b27.setMaximum(9)
        self.b27.setObjectName("b27")
        self.sudoku_board_layout.addWidget(self.b27, 2, 10, 1, 1)

        self.b28 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b28.setMinimumSize(QtCore.QSize(50, 50))
        self.b28.setAlignment(QtCore.Qt.AlignCenter)
        self.b28.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b28.setMinimum(0)
        self.b28.setMaximum(9)
        self.b28.setObjectName("b28")
        self.sudoku_board_layout.addWidget(self.b28, 4, 0, 1, 1)

        self.b29 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b29.setMinimumSize(QtCore.QSize(50, 50))
        self.b29.setAlignment(QtCore.Qt.AlignCenter)
        self.b29.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b29.setMinimum(0)
        self.b29.setMaximum(9)
        self.b29.setObjectName("b29")
        self.sudoku_board_layout.addWidget(self.b29, 4, 1, 1, 1)

        self.b30 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b30.setMinimumSize(QtCore.QSize(50, 50))
        self.b30.setAlignment(QtCore.Qt.AlignCenter)
        self.b30.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b30.setMinimum(0)
        self.b30.setMaximum(9)
        self.b30.setObjectName("b30")
        self.sudoku_board_layout.addWidget(self.b30, 4, 2, 1, 1)

        self.b31 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b31.setMinimumSize(QtCore.QSize(50, 50))
        self.b31.setAlignment(QtCore.Qt.AlignCenter)
        self.b31.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b31.setMinimum(0)
        self.b31.setMaximum(9)
        self.b31.setObjectName("b31")
        self.sudoku_board_layout.addWidget(self.b31, 4, 4, 1, 1)

        self.b32 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b32.setMinimumSize(QtCore.QSize(50, 50))
        self.b32.setAlignment(QtCore.Qt.AlignCenter)
        self.b32.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b32.setMinimum(0)
        self.b32.setMaximum(9)
        self.b32.setObjectName("b32")
        self.sudoku_board_layout.addWidget(self.b32, 4, 5, 1, 1)

        self.b33 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b33.setMinimumSize(QtCore.QSize(50, 50))
        self.b33.setAlignment(QtCore.Qt.AlignCenter)
        self.b33.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b33.setMinimum(0)
        self.b33.setMaximum(9)
        self.b33.setObjectName("b33")
        self.sudoku_board_layout.addWidget(self.b33, 4, 6, 1, 1)

        self.b34 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b34.setMinimumSize(QtCore.QSize(50, 50))
        self.b34.setAlignment(QtCore.Qt.AlignCenter)
        self.b34.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b34.setMinimum(0)
        self.b34.setMaximum(9)
        self.b34.setObjectName("b34")
        self.sudoku_board_layout.addWidget(self.b34, 4, 8, 1, 1)

        self.b35 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b35.setMinimumSize(QtCore.QSize(50, 50))
        self.b35.setAlignment(QtCore.Qt.AlignCenter)
        self.b35.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b35.setMinimum(0)
        self.b35.setMaximum(9)
        self.b35.setObjectName("b35")
        self.sudoku_board_layout.addWidget(self.b35, 4, 9, 1, 1)

        self.b36 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b36.setMinimumSize(QtCore.QSize(50, 50))
        self.b36.setAlignment(QtCore.Qt.AlignCenter)
        self.b36.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b36.setMinimum(0)
        self.b36.setMaximum(9)
        self.b36.setObjectName("b36")
        self.sudoku_board_layout.addWidget(self.b36, 4, 10, 1, 1)

        self.b37 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b37.setMinimumSize(QtCore.QSize(50, 50))
        self.b37.setAlignment(QtCore.Qt.AlignCenter)
        self.b37.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b37.setMinimum(0)
        self.b37.setMaximum(9)
        self.b37.setObjectName("b37")
        self.sudoku_board_layout.addWidget(self.b37, 5, 0, 1, 1)

        self.b38 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b38.setMinimumSize(QtCore.QSize(50, 50))
        self.b38.setAlignment(QtCore.Qt.AlignCenter)
        self.b38.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b38.setMinimum(0)
        self.b38.setMaximum(9)
        self.b38.setObjectName("b38")
        self.sudoku_board_layout.addWidget(self.b38, 5, 1, 1, 1)

        self.b39 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b39.setMinimumSize(QtCore.QSize(50, 50))
        self.b39.setAlignment(QtCore.Qt.AlignCenter)
        self.b39.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b39.setMinimum(0)
        self.b39.setMaximum(9)
        self.b39.setObjectName("b39")
        self.sudoku_board_layout.addWidget(self.b39, 5, 2, 1, 1)

        self.b40 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b40.setMinimumSize(QtCore.QSize(50, 50))
        self.b40.setAlignment(QtCore.Qt.AlignCenter)
        self.b40.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b40.setMinimum(0)
        self.b40.setMaximum(9)
        self.b40.setObjectName("b40")
        self.sudoku_board_layout.addWidget(self.b40, 5, 4, 1, 1)

        self.b41 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b41.setMinimumSize(QtCore.QSize(50, 50))
        self.b41.setAlignment(QtCore.Qt.AlignCenter)
        self.b41.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b41.setMinimum(0)
        self.b41.setMaximum(9)
        self.b41.setObjectName("b41")
        self.sudoku_board_layout.addWidget(self.b41, 5, 5, 1, 1)

        self.b42 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b42.setMinimumSize(QtCore.QSize(50, 50))
        self.b42.setAlignment(QtCore.Qt.AlignCenter)
        self.b42.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b42.setMinimum(0)
        self.b42.setMaximum(9)
        self.b42.setObjectName("b42")
        self.sudoku_board_layout.addWidget(self.b42, 5, 6, 1, 1)

        self.b43 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b43.setMinimumSize(QtCore.QSize(50, 50))
        self.b43.setAlignment(QtCore.Qt.AlignCenter)
        self.b43.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b43.setMinimum(0)
        self.b43.setMaximum(9)
        self.b43.setObjectName("b43")
        self.sudoku_board_layout.addWidget(self.b43, 5, 8, 1, 1)

        self.b44 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b44.setMinimumSize(QtCore.QSize(50, 50))
        self.b44.setAlignment(QtCore.Qt.AlignCenter)
        self.b44.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b44.setMinimum(0)
        self.b44.setMaximum(9)
        self.b44.setObjectName("b44")
        self.sudoku_board_layout.addWidget(self.b44, 5, 9, 1, 1)

        self.b45 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b45.setMinimumSize(QtCore.QSize(50, 50))
        self.b45.setAlignment(QtCore.Qt.AlignCenter)
        self.b45.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b45.setMinimum(0)
        self.b45.setMaximum(9)
        self.b45.setObjectName("b45")
        self.sudoku_board_layout.addWidget(self.b45, 5, 10, 1, 1)

        self.b46 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b46.setMinimumSize(QtCore.QSize(50, 50))
        self.b46.setAlignment(QtCore.Qt.AlignCenter)
        self.b46.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b46.setMinimum(0)
        self.b46.setMaximum(9)
        self.b46.setObjectName("b46")
        self.sudoku_board_layout.addWidget(self.b46, 6, 0, 1, 1)

        self.b47 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b47.setMinimumSize(QtCore.QSize(50, 50))
        self.b47.setAlignment(QtCore.Qt.AlignCenter)
        self.b47.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b47.setMinimum(0)
        self.b47.setMaximum(9)
        self.b47.setObjectName("b47")
        self.sudoku_board_layout.addWidget(self.b47, 6, 1, 1, 1)

        self.b48 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b48.setMinimumSize(QtCore.QSize(50, 50))
        self.b48.setAlignment(QtCore.Qt.AlignCenter)
        self.b48.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b48.setMinimum(0)
        self.b48.setMaximum(9)
        self.b48.setObjectName("b48")
        self.sudoku_board_layout.addWidget(self.b48, 6, 2, 1, 1)

        self.b49 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b49.setMinimumSize(QtCore.QSize(50, 50))
        self.b49.setAlignment(QtCore.Qt.AlignCenter)
        self.b49.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b49.setMinimum(0)
        self.b49.setMaximum(9)
        self.b49.setObjectName("b49")
        self.sudoku_board_layout.addWidget(self.b49, 6, 4, 1, 1)

        self.b50 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b50.setMinimumSize(QtCore.QSize(50, 50))
        self.b50.setAlignment(QtCore.Qt.AlignCenter)
        self.b50.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b50.setMinimum(0)
        self.b50.setMaximum(9)
        self.b50.setObjectName("b50")
        self.sudoku_board_layout.addWidget(self.b50, 6, 5, 1, 1)
        self.main_layout.addWidget(self.sudoku_board, 0, 0, 1, 1)

        self.b51 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b51.setMinimumSize(QtCore.QSize(50, 50))
        self.b51.setAlignment(QtCore.Qt.AlignCenter)
        self.b51.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b51.setMinimum(0)
        self.b51.setMaximum(9)
        self.b51.setObjectName("b51")
        self.sudoku_board_layout.addWidget(self.b51, 6, 6, 1, 1)

        self.b52 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b52.setMinimumSize(QtCore.QSize(50, 50))
        self.b52.setAlignment(QtCore.Qt.AlignCenter)
        self.b52.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b52.setMinimum(0)
        self.b52.setMaximum(9)
        self.b52.setObjectName("b52")
        self.sudoku_board_layout.addWidget(self.b52, 6, 8, 1, 1)

        self.b53 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b53.setMinimumSize(QtCore.QSize(50, 50))
        self.b53.setAlignment(QtCore.Qt.AlignCenter)
        self.b53.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b53.setMinimum(0)
        self.b53.setMaximum(9)
        self.b53.setObjectName("b53")
        self.sudoku_board_layout.addWidget(self.b53, 6, 9, 1, 1)

        self.b54 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b54.setMinimumSize(QtCore.QSize(50, 50))
        self.b54.setAlignment(QtCore.Qt.AlignCenter)
        self.b54.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b54.setMinimum(0)
        self.b54.setMaximum(9)
        self.b54.setObjectName("b54")
        self.sudoku_board_layout.addWidget(self.b54, 6, 10, 1, 1)

        self.b55 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b55.setMinimumSize(QtCore.QSize(50, 50))
        self.b55.setAlignment(QtCore.Qt.AlignCenter)
        self.b55.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b55.setMinimum(0)
        self.b55.setMaximum(9)
        self.b55.setObjectName("b55")
        self.sudoku_board_layout.addWidget(self.b55, 8, 0, 1, 1)

        self.b56 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b56.setMinimumSize(QtCore.QSize(50, 50))
        self.b56.setAlignment(QtCore.Qt.AlignCenter)
        self.b56.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b56.setMinimum(0)
        self.b56.setMaximum(9)
        self.b56.setObjectName("b56")
        self.sudoku_board_layout.addWidget(self.b56, 8, 1, 1, 1)

        self.b57 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b57.setMinimumSize(QtCore.QSize(50, 50))
        self.b57.setAlignment(QtCore.Qt.AlignCenter)
        self.b57.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b57.setMinimum(0)
        self.b57.setMaximum(9)
        self.b57.setObjectName("b57")
        self.sudoku_board_layout.addWidget(self.b57, 8, 2, 1, 1)

        self.b58 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b58.setMinimumSize(QtCore.QSize(50, 50))
        self.b58.setAlignment(QtCore.Qt.AlignCenter)
        self.b58.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b58.setMinimum(0)
        self.b58.setMaximum(9)
        self.b58.setObjectName("b58")
        self.sudoku_board_layout.addWidget(self.b58, 8, 4, 1, 1)

        self.b59 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b59.setMinimumSize(QtCore.QSize(50, 50))
        self.b59.setAlignment(QtCore.Qt.AlignCenter)
        self.b59.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b59.setMinimum(0)
        self.b59.setMaximum(9)
        self.b59.setObjectName("b59")
        self.sudoku_board_layout.addWidget(self.b59, 8, 5, 1, 1)

        self.b60 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b60.setMinimumSize(QtCore.QSize(50, 50))
        self.b60.setAlignment(QtCore.Qt.AlignCenter)
        self.b60.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b60.setMinimum(0)
        self.b60.setMaximum(9)
        self.b60.setObjectName("b60")
        self.sudoku_board_layout.addWidget(self.b60, 8, 6, 1, 1)

        self.b61 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b61.setMinimumSize(QtCore.QSize(50, 50))
        self.b61.setAlignment(QtCore.Qt.AlignCenter)
        self.b61.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b61.setMinimum(0)
        self.b61.setMaximum(9)
        self.b61.setObjectName("b61")
        self.sudoku_board_layout.addWidget(self.b61, 8, 8, 1, 1)

        self.b62 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b62.setMinimumSize(QtCore.QSize(50, 50))
        self.b62.setAlignment(QtCore.Qt.AlignCenter)
        self.b62.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b62.setMinimum(0)
        self.b62.setMaximum(9)
        self.b62.setObjectName("b62")
        self.sudoku_board_layout.addWidget(self.b62, 8, 9, 1, 1)

        self.b63 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b63.setMinimumSize(QtCore.QSize(50, 50))
        self.b63.setAlignment(QtCore.Qt.AlignCenter)
        self.b63.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b63.setMinimum(0)
        self.b63.setMaximum(9)
        self.b63.setObjectName("b63")
        self.sudoku_board_layout.addWidget(self.b63, 8, 10, 1, 1)

        self.b64 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b64.setMinimumSize(QtCore.QSize(50, 50))
        self.b64.setAlignment(QtCore.Qt.AlignCenter)
        self.b64.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b64.setMinimum(0)
        self.b64.setMaximum(9)
        self.b64.setObjectName("b64")
        self.sudoku_board_layout.addWidget(self.b64, 9, 0, 1, 1)

        self.b65 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b65.setMinimumSize(QtCore.QSize(50, 50))
        self.b65.setAlignment(QtCore.Qt.AlignCenter)
        self.b65.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b65.setMinimum(0)
        self.b65.setMaximum(9)
        self.b65.setObjectName("b65")
        self.sudoku_board_layout.addWidget(self.b65, 9, 1, 1, 1)

        self.b66 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b66.setMinimumSize(QtCore.QSize(50, 50))
        self.b66.setAlignment(QtCore.Qt.AlignCenter)
        self.b66.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b66.setMinimum(0)
        self.b66.setMaximum(9)
        self.b66.setObjectName("b66")
        self.sudoku_board_layout.addWidget(self.b66, 9, 2, 1, 1)

        self.b67 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b67.setMinimumSize(QtCore.QSize(50, 50))
        self.b67.setAlignment(QtCore.Qt.AlignCenter)
        self.b67.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b67.setMinimum(0)
        self.b67.setMaximum(9)
        self.b67.setObjectName("b67")
        self.sudoku_board_layout.addWidget(self.b67, 9, 4, 1, 1)

        self.b68 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b68.setMinimumSize(QtCore.QSize(50, 50))
        self.b68.setAlignment(QtCore.Qt.AlignCenter)
        self.b68.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b68.setMinimum(0)
        self.b68.setMaximum(9)
        self.b68.setObjectName("b68")
        self.sudoku_board_layout.addWidget(self.b68, 9, 5, 1, 1)

        self.b69 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b69.setMinimumSize(QtCore.QSize(50, 50))
        self.b69.setAlignment(QtCore.Qt.AlignCenter)
        self.b69.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b69.setMinimum(0)
        self.b69.setMaximum(9)
        self.b69.setObjectName("b69")
        self.sudoku_board_layout.addWidget(self.b69, 9, 6, 1, 1)

        self.b70 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b70.setMinimumSize(QtCore.QSize(50, 50))
        self.b70.setAlignment(QtCore.Qt.AlignCenter)
        self.b70.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b70.setMinimum(0)
        self.b70.setMaximum(9)
        self.b70.setObjectName("b70")
        self.sudoku_board_layout.addWidget(self.b70, 9, 8, 1, 1)

        self.b71 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b71.setMinimumSize(QtCore.QSize(50, 50))
        self.b71.setAlignment(QtCore.Qt.AlignCenter)
        self.b71.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b71.setMinimum(0)
        self.b71.setMaximum(9)
        self.b71.setObjectName("b71")
        self.sudoku_board_layout.addWidget(self.b71, 9, 9, 1, 1)

        self.b72 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b72.setMinimumSize(QtCore.QSize(50, 50))
        self.b72.setAlignment(QtCore.Qt.AlignCenter)
        self.b72.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b72.setMinimum(0)
        self.b72.setMaximum(9)
        self.b72.setObjectName("b72")
        self.sudoku_board_layout.addWidget(self.b72, 9, 10, 1, 1)

        self.b73 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b73.setMinimumSize(QtCore.QSize(50, 50))
        self.b73.setAlignment(QtCore.Qt.AlignCenter)
        self.b73.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b73.setMinimum(0)
        self.b73.setMaximum(9)
        self.b73.setObjectName("b73")
        self.sudoku_board_layout.addWidget(self.b73, 10, 0, 1, 1)

        self.b74 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b74.setMinimumSize(QtCore.QSize(50, 50))
        self.b74.setAlignment(QtCore.Qt.AlignCenter)
        self.b74.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b74.setMinimum(0)
        self.b74.setMaximum(9)
        self.b74.setObjectName("b74")
        self.sudoku_board_layout.addWidget(self.b74, 10, 1, 1, 1)

        self.b75 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b75.setMinimumSize(QtCore.QSize(50, 50))
        self.b75.setAlignment(QtCore.Qt.AlignCenter)
        self.b75.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b75.setMinimum(0)
        self.b75.setMaximum(9)
        self.b75.setObjectName("b75")
        self.sudoku_board_layout.addWidget(self.b75, 10, 2, 1, 1)

        self.b76 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b76.setMinimumSize(QtCore.QSize(50, 50))
        self.b76.setAlignment(QtCore.Qt.AlignCenter)
        self.b76.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b76.setMinimum(0)
        self.b76.setMaximum(9)
        self.b76.setObjectName("b76")
        self.sudoku_board_layout.addWidget(self.b76, 10, 4, 1, 1)

        self.b77 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b77.setMinimumSize(QtCore.QSize(50, 50))
        self.b77.setAlignment(QtCore.Qt.AlignCenter)
        self.b77.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b77.setMinimum(0)
        self.b77.setMaximum(9)
        self.b77.setObjectName("b77")
        self.sudoku_board_layout.addWidget(self.b77, 10, 5, 1, 1)

        self.b78 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b78.setMinimumSize(QtCore.QSize(50, 50))
        self.b78.setAlignment(QtCore.Qt.AlignCenter)
        self.b78.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b78.setMinimum(0)
        self.b78.setMaximum(9)
        self.b78.setObjectName("b78")
        self.sudoku_board_layout.addWidget(self.b78, 10, 6, 1, 1)

        self.b79 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b79.setMinimumSize(QtCore.QSize(50, 50))
        self.b79.setAlignment(QtCore.Qt.AlignCenter)
        self.b79.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b79.setMinimum(0)
        self.b79.setMaximum(9)
        self.b79.setObjectName("b79")
        self.sudoku_board_layout.addWidget(self.b79, 10, 8, 1, 1)

        self.b80 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b80.setMinimumSize(QtCore.QSize(50, 50))
        self.b80.setAlignment(QtCore.Qt.AlignCenter)
        self.b80.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b80.setMinimum(0)
        self.b80.setMaximum(9)
        self.b80.setObjectName("b80")
        self.sudoku_board_layout.addWidget(self.b80, 10, 9, 1, 1)

        self.b81 = QtWidgets.QSpinBox(self.sudoku_board)
        self.b81.setMinimumSize(QtCore.QSize(50, 50))
        self.b81.setAlignment(QtCore.Qt.AlignCenter)
        self.b81.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.b81.setMinimum(0)
        self.b81.setMaximum(9)
        self.b81.setObjectName("b81")
        self.sudoku_board_layout.addWidget(self.b81, 10, 10, 1, 1)

        # global variables ############################################################
        self.start_board = [[0 for x in range(9)] for y in range(9)]
        self.solution = [[0 for x in range(9)] for y in range(9)]

        self.board = [
            [self.b1, self.b2, self.b3, self.b4, self.b5,
                self.b6, self.b7, self.b8, self.b9],
            [self.b10, self.b11, self.b12, self.b13, self.b14,
                self.b15, self.b16, self.b17, self.b18],
            [self.b19, self.b20, self.b21, self.b22, self.b23,
                self.b24, self.b25, self.b26, self.b27],
            [self.b28, self.b29, self.b30, self.b31, self.b32,
                self.b33, self.b34, self.b35, self.b36],
            [self.b37, self.b38, self.b39, self.b40, self.b41,
                self.b42, self.b43, self.b44, self.b45],
            [self.b46, self.b47, self.b48, self.b49, self.b50,
                self.b51, self.b52, self.b53, self.b54],
            [self.b55, self.b56, self.b57, self.b58, self.b59,
                self.b60, self.b61, self.b62, self.b63],
            [self.b64, self.b65, self.b66, self.b67, self.b68,
                self.b69, self.b70, self.b71, self.b72],
            [self.b73, self.b74, self.b75, self.b76, self.b77,
                self.b78, self.b79, self.b80, self.b81]
        ]

        self.retranslateUi(RandomGenerator)
        QtCore.QMetaObject.connectSlotsByName(RandomGenerator)

    def retranslateUi(self, RandomGenerator):
        _translate = QtCore.QCoreApplication.translate

        self.generate_board()

        self.reset_button.setText(_translate("RandomGenerator", "Reset Game"))
        self.reset_button.clicked.connect(lambda: self.reset_board())

        self.solution_button.setText(_translate(
            "RandomGenerator", "Show Solution"))
        self.solution_button.clicked.connect(lambda: self.solve_board())

        self.check_solution_button.setText(
            _translate("RandomGenerator", "Check Solution"))
        self.check_solution_button.clicked.connect(
            lambda: self.check_solution())

    def generate_board(self):
        """Generate a random solvable board."""
        for i in range(9):
            for j in range(9):
                self.start_board[i][j] = 0

        self.start_board = sudukoSolver.make_sudoku(self.start_board)
        self.solution = deepcopy(self.start_board)

        try:
            sudukoSolver.solve(self.solution)
            for i in range(9):
                for j in range(9):
                    if self.solution[i][j] == 0:
                        self.generate_board()
        except:
            pass

        for i in range(9):
            for j in range(9):
                self.board[i][j].setValue(self.start_board[i][j])
                if self.board[i][j].value() != 0:
                    self.board[i][j].setDisabled(True)

    def reset_board(self):
        """Reset to start board."""
        for i in range(9):
            for j in range(9):
                self.board[i][j].setValue(self.start_board[i][j])
                if self.board[i][j].value() != 0:
                    self.board[i][j].setDisabled(True)

    def check_solution(self):
        """Check user's solution."""
        for i in range(9):
            for j in range(9):
                if self.board[i][j].value() != self.solution[i][j]:
                    self.check_solution_button.setText("Try Again!")
                    return
        self.check_solution_button.setText("You've solved it!")
        self.solve_board()

    def solve_board(self):
        """Solve the board."""
        self.check_solution_button.setDisabled(True)
        self.reset_button.setDisabled(True)
        self.solution_button.setDisabled(True)
        for i in range(9):
            for j in range(9):
                self.board[i][j].setValue(self.solution[i][j])
                self.board[i][j].setDisabled(True)
