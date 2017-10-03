"""
mozDefrag cx_Freeze setup file
"""

from cx_Freeze import setup, Executable

setup(
    name="mozDefrag",
    version="0.1",
    description="defrag Firefox/Thunderbird's sqlite DB for users/profiles",
    executables=[Executable("mozDefrag.py")],
)
