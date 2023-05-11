# slicing
# a=2,4
# x=[1,2,3,4,5,6,7,8]
# print(x[2])
# print(x[1:4])
# print(x[1:])
# alefba=["a","b","c","d","e","f"]
# print(alefba[0:3])
# print(alefba[2:5])

# x=[1,2]
# y=[3,4]
# z=x+y
# z=x*4
# print(z)
# print(x+y)
# print(x*4)
# print(type (z))

x=[1,2]
z=x*2
print(f"baraye tekrar adad list:(x*2)={z}")
print(type(z))
# sazande list(2 parantez),list((1,4,9,10,23))
print(f'lotfan list besaz:1,4,9,10,23={list((1,4,9,10,23))}')
a=[1,4,9,10,23]
a.append('90')
a.remove('1','4')
print(a)

print("lotfan adad 90 be list mazid shavad va 1,4 hazf shavad=",a)
print("liste item4,9 joda besaz=" ,a[1:3])
print("liste item10,23 joda besaz=", a[3:])

