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

# caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 65:
      return 0
    elif speed in range(66, 87):
    return 1
    else:
      return 2
  else:
    if speed <= 60:
      return 0
    elif speed in range(61,81):
      return 1
    else:
      return 2

