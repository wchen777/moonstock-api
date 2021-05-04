from selenium import webdriver
from util import *
from config_mysql import *
from db import *
import pprint
import mysql.connector

# constants
driver_path = './chromedriver'
url = 'https://www.slickcharts.com/sp500'
base_url = 'https://www.slickcharts.com/'
data_order = ['price', 'PE_trailing', 'change', 'PE_forward', 'change_percent',
              'dividend_yield', 'prev_close', 'dividend', 'volume', 'market_cap',
              'year_low', 'EPS_trailing', 'year_high', 'EPS_forward']

# get config from config file
config = cfg

# connect to mysql, setup table
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()
create_stock_table(cursor)
cnxn.commit()

# setup web scraper stuff
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)
table_body = driver.find_element_by_tag_name('tbody')
table_all = table_body.find_elements_by_tag_name('tr')

# length of table of stocks
length = len(table_all)

# index tracker
index = 0

while index < length:
    # reset current page, grab table data
    driver.get(url)
    table_body = driver.find_element_by_tag_name('tbody')
    table_all = table_body.find_elements_by_tag_name('tr')

    # get current table index
    row = table_all[index]

    print("#" + str(index + 1) + ":")

    stonk = {}

    # get fields from initial table
    cols = row.find_elements_by_xpath(".//*")

    name = cols[2].text
    ticker = cols[3].text
    weight = cols[5].text

    # go to web page with rest of data
    driver.get(base_url + 'symbol/' + ticker)

    # get all data points
    data_vals = driver.find_elements_by_tag_name('td')

    # first data points
    stonk['company_name'] = name
    stonk['ticker'] = ticker
    stonk['weight_sp500'] = weight

    # fill json/dict with order of data points
    for ind, vals in enumerate(data_vals):
        stonk[data_order[ind]] = vals.text

    # fix data types for stock data
    fix_values(stonk)
    pprint.pprint(stonk)
    index += 1

cnxn.close()
