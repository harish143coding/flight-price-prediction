
"""
practice questions for Python Interview
"""

#Nr-1 Write a Function to reverse a string
x = "reverse it"

def reverso(a):
  y = ""
  for i in range(1,len(x) + 1):
    y += a[-i]
    print(y)
  return y
print(reverso(x))

#Nr-2 Write a fn to find missing nr in array. 

L1 = [0.2, 'a', 1, True]
for x in L1:
   print(x)

  