from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

cards = list(combinations(cards, 3))
rslt = 0
tmp = 0

for card in cards:
  iSum = sum(card)

  if iSum <= m and iSum > tmp:
    rslt = iSum
    tmp = iSum

print(rslt)