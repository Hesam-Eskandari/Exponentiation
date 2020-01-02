#multiplication is allowed
#Python 3 Compatible
from time import time
from random import random, randint
import matplotlib.pyplot as plt
from math import log


def power(n):
    pass

def root(q,n=10):
    
    if q == 0 or q == 1 or n == 1:
        return q
    if q < 0:
        if n %2 == 0:
            print('math error calculating even root of a negative number',)
            return 0
        else:
            q = -q
            a = -1
    else: 
        a = 1
    epsilon = 0.0000001
    q2 = (q+1)/2.0
    qq = power_log(q2,10)
    qq = [qq,qq]
    q2 = [q2,q2]

    while True:
        
        if (qq[1] - q) < epsilon and (qq[1] - q) > -epsilon:
            break
        if qq[1] < q:
            if qq[0] < q:
                q2[0] = q2[1]
                q2[1] = (q2[1]+q)/2.0
                qq[0] = qq[1]
            else:
                q2[1] = (sum(q2))/2
        elif qq[1] > q:
            if qq[0] > q:
                q2[0] = q2[1]
                q2[1] = (q2[1]+1)/2.0
                qq[0] = qq[1]
            else:
                q2[1] = (sum(q2))/2
        qq[1] = power_log(q2[1],n)
    #return int((a*q2[1])/epsilon)/(int(1/epsilon)) 
    return a*q2[1]
    

def power_log(p,m,i=0,r=0):
    n = int(m)
    if  i == 0:
        r = (m-n)
    if n == 1:
        return p  
    elif n == -1:
        return 1/p
        #return (n==1)*p+(n==-1)/p
    elif n == 0:
        if r == 0:
            return 1
        else:
            pass
    if n%2 == 0:
        return power_log(p*p,n//2,i+1,r)
    elif n%2 == 1:
        return p* power_log(p*p,n//2,i+1,r)
    
def power(x,y):
    if x == 0:
        if y == 0:
            return "MathError: imposible operation"
        else:
            return 0
    if y == 0:
        return 1
    y2 = y
    y_list = []
    i = 0
    while True:
        y_list.append(int(y2))
        i+=1
        y2 = y2%1
        y2 *= 10
        if i > 2:
            if y_list[-4:] == [9,9,9,9] or y_list[-4:] == [0,0,0,0] or len(y_list)>6:
                break
    #print(y_list)
    result = 1
    for i in range(len(y_list)):
        result *= root(power_log(x,y_list[i]),10**(i))
        if y == int(y):
            break
    return result
times1 =[]
times2 = []
X = []
for x in [2**(i+10) for i in range(22)]: 
    #print(x)
    t0=time()
    a = power(2,x)
    t1=time()
    b = 2**x
    t2 = time()
    times1.append(t1-t0)
    times2.append(t2-t1)
    X.append(x)
times_avg = []
for i in range(100):
    t0=time()
    a = power(2,2**10)
    times_avg.append(time()-t0)
time_avg = sum(times_avg)/len(times_avg)

    
n = [(X[i]+1)/500*time_avg for i in range(len(times1))]
nlog = [log((X[i]+2),2)*time_avg for i in range(len(times1))]
plt.plot(X,times1,'-s',label="Power")
plt.plot(X,times2,'-r*',label="Python Pow()")
#plt.plot(X[:20],n[:20],'r',label="n")
#plt.plot(X,nlog,'g',label="log(n)")
plt.legend(loc="upper left")
plt.xlabel('Size of Exponent')
plt.ylabel('Time (s)')
plt.savefig('PowerVsPow.png',dpi=500)
plt.show()
#print(times1)

#print('correctness: ',a==b)
#root(10,1)
#print(power_log(2.288,2))      