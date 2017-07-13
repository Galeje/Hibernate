from cx_Freeze import setup, Executable

setup(name = 'Hibernate',
		version = '1.0',
		description = 'Hibernate your PC.',
		executables = [Executable("shutdown.py")])
