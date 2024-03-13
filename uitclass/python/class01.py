#     STRING AND FSTRING


name: str = 'Malik Shaqas'

print ("My name is", name)
print ('PIAIC')
print ('"By Zia Khan"')

print ('PIAIC','Generative AI','Cloud Applied', sep='---')

# for inline words spacing use ( end='   '  )
print('PIAIC', end='   ')
print('Generative AI', end='   ')
print('Cloud Applied')

#opeators
a :int =10
b : int = 5
c: int = a+b

print(a+b)  # For addition
print (c) 
print(c-a)   # for subtraction
print(a/b)   #for Division
print(a*c)   # for Mulitplication

#List and Its Methods

#    ->                   0       1           2
names : list[str] = ["Qasim","Sir Zia", "Sir Junaid",
                     "Apple","Banana", "Orange"]
# <-                    -3     -2          -1

print(names[1])
print(names[-1])
print(names[2])
print(names[-2])
print(names[3])
print(names[-3])

#slicing

print(names[1:5])
print(names[1:6])
print(names[1:7])

print(names[1:4])   # after : show index 3 value e.g (insert : 4) show 3rd index value

print()

print(names[-5:-3]) # (-) also follow forward position
print()

print(names[-3:-2])
print()
print(names[-3:-5])  # show empty becasue it does not support backward it supports only forward position
print()
print(names[0::3])
print(names[0::5])

names.sort()
print(names)

names_list = list(names)
names_list.append("watermelon")
print(names_list)

print(names)

names = tuple(names_list)
print(names)