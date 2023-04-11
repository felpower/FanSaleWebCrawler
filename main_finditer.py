import re
from urllib.request import Request, urlopen

if __name__ == '__main__':
    url = 'https://www.fansale.at/fansale/tickets/rock-pop/robbie-williams/502344/16342631'
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }

    page = Request(url, headers=headers)
    page = urlopen(page).read().decode()
    counter = {}
    single_offers = re.finditer(
        '(?<=<span class="EventEntryRow EventEntryRow-inDetailB NumberOfTicketsInOffer">)(.*)(?=</span>)', page)

    for match_obj in single_offers:
        counter[match_obj.span()[0]] = match_obj.group()
    multiple_offers = re.finditer('(?<=<span class="Dropdown-DisplayValue">)(.*)(?=</span>)', page)
    for match_obj in multiple_offers:
        counter[match_obj.span()[0]] = match_obj.group()
    sorted_counter = dict(sorted(counter.items()))
    # for i in range(3):
    #     (k := next(iter(sorted_counter)), sorted_counter.pop(k))
    element = re.findall('(?<=moneyValueFormat">)(.*)(?=</span> )', page)
    counter_list = list(sorted_counter.values())
    cheapest_ticket = 100000.0
    for i in range(len(element)):
        try:
            price_pre_ticket = float(element[i].replace(',', '.')) / float(counter_list[i])
            if price_pre_ticket < cheapest_ticket and price_pre_ticket != 0:
                cheapest_ticket = price_pre_ticket
            if price_pre_ticket != 0:
                print("Count: " + counter_list[i] + " Price: " + element[i] + " Price per Ticket: %.2f" % price_pre_ticket)
        except:
            continue


    print("Cheapest Ticket: %.2f" % cheapest_ticket)
