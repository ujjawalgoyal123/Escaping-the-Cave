# Level 5
### EAEAE cypher (Variant of AES)
## Steps to reach ciphertext
Go ---- Wave ---- dive ---- go ---- read --- password
## Decryption method used
The spirit says :
  "This is another magical screen. And this one I remember perfectly...
	Consider a block of size 8 bytes as 8 x 1 vector over F_{128} --
	constructed using the degree 7 irreducible polynomial x^7 + x + 1
	over F_2. Define two transformations: first a linear transformation 
	given by invertible 8 x 8 key matrix A with elements from F_{128} and 
	second an exponentiation given by 8 x 1 vector E whose elements are 
	numbers between 1 and 126. E is applied on a block by taking the ith 
	element of the block and raising it to the power given by ith element in E.
	Apply these transformations in the sequence EAEAE on the input block
	to obtain the output block. Both E and A are part of the key.
	You can see the coded password by simply whispering 'password' near 
	the screen..."
## Cipher text
lhiqigjniogigijtkfinfrjuhuffgrmq
## Decrypted password
twqxybopdk
## Analysis
### Observations:
1. We first tried out many inputs and then we found out that only certain inputs were being accepted. Hence, we arrived at the conclusion that a specific plaintext space existed and then we focused our efforts on trying to figure it out.
2. We then noticed that the output came out in the range of 16 letters from ‘f’ to ‘u’. The inputs which were being accepted consisted of these letters only.
3. Then we figured out that these letters represented 4 bits each with 0 as 'f', 1 as 'g' and so on till 15  as 'u'. We also noticed that along with the vector E which had elements from 1-126, we were also given a field F<sub>128</sub> which translates to 7 bytes whereas the input mentioned in the question was of 8 bytes.
4. Hence, we figured out that each byte of the input was from ’ff’ to ‘mu’ mapping 0 to 127. We also found that each byte had the signed bit or the most significant bit as 0. Upon further trial and inspection, we found that there was a padding of 'ff'. For example, when  'fg' and 'fgffffffffffffff' were given as inputs we obtained the same output.
5. It was further observed that by giving various inputs that had a few starting bytes as 'ff' and then changing the bytes, the output came out with the same number of starting bytes as 'ff' and the remaining bytes were encrypted. That is, for instance, for the input 'ffffhgmoklfgfhfm' we got the output 'ffffkukshmiritmn'. This indicated that the linear transformation matrix was a lower triangular matrix.
### Decryption:
1. We then generated inputs.txt and the corresponding output.txt of the form C<sub>8-i</sub>PC<sub>i-1</sub> using in_out_gen.ipynb, where C = 'ff' and P∈ ['fg', 'mu' ] .
2. Now, we conducted an iteration on every feasible value of diagonal elements and exponents as due to the input format used by us, only 1 block was non-zero per input. If a non-zero block i had the value x, then its output had the value O = (a<sub>i,i</sub>(a<sub>i,i</sub> * x<sup>e<sub>i</sub></sup>)<sup>e<sub>i</sub></sup>)<sup>e<sub>i</sub></sup> (Because A is lower triangular). Then using x<sup>7</sup> + x + 1 as a generator, operations were applied over the field F<sub>128</sub>, and this was subsequently utilised in decrypt.ipynb.
3. We then iterated across all values of e<sub>i</sub> and a<sub>i,i</sub> for every plaintext and ciphertext combination and analysed the result. 
4. All possible pairs of (e<sub>i</sub> and a<sub>i,i</sub>) values were stored and per block there were approximately 3 pairs. 

      |Blocknumber|(a<sub>i,i</sub>,e<sub>i</sub>)|
      |-------------|---------------------------------|
      | 0 | (84,20),(67,108) |
      | 1 | (72,53),(101,83),(70,118) |
      | 2 | (43,40),(14,89),(72,125) |
      | 3 | (6,11),(9,34),(12,82) |
      | 4 | (103,2),(8,38),(112,87) |
      | 5 | (17,29),(110,43),(11,55) |
      | 6 | (27,22),(66,37),(70,68) |
      | 7 |(104,1),(38,19),(38,107) |

5. To proceed further we had to find the non-diagonal elements and also we had to eliminate pairs. So we used some more plaintext and ciphertext combinations and then iterated over the above pairs to find elements within 0 to 127, for which the equation O was valid. a<sub>i,j</sub> was calculated with the help of a<sub>i,i</sub> and a<sub>j,j</sub> in a triangular manner.
6. We then obtained all elements next to the diagonal elements.

      | Block number | a<sub>i,i</sub> | e<sub>i</sub> |
      |---|---|---|
      | 0 | 84 | 20 |
      | 1 | 70 | 118 |
      | 2 | 43 | 40 |
      | 3 | 12 | 82 |
      | 4 | 112 | 87 |
      | 5 | 11 | 55 | 
      | 6 | 27 | 22 |
      | 7 | 38 | 19 |

7. Only for some specific pairs could we find the value of elements next to the diagonal elements, which enabled us to reduce the feasible pairs to an element each. Then all the elements of the matrix were obtained by iterating over all the available values form 0-127 using the final E vector and the previously obtained values of the vector A, and verified the correctness of function O.
8. Hence, we obtained the Linear Transformation Matrix A:

                                                  [84  0   0   0   0   0   0   0] 
                                                  [114 70  0   0   0   0   0   0] 
                                                  [14  28  43  0   0   0   0   0]
                                              A = [123 27  31  12  0   0   0   0] 
                                                  [97  39  3   108 112 0   0   0] 
                                                  [31  40  29  54  110 11  0   0] 
                                                  [17  121 20  101 4   83  27  0] 
                                                  [95  13  83  25  14  68  4  38]
                                                  
And the Exponent Matrix E:

                                              E = [20  118  40  82  87  55  22  19]
                                              
9. Similarly we decrypted the password, i.e. we iterated upon every feasible value for a block. We then matched our password with the output of the EAEAE function. This was done in two parts. We then obtained the decrypted password as 'twqxybopdk000000'. We figured that the '0's were used for padding thus the password obtained is :
**twqxybopdk**
