import urllib.request

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html

def get_problem_list():
    for i in range(1,86):
        url = f'https://codeforces.com/problemset/page/{i}'
        print(url)
        html = getHtml(url)
        print(html)
        #bytes to string
        html = html.decode('utf-8')
        #保存到db/codeforces/problem_list_{i}.html
        with open(f'db/codeforces/problem_list_{i}.html','w',encoding='utf-8') as f:
            f.write(html)