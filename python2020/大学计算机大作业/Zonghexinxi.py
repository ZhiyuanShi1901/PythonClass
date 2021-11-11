# Zonghexinxi
# coding=utf-8

def zonghe(zonghe):
    pingfen = zonghe.split('</span>')[0]
    leixing = zonghe.split('</span>')[1].split('>')[1].split('<')[0]
    time = zonghe.split('</a>')[1].split('/ ')[1]
    zishu = zonghe.split('/ ')[3].split('<br/>')[0]
    jianjie = zonghe.split('<br/>')[1]

    zonghexinxi = []
    zonghexinxi.append(pingfen)
    zonghexinxi.append(leixing)
    zonghexinxi.append(time)
    zonghexinxi.append(zishu)
    zonghexinxi.append(jianjie)
    return zonghexinxi
