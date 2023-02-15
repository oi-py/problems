#读取db_large/codeforces/下的所有html文件，统计每个题目中的每个单词的频率
#将统计结果存入db_large/codeforces_word_count.json
#注意只提取正文，不提取js、css、html标签等
#注意只提取英文单词，不提取中文、数字、标点符号等
#注意只提取长度大于等于3的单词，不提取长度小于3的单词
#注意存储时，每个每个条目只存储一个文件的统计结果
#将多个文件的统计结果加入一个字典中，然后再存储到json文件中

import json
import os
import re
from bs4 import BeautifulSoup

def get_counter(html):
    #提取正文
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    #提取英文单词
    words = re.findall('[a-zA-Z]+', text)
    #提取长度大于等于3的单词
    words = [word for word in words if len(word) >= 3]
    #统计每个单词的频率
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def main():
    #读取db_large/codeforces/下的所有html文件
    file_list = os.listdir('db_large/codeforces')
    #统计每个题目中的每个单词的频率
    problems = {}
    n = len(file_list)
    m = 0
    for file in file_list:
        m+=1
        print('processing %d/%d'%(m,n))
        #读取html文件
        html = open('db_large/codeforces/' + file, encoding='utf-8')
        problem_name = file.split('.')[0]
        word_count = get_counter(html)
        # soup = BeautifulSoup(html, 'html.parser')
        # word_count = {}
        # #提取正文
        # text = soup.get_text()
        # #提取英文单词
        # words = re.findall('[a-zA-Z]+', text)
        # #提取长度大于等于3的单词
        # words = [word for word in words if len(word) >= 3]
        # #统计每个单词的频率
        # for word in words:
        #     if word in word_count:
        #         word_count[word] += 1
        #     else:
        #         word_count[word] = 1
        #将统计结果存入字典problems中
        problems[problem_name] = word_count
    #将统计结果存入db_large/codeforces_word_count.json
    with open('db_large/codeforces_word_count.json', 'w', encoding='utf-8') as f:
        json.dump(problems, f, ensure_ascii=False, indent=4)
    print('Done!')

if __name__ == "__main__":
    main()