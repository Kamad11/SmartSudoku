from cx_Freeze import setup, Executable

setup(name = "Smart Sudoku",
      version = "1.0.0",
      description = "",
      executables = [Executable("mainWindow.py")])
