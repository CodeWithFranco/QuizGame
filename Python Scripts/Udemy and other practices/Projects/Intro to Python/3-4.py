friends = ['anna', 'mark', 'lyn', 'alex', 'jaz']
print(f'Hello! Welcome home, {friends[0].title()}. Im glad you are here.')
print(f'\nHello! Welcome home, {friends[1].title()}. Im glad you are here.')
print(f'\nHello! Welcome home, {friends[2].title()}. Im glad you are here.')
print(f'\nHello! Welcome home, {friends[3].title()}. Im glad you are here.')
friends[1] = 'don'
print(f'\nHello! Welcome home, {friends[1].title()}. Im glad you are here.\n')
no_friend = friends.pop(4)
print(friends)
print(f'\nThe killer was there, {no_friend.title()}.')