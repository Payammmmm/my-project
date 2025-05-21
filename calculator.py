#this is my first project simple calculator
print("if you write -1 exit program")
num2=0
num1=0
while num1 != -1:
      num1=int(input('enter number one: '))
      if num1== -1:
           print('exiting program ...')
           break
      oper=input('enter your operator: ')
      num2=int(input('enter number two: '))
      if oper=='+':
         jam=num1+num2
         print(jam)
      elif oper=='-':
           tafrigh=num1-num2
           print(tafrigh)
      elif oper=='*':
           zarb=num1*num2
           print(zarb)
      elif oper=='/':
           taghsim=num1/num2
           print(taghsim)
