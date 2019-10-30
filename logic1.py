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

# love6
def love6(a, b):
  return True if(a==6 or b==6 or a+b==6 or abs(a-b)==6) else False

# in1to10
def in1to10(n, outside_mode):
  if not outside_mode:
    if n in range(1,11):
      return True
    else:
      return False
  else:
    if n<=1 and n>=10:
      return True
    else:
      return False

# near_ten
def near_ten(num):
  x = num%10
  if x<=2 or x in range(8,10):
    return True
  else:
    return False

# sorta_sum
def sorta_sum(a, b):
  sum = a + b
  return 20 if sum in range(10, 20) else sum

# alarm_clock
def alarm_clock(day, vacation):
  if vacation:
    if day in range(1,6):
      return '10:00'
    elif day==0 or day==6:
      return 'off'
  else:
    if day in range(1,6):
      return '7:00'
    else:
      return '10:00'

