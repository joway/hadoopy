# with open('words.list') as file:
#     print(file.read(4))
#     print(file.read(4))
#     print(file.read(4))
def test(n):
    for i in range(n):
        yield i

t = test(10)

for i in t:
    print(i)
