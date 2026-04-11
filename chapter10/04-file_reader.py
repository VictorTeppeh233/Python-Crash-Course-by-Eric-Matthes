#Reading the contents from the a file in the sub-folder.
#importing Path from pathlib
from pathlib import Path

#passing the Path object to the variable path
path = Path("text_files/country.txt")
#assigns the text inside the file to the country variable
country = path.read_text()
#prints the results
print(country)