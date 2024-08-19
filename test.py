import datetime

def is_prime(n):
  if n <= 1:
    return False
  
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
    
  return True

def is_prime_2(num):
    if num < 2:
        return False
    
    for i in range(2, int(num)):
        timestamp = datetime.datetime.now()
        print(timestamp)

        if num % i == 0:
            return False
        
        print(datetime.datetime.now() - timestamp)
        
    return True

def main():
    is_prime_2(10000000)

if __name__ == "__main__":
    main()