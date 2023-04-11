from selenium import webdriver
from selenium.webdriver.common.by import By
import re

if __name__ == '__main__':
    url = 'https://www.fansale.at/fansale/tickets/rock-pop/pnk/502086/15912501'
    browser = webdriver.Chrome()
    browser.get(url)
    counter = {}
    single_offers = re.finditer('(?<=NumberOfTicketsInOffer">).', browser.page_source)

    for match_obj in single_offers:
        counter[match_obj.span()[0]] = match_obj.group()
    multiple_offers = re.finditer('(?<=<span class="Dropdown-DisplayValue">).', browser.page_source)
    for match_obj in multiple_offers:
        counter[match_obj.span()[0]] = match_obj.group()
    sorted_counter = dict(sorted(counter.items()))
    # for i in range(3):
    #     (k := next(iter(sorted_counter)), sorted_counter.pop(k))
    element = browser.find_elements(By.CLASS_NAME, 'moneyValueFormat')
    counter_list = list(sorted_counter.values())
    for i in range(len(element)):
        try:
            price_pre_ticket = float(element[i].text.replace(',', '.')) / float(counter_list[i])
            print("Count: " + counter_list[i] + " Price: " + element[i].text + " Price per Ticket: %.2f" % price_pre_ticket)
        except:
            continue
