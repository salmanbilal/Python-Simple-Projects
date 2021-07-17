
"""
About:
Date : 23/06/2021
Author : Salman Bilal
https://www.twitter.com/SalmanB34055398
"""

# TXT module

from os import path

# Create File
try:
    def createFile(file_name):
        if path.exists(file_name) is False:
            with open(file_name, "w") as create_:
                pass
        elif path.exists(file_name) is True:
            raise ValueError("File already Exists")

except Exception as NotCreating:
    print(NotCreating)

# Writing Line
try:
    class writeOrAppend:
        def writeln(FileName, line):
            if path.exists(FileName) is True:
                with open(FileName, "a") as write_:
                    _write_ = f"{line}\n"
                    write_.write(_write_)
            elif path.exists(FileName) is False:
                raise ValueError("No file Found")
        def appendln(FileName, line):
            if path.exists(FileName) is True:
                with open(FileName, "a") as append_:
                    _append_ = f"{line}"
                    append_.write(_append_)
            elif path.exists(FileName) is False:
                raise ValueError("No file Found")

except Exception as NotWriting:
    print(NotWriting)

# Clears the File
try:
    def clearFile(name):
        if path.exists(name) is True:
            with open(name, "w") as clear_:
                clear_.write("")
        elif path.exists(name) is False:
            raise ValueError("No file Found")

except Exception as NotEmptying:
    print(NotEmptying)
