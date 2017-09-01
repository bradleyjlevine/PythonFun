# The method used for finding primes is trial division and the method for the threads is domain restriction

import math as m
import threading as t


class PrimeThread(t.Thread):
    def __init__(self, begin, end):
        t.Thread.__init__(self)
        self.begin = begin
        self.end = end
        self.r = []

    def run(self):
        self.r = [p for p in range(self.begin, self.end, 2) if self.is_prime(p)]

    def is_prime(self, n):
        assert n > 0
        stop = int(m.sqrt(n)) + 1
        for i in range(3, stop, 2):
            if n % i == 0:
                return False
        return True


hi = int(input("Enter the upper limit to generate primes: "))
num_threads = int(input("Enter the number of threads: "))
assert num_threads > 0

step = int(hi / num_threads)
remainder = int(hi % num_threads)
begin = 3
end = step

if end % 2 == 0:
    end = end + 1

threads = []
for i in range(num_threads):
    threads.append(PrimeThread(begin, end))
    begin = end
    end = end + step
    if i == num_threads - 2:
        end = end + remainder

for i in range(num_threads):
    threads[i].start()
    
print ("\n")    
for i in range(num_threads):
    threads[i].join()
    print ("Thread-{0}: {1}".format(str(i + 1), str(threads[i].r)))

r = [2]
for i in range(num_threads):
    r = r + threads[i].r

pn = len(r)
pd = pn / (1.0 * hi)
pda = 1 / m.log(pn)
print ("{0}\n# of Primes found: {1}\nPrime Density measured: {2}\nPrime Density approx: {3}".format(str(r), str(pn),
                                                                                                    str(pd), str(pda)))
