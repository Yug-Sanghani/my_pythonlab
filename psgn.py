"""basic of positional argrument
def sum(a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result=sum(2,3)
print("add",result)


2.student information:
def stud_info(name,roll,marks):
    print("name :",name)
    print("roll no :",roll)
    print("marks:",marks)
    
stud_info("ravi",101,58)"""

#3.odd or even:
"""def odd_even(no):
    if(no%2==0):
        print("value{0}is even")
    else:
        print("value {no}is odd")
odd_even(50)
odd_even(15)"""

#4.check number is positive negetive or zero:
"""def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")
check_value(0)
check_value(90)
check_value(-444)"""

#5.simple interest:
"""def a(p,q,r):
    si=(p*q*r)/100
    print("simple interest :",si)
a(444,44,4)
a(444,4.4,4)"""



#area of circle:
def p(r):
    p=3.14*r*r
    p("area of circle :",p)
p(1.5)
p(4)