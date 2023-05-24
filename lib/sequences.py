#!/usr/bin/env python3

def print_fibonacci(length):
    fib_seq = []
    if length > 0:
        fib_seq.append(0)
        if length > 1:
            fib_seq.append(1)
            if length > 2:
                for i in range(2, length):
                    # print(i)
                    fib_seq.append(fib_seq[i -1] + fib_seq[i -2])
                
    print(fib_seq)
    
print_fibonacci(10)

# def print_fibonacci(length):
#     if length > 2:
#         return(print_fibonacci(length - 1) + print_fibonacci(length - 2))
#     else:
#         return length

# def start_fib(fib_length):
#     if fib_length <= 0:
#         print(f'cant calculate with negative number')
#     else:
#         for i in range(fib_length):
#             print(print_fibonacci(i))
            
# start_fib(11)