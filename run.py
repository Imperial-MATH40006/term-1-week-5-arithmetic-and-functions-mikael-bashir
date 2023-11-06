import time
from autograder_term1week5 import *
import math, cmath
import numpy
from datetime import datetime
_globals = globals()


# ============================
# question 0
# ============================


# 5 Marks
# Do not try to delete this cell
# Run this cell for grading of Question 0
_globals = globals()
question0(_globals)


# ============================
# question 1)i)
# ============================


q1ia_answer = 17
q1ib_answer = 64
q1ic_answer = 2/3
q1id_answer = 8
q1ie_answer = 128
q1if_answer = 32768
# print(q1ia_answer)
# print(q1ib_answer)
# print(q1ic_answer)
# print(q1id_answer)
# print(q1ie_answer)
# print(q1if_answer)

'''
# a)
print(4**2 + 1)

# b)
print(4**(2+1))

# c)
print(2/3)

# d)
smallest = 0
while True:
    if smallest <= 381/47:
        smallest += 1
    else:
        print(smallest - 1)
        break

# e)
print(4 * 2**5)

# f)
print((4*2)**5)
'''


_globals = globals()
question1(_globals)


# ============================
# question 1)ii)
# ============================


q1iia_answer = 1237
q1iib_answer = 1157
q1iic_answer = 636
start = time.time()
q1iid_answer = pow(1417456, 1191761, 1820)
duration = time.time() - start
# print(q1iia_answer)
# print(q1iib_answer)
# print(q1iic_answer)
# print(q1iid_answer)

'''
# a)
print(372517%1820)

# b)
print((1417456+1191761)%1820)

# c)
print((1417456*1191761)%1820)

# d)
print(pow(1417456, 1191761, 1820))
'''

_globals = globals()
question1_ii(_globals)


# ============================
# question 2)i)
# ============================


q2ia_answer = math.sqrt(50)
q2ib_answer = math.cos(math.pi/7)
q2ic_answer = math.e**(math.e**2)
q2id_answer = math.log(58, math.e)
q2ie_answer = math.log10(58)
q2if_answer = math.pi/2 - math.atan(2)
q2ig_answer = math.atanh(1/2)
#print(q2ia_answer)
#print(q2ib_answer)
#print(q2ic_answer)
#print(q2id_answer)
#print(q2ie_answer)
#print(q2if_answer)
#print(q2ig_answer)

'''
# a)
print(math.sqrt(50))

# b)
print(math.cos(math.pi/7))

# c)
print(math.e**(math.e**2))

# d)
print(math.log(58, math.e))

# e)
print(math.log10(58))

# f)
print(math.pi/2 - math.atan(2))

# g)
print(math.atanh(1/2))
'''

_globals = globals()
question2_i(_globals)


# ============================
# question 2)ii)
# ============================


q2iia_answer = numpy.sqrt(50)
q2iib_answer = numpy.cos(numpy.pi / 7)
q2iic_answer = numpy.exp(numpy.e ** 2)
q2iid_answer = numpy.log(58)
q2iie_answer = numpy.log10(58)
q2iif_answer = numpy.arctan(1/2)
q2iig_answer = numpy.arctanh(1/2)
#print(q2iia_answer)
#print(q2iib_answer)
#print(q2iic_answer)
#print(q2iid_answer)
#print(q2iie_answer)
#print(q2iif_answer)
#print(q2iig_answer)

'''
# a)
print(numpy.sqrt(50))

# b)
print(numpy.cos(numpy.pi / 7))

# c)
print(numpy.exp(numpy.e**2))

# d)
print(numpy.log(58))

# e)
print(numpy.log10(58))

# f)
print(numpy.arctan(1/2))

# g)
print(numpy.arctanh(1/2))
'''

_globals = globals()
question2_ii(_globals)


# ============================
# question 3)
# ============================

# a)
# import any necessary functions
# Assign your solutions to the questions above to the variables below.
p = 6
q = 9

x = numpy.cbrt(q/2 + numpy.sqrt((q//2)**2 - (p//3)**2)) + numpy.cbrt(q/2 - numpy.sqrt((q//2)**2 - (p//3)**2))
#print(p)
#print(q)
#print(x)

if round(x)**3 == p*round(x) + q:
    x = round(x)

assert(x == question3(p, q))
print("Question 3(a) passed!")

# b)
# import any necessary functions
# Assign your solutions to the questions above to the variables below.
p = 3
q = 18

x = numpy.cbrt(q/2 + numpy.sqrt((q//2)**2 - (p//3)**2)) + numpy.cbrt(q/2 - numpy.sqrt((q//2)**2 - (p//3)**2))
#print(p)
#print(q)
#print(x)

assert(x == question3(p, q))
print("Question 3(b) passed!")

# c)
# import any necessary functions
# Assign your solutions to the questions above to the variables below.
p = 6
q = 4
temp = 2 + 4j
x = (q/2 + ((q//2)**2 - (p//3)**2)**(1/2))**(1/3) + (q/2 - ((q//2)**2 - (p//3)**2)**(1/2))**(1/3)
print(x)
x = (q/2 + cmath.sqrt((q//2)**2 - (p//3)**2))**(1/3) + (q/2 - cmath.sqrt((q//2)**2 - (p//3)**2))**(1/3)
#print(p)
#print(q)
print(x)

print(cmath.log(-2+0j))
print(numpy.log((-2+0j)))
print(6)


assert(x == question3(p, q))
print("Question 3(c) passed!")

print(pow())
