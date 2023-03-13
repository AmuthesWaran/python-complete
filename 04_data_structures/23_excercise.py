from pprint import pprint

sentence = "This is a common interview question"

char_fq = {}

for char in sentence:
    if char in char_fq:
        char_fq[char] += 1
    else:
        char_fq[char] = 1

# pprint(char_fq, width=1)

print(sorted(char_fq.items(), key=lambda kv: kv[1], reverse=True))

char_fq_sorted = sorted(char_fq.items(),
                        key=lambda kv: kv[1],
                        reverse=True)
print(char_fq_sorted[0])
