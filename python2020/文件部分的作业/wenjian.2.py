# wenjian.2
# coding=utf-8

with open("poem.txt", 'w+', encoding='utf-8') as poem:
    gushi = ['八阵图\n', '[唐]杜甫\n', '功盖三分国\n', '名高八阵图\n', '江流石不转\n', '遗恨失吞吴\n']
    poem.writelines(gushi)
    poem.seek(0, 0)
    print(poem.read())
