'''All Pairs that Sum to Target
Create a function that returns all pairs of numbers in a list that sum to a target. Sort the pairs in ascending order with respect to the smaller number, then order each pair in this order: [smaller, larger].

Examples
all_pairs([2, 4, 5, 3], 7) ➞ [[2, 5], [3, 4]]
# 2 + 5 = 7, 3 + 4 = 7

all_pairs([5, 3, 9, 2, 1], 3) ➞ [[1, 2]]

all_pairs([4, 5, 1, 3, 6, 8], 9) ➞ [[1, 8], [3, 6], [4, 5]]
# Sorted: 1 < 3 < 4; each pair is ordered [smaller, larger]
Notes
If no pairs are found, return an empty list [].
You are only allowed to use each number once in a pair.
See Comments for a hint.'''

def all_pairs(numbers, target):
    pairs = []
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append([numbers[i], numbers[j]])
    return pairs

# Examples
print(all_pairs([2, 4, 5, 3], 7))  #  [[2, 5], [3, 4]]
print(all_pairs([5, 3, 9, 2, 1], 3))  # [[1, 2]]
print(all_pairs([4, 5, 1, 3, 6, 8], 9))  # [[1, 8], [3, 6], [4, 5]]
