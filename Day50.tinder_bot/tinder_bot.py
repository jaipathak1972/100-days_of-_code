# 
def check(word):
  if word == word[::-1]:
    return True
  else:
    return False

# test 
if check(78):
  print("done")
else:
  print("fuck")