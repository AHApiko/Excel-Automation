#I use CxFreeze to share it with my colleagues

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("employees.py", base=base)]

packages = ["idna", "tkinter", "re", "pandas"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<BBDD>",
    options = options,
    version = "1.0",
    description = 'First try',
    executables = executables
)