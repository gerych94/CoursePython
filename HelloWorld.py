"""
print("HelloWorld");
import re
snl = "";
with open('HelloWorld.py') as f:
    while True:
        s=f.readline();
        if(len(s)==0):
            break
        sn=re.sub('\s{2,5}',' '*4,s);
        snl+=sn;
    with open('HelloWorld.py','w') as f:
        f.writelines(snl);
    # w=open("test.py","w");
    # w.write(snl);
    # w.close();
    # print(snl);
"""
# import requests
# print(requests.get("https://github.com/apache/spark/blob/master/README.md"))
import random

# mas = [random.randint(100) for _ in range(100)]
mas = random.sample(range(20), 20)
print("Excisting array: ")
print(mas)

for i in range(len(mas)):
    for j in range(len(mas) - 1 - i):
        if mas[j] > mas[j + 1]:
            b = mas[j]
            mas[j] = mas[j + 1]
            mas[j + 1] = b
print("Buble sort: ")
print(mas)
random.shuffle(mas)

print(mas)

m = map(len, ["dd", "dddfdfdf"])
print(m)
