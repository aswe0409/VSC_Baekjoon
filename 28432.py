num = int(input())

word = []
for i in range(num):
    word.append(input())

candi_num = int(input())
candi = []
for i in range(candi_num):
    candi.append(input())

idx = word.index("?")

if num == 1:
    print(candi[0])
    quit()

# ?가 맨 앞에 있을 때
if idx == 0:
    back_word = word[idx + 1]
    back_candi = back_word[0]

    for i in candi:
        if i[-1] == back_candi:
            if i in word:
                continue
            else:
                print(i)
                quit()

# ? 가 맨 뒤에 있을 때
elif idx == len(word) - 1:
    front_word = word[idx - 1]
    front_candi = front_word[-1]

    for i in candi:
        if i[0] == front_candi:
            if i in word:
                continue
            else:
                print(i)
                quit()


else:
    front_word = word[idx - 1]
    front_candi = front_word[-1]

    back_word = word[idx + 1]
    back_candi = back_word[0]

    for i in candi:
        if i[0] == front_candi and i[-1] == back_candi:
            if i in word:
                continue
            else:
                print(i)
