import requests
import re


def getHTMLText(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 '  # (Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36(kHTML, like Gecko)'
            # ' Chrome/52.0.2743.116 Safari/537.36'
        }
        r = requests.get(url, headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"data-original-title\"\:\".*?\"', html)
        tlt = re.findall(r'\"solution-link\"\:\".*?\"', html)

        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("错误1")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "题目", "题解"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    url = 'https://leetcode-cn.com/problemset/all/'
    infoList = []
    try:
        html = getHTMLText(url)
        parsePage(infoList, html)
        printGoodsList(infoList)
    except:
        print("错误2")
    printGoodsList(infoList)


main()