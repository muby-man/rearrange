import re

def rearrange_name(fullname):
  return re.sub("(\w+), (\w+)","\2 \1",fullname)

