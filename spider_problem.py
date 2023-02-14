#读取db/codeforces/problem_list_*.html
#使用正则表达式匹配出题目的标题，url，难度和tag
#原始HTML内容如下：
'''
            <td>
                <div style="float: left;">
                    <a href="/problemset/problem/1774/F2">
Magician and Pigs (Hard Version)                    </a>
                </div>
                <div style="float: right; font-size: 1.1rem; padding-top: 1px; text-align: right;">
                        <a href="/problemset?tags=binary+search" style="text-decoration: none;" class="notice" title="Binary search">binary search</a>,
                        <a href="/problemset?tags=brute+force" style="text-decoration: none;" class="notice" title="Brute force">brute force</a>,
                        <a href="/problemset?tags=data+structures" style="text-decoration: none;" class="notice" title="Heaps, binary search trees, segment trees, hash tables, etc">data structures</a>,
                        <a href="/problemset?tags=implementation" style="text-decoration: none;" class="notice" title="Implementation problems, programming technics, simulation">implementation</a>
                </div>
            </td>
            <td class="act">
                <span class="act-item">
                    <a href="/problemset/submit/1774/F2"><img src="https://codeforces.org/s/44797/images/icons/submit-22x22.png" title="Submit" alt="Submit"/></a>
                </span>
            </td>
                <td style="font-size: 1.1rem">
                    <span title="Difficulty"class="ProblemRating">2700</span>
                </td>
            <td style="font-size: 1.1rem;">
                    <a title="Participants solved the problem" href="/problemset/status/1774/problem/F2"><img style="vertical-align:middle;" src="https://codeforces.org/s/44797/images/icons/user.png"/>&nbsp;x448</a>
            </td>
'''
#要提取的内容是：
#标题：Magician and Pigs (Hard Version)
#url：/problemset/problem/1774/F2
#难度：2700
#tag：binary search,brute force,data structures,implementation
#html中有很多题目，每个题目的内容都要提取出来
#HTML中的png链接可能变化，不要以它作为匹配标准
#保存list，每个元素的格式为[标题，url，难度，tag]
#注意删除标题中的换行符和多余的空格
#转为json格式保存到db/problem_list.json
#输出问题总数

import re
import json

def spider_problem():
    #从list_1匹配到list_85
    cnt = 0
    items_all = []
    for i in range(1,86):
        #读取文件
        filename = 'db/codeforces/problem_list_' + str(i) + '.html'
        print(i,filename)
        with open(filename,'r',encoding='utf-8') as f:
            html=f.read()
        print('read ok')
        #匹配标题+url+难度
        pattern = re.compile(r'<div style="float: left;">.*?<a href="(/problemset/problem/\d+/\w+)">(.+?)</a>.*?text-align: right;.*?<span title="Difficulty"class="ProblemRating">(\d+)</span>',re.S)
        items = re.findall(pattern,html)
        for url,title,diff in items:
            #去掉title中的换行符和多余的空格
            title = title.replace('\r','').replace('\n','').replace('  ','')
            print(title,url,diff)
            items_all.append([title,url,diff])
        cnt += len(items)
        print(i,cnt)
    with open('db/problem_list.json','w',encoding='utf-8') as f:
        json.dump(items_all,f)

if __name__ == '__main__':
    spider_problem()

