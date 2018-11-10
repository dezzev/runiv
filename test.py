import requests

tourl = ""

server = "http://127.0.0.1:80"

def test_shorts():
    global tourl

    url = "%s/link_gen" % server
    r = requests.post(url, data={'url': "google.com"})
    res = r.json()
    if res.get('tourl'):
        tourl = res.get('tourl')
    assert tourl != ""


def test_shortsCorrectly():
    global tourl

    url = "%s/%s" % (server, tourl)
    r = requests.get(url)
    res = False

    if r.history:
        print(r.url)
        if r.url == "http://www.google.com/":
            res = True
    assert res
