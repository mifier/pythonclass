# n=1 ¿ªÊ¼

def josephus(n, q): return 1 if n == 1 else (josephus(n-1, q) + q-1) % n +1
   

print(josephus(46, 4))


