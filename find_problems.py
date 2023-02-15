import splider_problem_fetch
import similar
import json
import splier_problem_counter

if __name__ == '__main__':
    print('input url:')
    url = input()
    html = splider_problem_fetch.get_html(url)
    word_count = splier_problem_counter.get_counter(html)
    #读取db_large/codeforces_word_count.json
    with open('db_large/codeforces_word_count.json', 'r', encoding='utf-8') as f:
        problems = json.load(f)
    #计算与每个题目的相似度
    ans = {}
    for problem in problems:
        ans[problem] = similar.cal_similar(word_count, problems[problem])
    #输出相似度最高的前10个题目
    ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    for i in range(10):
        print(i,ans[i])
