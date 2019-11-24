from random import random
from array import array

# floats = array('d',(random() for i in range(10**7)))
# print(floats[0])

DITAL_CODES = [(86,'China'),(91,'USA'),(33,'UK'),(12,'Frech'),(56,'Rossa')]
country_code = {country:code for code,country in DITAL_CODES }
print(country_code)
print(country_code.items())
country_codes = {code:country.upper() for code,country in DITAL_CODES if code <66}
countries_code = {code:country.upper() for country,code in country_code.items() if code < 66}
print(country_codes)
print(countries_code)