# To find the real root by bisection method using python programming
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn= input('Enter the equation with variable x: ')

#check euation
def F(x,eqn):
    return eval(eqn)
def f(x):
    return F(x,eqn)

# approximation
A=[]
M=[]
a=float( input('Enter the first approximation :'))
b=float( input('Enter the second approximation :'))

if f(a)*f(b)>0:
    print(f'No root lies in between ({a},{b})')
else:
    e=float(input('Enter the tolerable error:'))
    n=int(input('Enter the no of iteration:'))
    itr=1
    while itr<=n:
        c=(a+b)/2
        M.append(c)
        A.append([itr,a,b,c,f(a),f(b),f(c)])
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
        
        error = abs(b-a)


        if error<e:
            A=pd.DataFrame(A, columns=['iteration','a','b','c','f(a)',"f(b)",'f(c)']).to_string(index=False)
            print(A)           
            print(f'The aprox root is {(a+b)/2} in {itr} iteration')
            break
        itr +=1
   

    if itr>n:
        print(f'Solution doesnt converge in {n} iterations')
M=np.array(M)
#graph
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