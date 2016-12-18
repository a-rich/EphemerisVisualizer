from splinter import Browser
from sys import exit, argv
import time
import re
import pickle

objects = {
    'planet': {},
    'js': {},
    'ss': {},
    'us': {},
    'ns': {},
    'os': {},
    'sc': {}
  }

browser = Browser('chrome')
browser.visit("http://ssd.jpl.nasa.gov/horizons.cgi")
browser.find_by_text('change')[1].click()

t = time.ctime().split()
date = t[4] + '-' + t[1] + '-' + str(int(t[2])+1)

for obj in objects:
  browser.select('mb_list', obj)
  browser.find_by_name('show_mb_list').first.click()
  items = browser.find_by_name('body').first.value
  IDs = [re.findall("[*\-0-9]+", b)[0] for b in items.split("\n")]

  for i in IDs:
    browser.select('body', "MB:{0}".format(i))
    browser.find_by_name('select_body').first.click()
    browser.find_by_name('go').first.click()
    text = browser.find_by_css('pre')[1].text.split("\n")

    for line in text:
      if "Start time" not in line and date in line:
        data = line.split("    ")[1].split()[:6]

    objects[obj][i] = data
    browser.back()
    browser.back()

  browser.back()

pickle.dump(objects, open("objects.p", "wb"))
