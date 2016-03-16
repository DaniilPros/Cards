import cx_Freeze
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Source.py")]

cx_Freeze.setup(
    name='Cards',
    options={"build_exe": {"include_files": ["img\\1.ico", "img\\1.png",
                                             "img\\2.png",
                                             "img\\3.png",
                                             "img\\4.png",
                                             "img\\5.png",
                                             "img\\6.png",
                                             "img\\7.png",
                                             "img\\8.png",
                                             "img\\9.png",
                                             "img\\10.png",
                                             "img\\11.png",
                                             "img\\12.png",
                                             "img\\13.png",
                                             "img\\14.png",
                                             "img\\15.png",
                                             "img\\16.png",
                                             "img\\17.png",
                                             "img\\18.png",
                                             "img\\19.png",
                                             "img\\20.png",
                                             "img\\21.png",
                                             "img\\22.png",
                                             "img\\inside.png"]}},
    executables=executables)

"""
                           "include_files": ["img\\1.ico", "img\\1.png",
                                             "img\\2.png",
                                             "img\\3.png",
                                             "img\\4.png",
                                             "img\\5.png",
                                             "img\\6.png",
                                             "img\\7.png",
                                             "img\\8.png",
                                             "img\\9.png",
                                             "img\\10.png",
                                             "img\\11.png",
                                             "img\\12.png",
                                             "img\\13.png",
                                             "img\\14.png",
                                             "img\\15.png",
                                             "img\\16.png",
                                             "img\\17.png",
                                             "img\\18.png",
                                             "img\\19.png",
                                             "img\\20.png",
                                             "img\\21.png",
                                             "img\\22.png",
                                             "img\\inside.png"]
                                             """

