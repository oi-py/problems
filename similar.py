#计算相似度
#传入两个单词统计的字典
#计算在两个字典中都出现的单词的个数
def cal_similar(dict1,dict2):
    ans = 0
    for word in dict1:
        if word in dict2:
            ans += min(dict1[word],dict2[word])
    return ans