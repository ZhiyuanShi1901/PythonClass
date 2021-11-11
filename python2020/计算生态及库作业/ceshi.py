# ceshi
# coding=utf-8


# _1
# coding=utf-8

def getHtml(savedhtml):
    with open(savedhtml, 'r', encoding='utf-8') as jingdong:
        Htmls = jingdong.readlines()
        return Htmls


def extractPictures(Htmllist):
    urls = []
    condition = 0
    for line in Htmllist:
        if '<img' in line:
            urls.append(url)
    return urls

with open('images.txt', 'a', encoding='utf-8') as image:
    Htmllist = getHtml('jingdong.html')
    urls = extractPictures(Htmllist)
    for url in urls:
        image.write(url)
    print(urls)


def extractPictures(Htmllist):
    urls = []
    for line in Htmllist:
        if 'src="' in line:
            urls.append(url)
    return urls