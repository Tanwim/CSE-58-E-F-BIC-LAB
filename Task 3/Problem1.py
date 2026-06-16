from itertools import product

text = input()
k, d = map(int, input().split())

counts = {}

for p in product("ACGT", repeat=k):
    pattern = "".join(p)
    count = 0

    for i in range(len(text) - k + 1):
        mismatches = 0

        for j in range(k):
            if pattern[j] != text[i + j]:
                mismatches += 1

        if mismatches <= d:
            count += 1

    counts[pattern] = count

max_count = max(counts.values())

for pattern in counts:
    if counts[pattern] == max_count:
        print(pattern, end=" ")
