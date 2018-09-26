from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#from datetime import datetime
import numpy as np
import pandas as pd
import time
import sys
import csv

class Yahoo_Basic_Info(object):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def action(self, date):

        my_url = 'https://finance.yahoo.com/calendar/economic?from=' + date
        print(my_url)

        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, 'html.parser')

        # save and look at the html coding, find the location of what you need to get, apply the struture and grab
        d0 = []
        d1 = list()
        d2 = list()
        d3 = list()
        d4 = list()
        d5 = list()
        d6 = list()
        d7 = list()
        col0 = page_soup.find_all('td', {"data-col0"})
        col1 = page_soup.find_all('td', {"data-col1"})
        col2 = page_soup.find_all('td', {"data-col2"})
        col3 = page_soup.find_all('td', {"data-col3"})
        col4 = page_soup.find_all('td', {"data-col4"})
        col5 = page_soup.find_all('td', {"data-col5"})
        col6 = page_soup.find_all('td', {"data-col6"})
        col7 = page_soup.find_all('td', {"data-col7"})
          #print(len(col0))
        length=len(col0)
        for x in range(length):
            d0.append([col0[x].text])
            d1.append([col1[x].text])
            d2.append([col2[x].text])
            d3.append([col3[x].text])
            d4.append([col4[x].text])
            d5.append([col5[x].text])
            d6.append([col6[x].text])
            d7.append([col7[x].text])

        print(d0[0][0])
        with open('C:/Users/User/Desktop/webscraping.csv','w',newline='') as csvfile:
              writer = csv.writer(csvfile,delimiter=',')
              for y in range(length):  ######
                  output = writer.writerow(
                      [d0[y][0], d1[y][0], d2[y][0], d3[y][0], d4[y][0], d5[y][0], d6[y][0], d7[y][0]])



def Main():
    obj = Yahoo_Basic_Info()
    date = pd.date_range(start='2017-01-01', end='2017-09-21' )  #range
    for i in range(len(date)):
        dateStr =str(date[i])
        dateStr = dateStr.split(' ')[0]
        print(dateStr)
        output = obj.action(dateStr)

    #print(date,output)
if __name__ == '__main__':
        Main()
