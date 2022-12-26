# Quick python script to solve the coin problem, aka chicken mcnugget problem. Given an infinite number of one coin, and an infinite number of another, what's the largest amount you cannot make?

# This is a brute force approach, the test shows a number theory approach
def highest_impossible_amount(token1, token2):
  can_make = []
  limit = token1 * token2
  for a in range(limit):
    for b in range(limit):
      r = (a * token1) + (b * token2)
      if r not in can_make:
        can_make.append(r)

  cannot_make = []
  for i in range((token1 * token2)):
    if i not in can_make:
      cannot_make.append(i)
  return max(cannot_make)
