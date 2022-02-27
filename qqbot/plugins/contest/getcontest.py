import requests
from urllib import request
from pprint import pprint

url = "http://algcontest.rainng.com/"
ojs = ["CodeForces", "AtCoder"]


def getcontest():
    re = requests.get(url=url)
    data = re.json()
    # pprint(data)
    res = []
    for each in data:
        if each["oj"] in ojs:
            # pprint(each)
            res.append(each)

    pprint(res)
    return res
