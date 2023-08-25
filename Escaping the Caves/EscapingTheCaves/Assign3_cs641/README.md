# Level 3
### Decryption using Group theory, modular arithematic
## Steps to reach cipher text
Enter -- Enter --- pick --- press c -- press c --  back ---- give --- note down the key, "thrnxxtyz" ---- back --- back ---- insert the key "thrnxxtyz"---- read
## Problem and Ciphertext
    Password for this level is an element of the multiplicative
	  group Z_p^* where p = 19807040628566084398385987581 is a prime. 
    You carefully look around and find three pairs of numbers of the
    form (a, password * g^a) where g is a element in Z_p^* and a is 
    an integer. The g in each pair is the same.

      (324,  11226815350263531814963336315)
      (2345, 9190548667900274300830391220)
      (9513, 4138652629655613570819000497)

    You desperately start searching for more numbers and find

      1___4_2______0___94____9

    This looks like g but most of the entries are missing. Speak 
    out the password loudly to pass this level!
## Decrypted password
    3608528850368400786036725
## Analysis
We figured out the password using modular arithmetic. 
<br>p = 19807040628566084398385987581

a_x = 324, x = 11226815350263531814963336315

a_y = 2345, y = 9190548667900274300830391220

a_z = 9513, z = 4138652629655613570819000497

Now, <br>
(password*(g^a_x)) mod p = x     --- equation 1<br>
(password*(g^a_y)) mod p = y     --- equation 2<br>
(password*(g^a_z)) mod p = z       --- equation 3<br>

Now, <br>(password*(g^a_x)) mod p = x<br>
=> (password \* ( (g^a_x) mod p ) ) mod p = x<br>
=> inverse(x) \* (password \* ( (g^a_x) mod p ) ) mod p = x\*inverse(x)<br>
=> password \*( ( (g^a_x) mod p) \* inverse(x) ) mod p  = 1<br>


Using Eq. 1 and 2<br>
( g^(a_y - a_x) ) mod p = (y\*inverse(x)) mod p

Using Eq. 1 and 3<br>
( g^(a_z - a_y) ) mod p = (z*\inverse(y)) mod p


Solving (a_y - a_x) \* u + (a_z - a_y) \* v = 1, we obtain the values of u and v.<br>
u = 493<br>
v = -139

Now, g = ( ( (y\*inverse(x))^u )  \*  ( (z\*inverse(y))^v )  ) mod p<br>
g = 192847283928500239481729<br>
By substituting the value of g in equation 1, equation 2 and equation 3, and solving we get the common value as the password.<br>
