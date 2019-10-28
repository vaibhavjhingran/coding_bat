# Coding Bat - String 1

# hello_name
def hello_bob(name):
  return 'Hello' + 'name' + '!'

# make_abba
def make_abba(a, b):
  return a+b+b+a

# make_tags
def make_tags(tag, word):
  return '<'+ tag + '>' + word + '</' + tag + '>'

# make_out_word
def make_out_word(out, word):
  return out[:2] + word + out[2:]

# extra_end
def extra_end(str):
  return str[-2:]*3

# first_two
def first_two(str):
  return str[:2] if len(str)>=0 else str

# first_half
def first_half(str):
  half_length = len(str)/2
  return str[:half_length]

# without_end
def without_end(str):
  return str[1:len(str)-1]

# combo_end
def combo_end(a, b):
  return a+b+a if len(a)<len(b) else b+a+b

# non-start
def non_start(a, b):
  return a[1:]+b[1:]

# left2
def left2(str):
  return str[2:] + str[:2]
