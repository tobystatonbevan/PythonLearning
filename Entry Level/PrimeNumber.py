def is_prime(num):
    if num == 2:
        return True
    for i in range (2,num):
        if num%i:
            if i == num-1:
                return True
            pass
        else:
            return False

#this function is more efficient because a non-prime number will have a successful divisor below the value of its square root        
# def is_prime(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
