#This program removes a prefix from the string

#assigning a URL to a variable
nostarch_url = "https://nosarch.com"

#removing "https://"
nostarch_url = nostarch_url.removeprefix('https://')

#showing the stripped version
print(nostarch_url)