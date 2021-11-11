# 11.2
# coding=utf-8

with open("../lab15/poem.txt", 'w+', encoding='utf-8') as poem:
    gushi = ['采桑子·重阳\n', '毛泽东\n', '人生易老天难老，岁岁重阳。\n', '今又重阳，战地黄花分外香。\n', '一年一度秋风劲，不似春光。\n', '胜似春光，寥廓江天万里霜。\n']
    for line in gushi:
        poem.write(line)
    poem.seek(0, 0)
    print(poem.read())