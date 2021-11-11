# _1
# coding=utf-8
def getHtml(savedhtml):
    with open(savedhtml, 'r', encoding='utf-8') as jingdong:
        Htmls = jingdong.readlines()
        return Htmls
def extractPictures(Htmllist):
    storage = []
    urls = []
    for line in Htmllist:
        if 'jpg' in line or 'png' in line:
            if 'https://' in line:
                storage.append(line)
    fat = []
    for line in storage:
        fat.append(line.split('"'))
    for it in fat:
        for line in it:
            if ('jpg' in line or 'png' in line) and 'http' in line:
                urls.append(line)
    return urls

with open('images.html', 'a', encoding='utf-8') as image:
    Htmllist = getHtml('jingdong.html')
    urls = extractPictures(Htmllist)
    print(urls)
    for url in urls:
        image.write(url)
        image.write('\n')
        image.write('\n')
