#读取db/codeforces_index.json
#格式为[{url,title,difficulty}]
#枚举每个url，在url前拼接https://codeforces.com/，得到完整url，然后获取题目的html
#将每个题目的完整html存入db_large/codeforces/下，文件名为题目的url后缀，如https://codeforces.com/problemset/problem/4/A的文件名为4_A.html
#使用utf-8编码，避免中文乱码

import json
import requests
import os

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

def main():
    with open("db/codeforces_index.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    n = len(data)
    m = 0
    for title,url,difficulty in data:
        m += 1
        url = "https://codeforces.com" + url
        url_token = url.split("/")[-2:]
        filename = "_".join(url_token) + ".html"
        if os.path.exists("db_large/codeforces/" + filename):
            continue
        html = get_html(url)
        with open("db_large/codeforces/" + filename, "w", encoding="utf-8") as f:
            f.write(html)
        print("已下载：" + filename + "，进度：" + str(m) + "/" + str(n))

if __name__ == "__main__":
    main()