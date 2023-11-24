
def rearrange(fullname):
  return re.sub("(\w+), (\w+)","\2 \1",fullname)
