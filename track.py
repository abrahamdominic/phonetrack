# first install phone numbers, phone number is a Python package
# pip install phonenumbers
# this script is for tracking phone number and ISP name
# you can use any text editor to write your Python script but i used vim editor to write this script.


import phonenumbers
from test import number

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(nmber, "RO")
print(carrier.name_for_number(service_nmber, "en"))
