# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from rich.table import Table
from rich import print as rprint
from rich import box

s = requests.Session()
main_url = "http://lugatim.com"
url = main_url + "/s/"


def get_cookie():
    try:
        g = s.get(main_url)
        jsessionid = s.cookies["JSESSIONID"]
    except:
        return "Session error!"
    return jsessionid


def get_results(word):
    headers = {"Cookie": "JSESSIONID=" + get_cookie()}
    r = s.get(url + quote(word), headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    div = soup.find("div", {"class": "search-results-div"})
    aa = div.find_all(["h3", "p"])
    results = []

    for item in aa:
        if item.name == "h3":  # title
            title = item.text.strip()
            results.append(title)
        if item.name == "p":  # definitions
            psoup = item.find_all(["span", "br"])
            idx = 0
            defin = [""]
            for i in psoup:
                # combine all spans until br
                if i.name == "span":
                    defin[idx] += i.text
                # create new item
                if i.name == "br":
                    defin[idx] = defin[idx].strip()
                    defin.append("")
                    idx += 1
            defin[-1] = defin[-1].strip()
            if defin != "":
                results.append(defin)
    if results == []:
        print("Sonuç bulunamadı!")
        exit()
    return results


def plain(word, all):
    results = get_results(word)
    for i in results:
        if isinstance(i, list):
            for j in i:
                print(j)
        else:
            print(i)
        # if all != True:
        #     break


def rich(word, all):
    results = get_results(word)
    tabl = 0
    for i in results:
        if isinstance(i, list):  # resutls
            for j in i:
                globals()[f"table{tabl-1}"].add_row(j)
        else:  # title
            title = (
                f"[link={url}{quote(word)}]Kubbealtı Lugatı - {word}[/link]"
                if tabl == 0
                else None
            )
            globals()[f"table{tabl}"] = Table(title=title, box=box.SQUARE)
            globals()[f"table{tabl}"].add_column(i)
            tabl += 1
    for s in range(tabl):
        rprint(globals()[f"table{s}"])
        del globals()[f"table{s}"]
        if all != True:
            break
