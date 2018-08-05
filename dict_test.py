
a=dict(one=1, two=2, three=3)
print('a' ,a)

b={'one':1, 'two':2, 'three':3}
print('b', b)

c=dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print('c', c)

d=dict([('two', 2), ('one', 1), ('three', 3)])
print('d', d)

e=dict({'one':1, 'three':3, 'two':2})
print(a==b==c==d==e)

#dict comprehension
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

#{'China': 86, 'India': 91, 'Bangladesh': 880, 'United States': 1,
#'Pakistan': 92, 'Japan': 81, 'Russia': 7, 'Brazil': 55, 'Nigeria':
#234, 'Indonesia': 62}

country_code_1={code: country.upper() for country, code in country_code.items() if code < 66}
print(country_code_1)
print(country_code_1.values())
#{1: 'UNITED STATES', 55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA'}

#处理不存在的字段

import sys
import re

WORD_RE = re.compile(r'\w+')
print('\n\n\nUse setdefault to handle the not existance key\n')
index = {}
with open('first.py', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # 这其实是一种很不好的实现，这样写只是为了证明论点
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])

#方法二：用一行就解决了获取和更新单词的出现情况列
#表，当然跟示例 3-2 不一样的是，这里用到了 dict.setdefault
print('\n\n\nUse setdefault to handle the not existance key\n')
index = {}
with open('first.py', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])


#方法三：使用collections.defaultdict
import collections
print('\n\n\nUse collections.defaultdict to handle the not existance key\n')
index = collections.defaultdict(list)
with open('first.py', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)

# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])