from urllib.request import Request, urlopen
import json
import regex

if __name__ == '__main__':
    url = 'https://www.fansale.at/fansale/tickets/rock-pop/pnk/502086/15912501'
    # Lido = 'https://www.fansale.at/fansale/tickets/rock-pop/lido-sounds/782486/15935882'
    # Pink = 'https://www.fansale.at/fansale/tickets/rock-pop/pnk/502086/15912501'
    # Robbie Williams = 'https://www.fansale.at/fansale/tickets/rock-pop/robbie-williams/502344/16342631'
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/112.0.0.0 Safari/537.36"
    }

    req = Request(url, headers=headers)
    url_req = urlopen(req)
    page = url_req.read()

    string = page.decode('utf-8')
    ch1 = ".initialOfferData = "
    text = string[string.find(ch1) + len(ch1):string.find("FS.eventdata.filtering.init();")]
    pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
    json_list = pattern.findall(text)
    counter = []
    for obj in json_list:
        try:
            obj = json.loads(obj)
            for splits in obj["allSplittingPossibilitiesWithPrice"]:
                counter.append(splits)
        except:
            continue
    if counter:
        new_list = sorted(counter, key=lambda d: d['price'])
        print(new_list)
