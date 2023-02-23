score = {'Anayara': 1, 'Alexandre': 0}

higher_score = 0
for player, points in score.items():        
    if points > higher_score:
        higher_score = points
        winner = player

# print(winner, higher_score)     

yes = score.items()

no = iter(yes)

print(next(no)[0])
print(next(no)[0])
print(next(no)[0])