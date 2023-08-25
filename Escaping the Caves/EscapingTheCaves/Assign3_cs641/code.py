def power(x, n, p): 
    if (n == 0) : 
        return 1
    elif (n % 2 == 0) : 
        return power((x * x) % p, n // 2, p) 
    else: 
        return (x * power((x * x) % p, (n - 1) / 2 % p, p))

def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 
