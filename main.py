from random import randint

def FermatTest(n, k = 30):
  if(n == 1):
    return False;
  if(n == 2 or n == 3):
    return True;
  for i in range(0,k):
    a = randint(2,n-1)
    if (pow(a,n-1,n) != 1): return False;
  return True;




