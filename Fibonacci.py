import sys

def fibonacci(N):
    list = [0,1]
    for i in range(0,N):
        list.append(list[i]+list[i+1])
    return list

def main():
    N = int(input('Input : '))
    list = fibonacci(N)
    print(list)
    sum = 0
    for i in list:
        if i < N:
            if i % 2 == 0:
                sum+=i
    sys.stdout.write('Output : ')
    print(sum)

main()
