'''
自学网站：https://www.runoob.com/regexp/regexp-syntax.html
'''
#正则表达式
import re

#1、使用search函数匹配出第一次出现的数字100

content = '''xiaohong has 100 apples! 
xiaohong has 100 apples!
xiaohong has 100 apples! 
xiaohong has 100 apples!'''
result = re.search('xi.*?(\d+)\s.*?!',content)
#result2 = re.findall('xi.*?(\d+)\s.*?!',content)
#print(result2)
print(result.group(1))




#2、使用findall函数匹配出content中所有的数字
#findall函数的第一个参数是匹配的规则，第二个参数是要被匹配的内容

content = '''hello world 123 yes; hello world 123 yes; hello world 123 yes;'''
result  = re.findall('hel.*?(\d+)\s.*?s;',content,re.S)
print(result)

#3、规则封装
content = '''hello world 123 yes; hello world 123 yes; hello world 123 yes;'''
pattern = re.compile('hel.*?(\d+)\s.*?s;')
result = re.findall(pattern,content)
print(result)
