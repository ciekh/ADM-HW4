import math
import sympy
import numpy as np
import time
from datetime import datetime

# Let's calculate how many hash function we need:

def choose_size_and_hash(p, n):

    m = -n * math.log(p)/(math.log(2))**2 # Size of the bit array
    
    for num in range(int(m), 10000000000001): # Find the fist prime number after that size 
        if sympy.isprime(num):
            m = num
            break
    
    k = math.ceil(m/n*math.log(2)) # Number of hash functions
    gamma = n/m # ration beetween all elements and the bit array size, it should be under 0.5

    print("Number of hash functions we need:", k, "\nBit Array size: ", m, 
          "\nIs the probability of False Positive is minimized?", bool(gamma < 0.5))

    return [m, k]

# Let's create the hash functions:

def hash1(word, coeff, m):
    
    a = coeff[0:20]
    h = 0
    for i in range(len(word)):
        h += ord(word[i])*a[i] # ord returns the ascii code
        #h += ord(word[i])*a[0]**(len(word)-i) # Alternative version, slower
        
    return h % m # we get as index the mod between hash and the prime number we have choosen as size of the bit array


def hash2(word, coeff, m):
    
    a = coeff[20:40]
    h = 0
    for i in range(len(word)):
        h += ord(word[i])*a[i]
        #h += ord(word[i])*a[1]**(len(word)-i)
        
    return h % m

def hash3(word, coeff, m):
    a = coeff[40:60]
    h = 0
    for i in range(len(word)):
        h += ord(word[i])*a[i]
        #h += ord(word[i])*a[2]**(len(word)-i)
        
    return h % m

def hash4(word, coeff, m):
    
    a = coeff[60:80]
    h = 0
    for i in range(len(word)):
        h += ord(word[i])*a[i]
        #h += ord(word[i])*a[3]**(len(word)-i)
        
    return h % m

def hash5(word, coeff, m):
    
    a = coeff[80:100]
    h = 0
    for i in range(len(word)):
        h += ord(word[i])*a[i]
        #h += ord(word[i])*a[4]**(len(word)-i)
        
    return h % m

def hash6(word, coeff, m):
    
    a = coeff[100:120]
    h = 0
    for i in range(len(word)):
        h += ord(word[i])*a[i]
        #h += ord(word[i])*a[5]**(len(word)-i)
        
    return h % m

def hash7(word, coeff, m):
    a = coeff[120:140]
    h = 0
    for i in range(len(word)):
        h += ord(word[i])*a[i]
        #h += ord(word[i])*a[6]**(len(word)-i)
        
    return h % m

def bloom_indexes(word, coeff, m): # Call all functions in one shot
    
    return [hash1(word, coeff, m), hash2(word, coeff, m), hash3(word, coeff, m), 
            hash4(word, coeff, m), hash5(word, coeff, m), hash6(word, coeff, m), 
            hash7(word, coeff, m)] # Returns an array with all indexes produced by the hash functions

# Let's create the filter:

def CreateFilter(lst_pw, bloom, coeff, m):

    now = datetime.now()
    
    print("\nStart to create the Bloom Filter ", "at ", now.hour, ":", now.minute, ":", now.second, "\n", sep="")
    
    
    count = 0        
    start = time.time() # The beginning of the process
    time_lst = [] # it is useful to get everytime the moment in which we are
    
    for pw in lst_pw:
        
        # In each iteration we switch to 1 the positions in the filter given by hasehs:
        
        i1, i2, i3, i4, i5, i6, i7 = bloom_indexes(pw,coeff, m) 
        bloom[i1] = 1
        bloom[i2] = 1
        bloom[i3] = 1
        bloom[i4] = 1
        bloom[i5] = 1
        bloom[i6] = 1
        bloom[i7] = 1
        
        # This code needs only to interact with the user, TO BE AWARE AT WHICH POINT THE FILTER IS
        
        if count % 10000000 == 0 and count != 0:
            end = time.time()
            this_tot_time = round((end - start)/60, 2)
            current_time = datetime.now()
            print("Local Time: ", current_time.hour, ":", current_time.minute, ":", current_time.second,
                  "\nTot. time: ", round(sum(time_lst) + this_tot_time,2), " minutes",
                  "\nTime needed for this millions: ", this_tot_time, " minutes",
                  "\nN. elements: ", count, "\nPercentage: ", round(count/100000000*100, 2), "%\n", sep="")
            time_lst.append(this_tot_time)
            start = end
        
        if count == 100000000:
            end = time.time()
            this_tot_time = round((end - start)/60, 2)
            print("Bloom Filter has been created!", "\nTot. time:", round(sum(time_lst) + this_tot_time, 2), "minutes", "\n")
        
        count += 1
    
# Check passwords function:
        
def CheckPass(to_check, bloom, coeff, m):
    
    now = datetime.now()
    
    print("Start to check the passwords ", "at ", now.hour, ":", now.minute, ":", now.second, "\n", sep="")
    
    start = time.time()
    time_lst = []
    count = 0
    match = [] # List of passwords present in both files
        
    for pw in to_check:
            
        # Transform the password with the hash functions:
        
        i1, i2, i3, i4, i5, i6, i7= bloom_indexes(pw, coeff, m)
            
        # We say that there the password maybe in the file only if all position given by the indexes are ones:
        
        if bloom[i1] == 1 and bloom[i2] == 1 and bloom[i3] == 1 and bloom[i4] and bloom[i5] == 1 and bloom[i6] == 1 and bloom[i7] == 1:
            match.append(pw) # Add to the list of passwords contained in both files
            
        if count % 10000000 == 0 and count != 0:
            end = time.time()
            this_tot_time = round((end - start)/60, 2)
            current_time = datetime.now()
            print("Local Time: ", current_time.hour, ":", current_time.minute, ":", current_time.second,
                  "\nN. elements scanned: ", count,
                  "\nTime needed for this millions: ", this_tot_time, " minutes", 
                  "\nTot. time: ", round(sum(time_lst) + this_tot_time, 2), " minutes",
                  "\nProcess Done: ", round(count/39000000*100, 2), "%", 
                  "\nNumber of elements founded: ", len(match), "\n", sep="")
            time_lst.append(this_tot_time)
            start = end
            
        if count == 39000000:
            print("All passwords have been checked!", "\nTot. Password founded:", len(match), "\n")
            
        count += 1
        
    return match