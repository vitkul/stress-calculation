from cx_Freeze import setup, Executable


setup(
    name='StaticcalMomentCulator',
    version=0.1,
    description="Moments,area,section calculator",
    executables = [Executable("calculator.py")]

)
