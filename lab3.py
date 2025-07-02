#To find real root of a non linear equation by Netwon Rapture method using python programming
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sys 

#input equation
eqn = input('Enter the equation:')
def F(x, eqn):
    try:
        return eval(eqn)
    except Exception as e:
        print(f"Error evaluating the function: {e}")
        sys.exit()

def f(x):
    return F(x,eqn)

def g(f,x,h=1e-10):
    return ((f(x+h)- f(x-h))/(2*h))

#approximation
a = float(input('Enter the 1st approximation:'))
M=[]
A=[]

#check
if g(f,a)==0:
    print('value become infinite!')
else:
    itr =1
    e=float(input('Enter the tolerable error:'))
    n=int(input('Enter the no of iteration:'))
    while(itr<=n):
        b= a- f(a)/g(f,a)
        M.append(b)
        A.append([itr,a,b,f(a),f(b)])
        error =abs(f(b))

        if error < e:
            print(f"The approx root is {b} in {itr} iteration")
            break
        a=b

        if g(f,a)==0:
             
            print('Division by 0 is not allowed')
            sys.exit()
        else:

            itr +=1

    if itr>n:
        print(f'solution doesnot change in {n} iteration')

A=pd.DataFrame(A, columns=['iteration','a','b','f(a)',"f(b)"]).to_string(index=False)
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
plt.title('Netwon Repture')
plt.scatter(M,f(M))
for i, val in enumerate(M):
    plt.text(val,f(val),f"{i+1}")
plt.show() 