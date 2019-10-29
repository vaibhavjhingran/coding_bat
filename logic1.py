# Coding Bat - Logic 1

# cigar_party
def cigar_party(cigars, is_weekend):
  if is_weekend and cigars>=40:
    return True
  elif cigars in range(40,61):
    return True
  else:
    return False

# date_fashion
def date_fashion(you, date):
  if you in range(8,11) and date in range(8,11):
    return 2
  elif you in range(0,3) and date in range(0,3):
    return 0
  else:
    return 1

# squirrel_play
def squirrel_play(temp, is_summer):
  if is_summer:
    return True if temp in range(60,101) else False
  elif temp in range(60,91):
    return True
  else:
    return False
