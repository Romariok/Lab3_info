import re

def readfile(s):
    tmp = open(s, encoding='utf8')
    tmp1 = ''
    for i in tmp.readlines():
        tmp1 += i
    tmp.close()
    return tmp1

smile = r'=-\|'

t1 = re.findall(smile, readfile("Smile_tests/Smile_test1.txt"))
t2 = re.findall(smile, readfile("Smile_tests/Smile_test2.txt"))
t3 = re.findall(smile, readfile("Smile_tests/Smile_test3.txt"))
t4 = re.findall(smile, readfile("Smile_tests/Smile_test4.txt"))
t5 = re.findall(smile, readfile("Smile_tests/Smile_test5.txt"))
print("Количество вхождений смайлика в тексте 1 = ", len(t1))
print("Количество вхождений смайлика в тексте 2 = ", len(t2))
print("Количество вхождений смайлика в тексте 3 = ", len(t3))
print("Количество вхождений смайлика в тексте 4 = ", len(t4))
print("Количество вхождений смайлика в тексте 5 = ", len(t5))
