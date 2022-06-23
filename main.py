from bs4 import BeautifulSoup as bs
import requests
import os
site = "https://www.irctchelp.in/cancelled-trains-list/"
raw_html_err = requests.get(site)
raw_html = raw_html_err.text
# print(raw_html)
soup = bs(raw_html, 'html.parser')
list_of_trains = soup.find("pre").find("code")
raw_lot = str(list_of_trains)
trimed_lot = raw_lot.split(" ")
lot_err = list(trimed_lot)


train_number = input("Enter the train number: ")
if train_number in lot_err:
  print("Train is Cancelled")
else:
  print("Yayyy! Train is available and running!")
print(" ")
print("By <AdityaKrCodes/>")
print("Github: @adityakrcodes")
# TO CHECK