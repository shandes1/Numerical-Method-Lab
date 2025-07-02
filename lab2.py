#To find real root of a non linear equation by secand method using python programming
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sys 

#input equation
eqn = input('Enter the equation:')
def F(x,eqn):
    return eval(eqn)

def f(x):
    return F(x,eqn)

#approximation
a,b = float(input('Enter the 1st approximation:')),float(input('Enter the 2nd approximation:'))
M=[]
A=[]

#check
if f(a)==f(b):
    print('value become infinite!')
else:
    itr =1
    e=float(input('Enter the tolerable error:'))
    n=int(input('Enter the no of iteration:'))
    while(itr<=n):
        c= (a*f(b)-b*f(a))/(f(b)-f(a))
        M.append(c)
        A.append([itr,a,b,c,f(a),f(b),f(c)])
        error =abs(f(c))

        if error < e:
            print(f"The approx root is {c} in {itr} iteration")
            break
        a,b=b,c

        if f(a)== f(b):
             
            print('Division by 0 is not allowed')
            sys.exit()
        else:

            itr +=1

    if itr>n:
        print(f'solution doesnot change in {n} iteration')

A=pd.DataFrame(A, columns=['iteration','a','b','c','f(a)',"f(b)",'f(c)']).to_string(index=False)
print(A)
#graph
M = np.array(M)
x=np.linspace(-5,5,1000)
plt.plot(x,f(x),color='red',label=eqn,linestyle='--')
plt.axhline(0,0,color="black")
plt.axvline(0,0,color="black")
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')                                                                                                                                                                                    
plt.legend()
plt.title('Bisection Method')
plt.scatter(M,f(M))
for i, val in enumerate(M):
    plt.text(val,f(val),f"{i+1}")
plt.show() 