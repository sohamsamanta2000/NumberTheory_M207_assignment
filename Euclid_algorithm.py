def gcd(a,b):
    a=max(a,b)  
    b=min(a,b)

    if b==0:       #base case
        return a   
    else:

        c=a        #temporary variable
        a=b       
        b=c%b    #updating b by, r_i+2 as explained below

        return gcd(a,b)

print( gcd(200,66)) #example


#algorithm explanation
# check whether b=0 or not 
        #this is will happen at the last step of euclid's algorithm, i.e when the nth remainder is zero (here b=nth remainder)
             #in this case a is the gcd
#else 
        #store b's value in a and the ith remainder in b (i.e. b=a%b)
        # then pass these modified values of a and b to the gcd function for further iteration.

#We can represent each step of the euclid's algorithm by : r_i=(q_i+2)*(r_i+1)+(r_i+2), 
#                                                           where (q_i+2)=[(r_i)/(r_i+1)], [] is gif
