import re
with open("input.txt", "r") as f:
    read = f.readlines()

triples = []
for i in range(2, 140):
    triples.append([read[i - 2], read[i-1], read[i]])

strings = []
for i in triples:
    string = ""
    for j in range(2, 140):
        string1 = string.join([i[0][j], i[1][j-1], i[2][j-2]])
        string2  = string1 + "".join([i[0][j-2], i[1][j-1], i[2][j]])
        strings.append(string2)


count = 0
possible_matches = ["MASMAS", "MASSAM", "SAMMAS", "SAMSAM"]
for i in strings:
    if i in possible_matches:
        count += 1

print(count)