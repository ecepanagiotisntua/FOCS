from random import randint

def MillerRabinTest(a, d, s, n):
  x = pow(a,d,n)
  if(x == 1 or x == n-1):
    return True
  for i in range (0,s-1):
    x = x**2 % n
    if(x == n-1):
      return True
  return False

def MRTest(n, k = 30):
  if(n == 1):
    return False;
  if(n == 2 or n == 3):
    return True;

  d = n - 1
  s = 0
  while(d%2==0):
      d = d//2
      s = s+1


  for i in range(0,k):
    a = randint(2,n-1)
    if (MillerRabinTest(a,d,s,n)==False): 
      return False;
  return True;




