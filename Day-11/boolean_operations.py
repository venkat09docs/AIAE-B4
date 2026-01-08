# BOOLEAN VARIABLES

cardio_completed = True # 1
strength_completed = False # 0

bonus_points = cardio_completed + strength_completed
print(bonus_points)

if bonus_points > 0:
    print(f'Great job! You’ve earned {bonus_points} bonus point(s) for today’s workout!')
else:
    print('No bonus points today. Try completing a session to earn points!')

username = ''

if username:
    print(f'Welcome back, {username}!')
else:
    print('Please enter your username.')