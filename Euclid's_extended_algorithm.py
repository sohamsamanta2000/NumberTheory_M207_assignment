def ext_gcd(a, b):
    x, y = 0, 1  # initial values as explained below
    x1, y1 = 1, 0  # initial values as explained below
    while a != 0:
        q = b // a  # quotient at each step of euclid's algorithm
        r = b % a  # remainder at each step of euclid's algorithm
        x2 = x - x1 * q  # updating x_i as explained below  x_i=(x_i-2)-(x_i-1)(q_i)
        y2 = y - y1 * q  # updating y_i as explained below  y_i=(y_i-2)-(y_i-1)(q_i)
        b = a  # updating b
        a = r  # updating a
        x = x1  # (x_i-2)=(x_i-1) updated by next value
        y = y1  # (y_i-2)=(y_i-1) updated by next value
        x1 = x2  # (x_i-1)=(x_i)   updated by next value
        y1 = y2  # (x_i-1)=(x_i)   updated by next value

    gcd = b

    return gcd, x, y


print(ext_gcd(10889992, 66))  # example

# Explanation of the algorithm (Mathematical approach)
# We can represent each step of the euclid's algorithm by : r_i=(q_i+2)*(r_i+1)+(r_i+2),
#                                                           where (q_i+2)=[(r_i)/(r_i+1)], [] is gif
#                                                           also r_0 =a and r_1=b (defined)
#  So, we can write r_i=(r_i-2)-(q_i)*(r_i-1), 0<= r_i < (r_i-1)  ---------------(1)
#  Now, we can write r_i =(x_i)*a + (y_i)*b
#  putting this in the recursive relation (1), above, we get: x_i=(x_i-2)-(x_i-1)(q_i)
#                                                        and  y_i=(y_i-2)-(y_i-1)(q_i)
# now for the initial values, : a=r_1=(x_0)*a + (y_0)*b , so x_0=1 and y_0=0
#                             : b=r_0=(x_1)*a + (y_1)*b , so x_1=0 and y_1=1
#  here gcd(a,b)=r_n-2=(x_n-2)*a + (y_n-2)*b
