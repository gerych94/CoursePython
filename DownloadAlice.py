import urllib.request

url = 'http://www.umich.edu/~umfandsf/other/ebooks/alice30.txt'
a = url
print(a)
urllib.request.urlretrieve(url, 'alice30.txt')
print("Downloaded")
words = []
with open("alice30.txt") as f:
    while True:
        b = f.readline()
        if b == "":
            break
        c = b.split()
        # words += c
        for i in range(1, len(c)):
            if len(c[i]) > 5:
                if c[i][:-3] == c[i - 1][:-3]:
                    print(c[i])
                    print(c[i - i])

# age = int(input("How old are you?"))
# reply = ('Учись', 'Учи')[age > 46]
# print(reply)
print("Opened")
print(words)
