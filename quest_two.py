def fibonacci(n):
  if n <= 1:
    return n
  else:
    fib_seq = [0,1]
    while len(fib_seq) < n + 1:
      fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def main():
  num = int(input("Digite um número "))
  fib_seq = fibonacci(num)

  if num in fib_seq:
    print (f" O número {num} pertence a sequência de Fibonacci ;)")
  else:
    print (f" O número {num} não pertence a sequência de Fibonacci :(")

if  __name__ == '__main__':
  main()