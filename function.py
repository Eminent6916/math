def fb_point (wins, draws, losses, ):
    win = wins * 3
    draw = draws * 1
    loss = losses * 0
    total = win + draw + loss
    print(f'(Football Point({wins}, {draws}, {losses},) -----> {total} ')
    
print('Instruction: seperate your value with a coma " , " ') 
point = (input('wins,   draws,  losses \n:>'))
sheet = point.split(',')
wins = int(sheet[0]) 
draws = int(sheet[1])
losses =  int(sheet[2])

print(fb_point (wins, draws, losses,))
