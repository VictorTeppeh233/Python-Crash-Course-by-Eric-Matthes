# Writing to a File
# Writing a Single Line

from pathlib import Path

path = Path("programming.txt")
path.write_text("I love programming.")