# Level 4
### Breaking 6 round Data Encryption Standard using 3 round Characterstic
## Steps to reach the Cipher
We used, go ---- jump ---- jump ---- back ---- pull, to get the magic wand. Then we went to level 3 of the game and used the command 'enter' ---- 'wave'. The spirit came out to help us and we came back again to level 4 and used the command read to get the problem statement.
## Cryptosystem
We used DES 6 cryptosystem - sixth level DES. Differential Cryptoanalysis.
## Analysis
1) On the first screen, there was a panel nearby so we used read but nothing was written on that panel. So, we used enter. On the next screen, we were at the edge of the lake so we used jump. We again came out. So, we jump again. There we see magic wand and tried pull but went out of breath and died. So, we entered the above commands again and the instead of pull we used back and then used dive again. Now, we use pull and got the wand.

2) Now, we went back to the first screen using series of back. And tried read but it was still empty. After a while we figured out that it has something to do with the chapter name which is THE SPIRIT and there was a spirit in level 3.
So, we went back to level 3 and used enter and reached second screen where we used wave and freed the spirit. Then from the first screen of 4th chapter we used read and we got the question read by spirit.

3) It said this is either 4,6 or 10 rounds DES. As 10 rounds is very difficult to break and 4 rounds would be easy to break. So, we started with 6 round thinking if this won't work then we can use the similar analysis for 4 round DES.
It was given that two letters were for one byte and DES has a block size of 64 bits or 8 bytes. So, 16 letters represented 1 block size.

4) After trying many inputs, we found that 16 letters in the output are from 'f to 'u'. Also, we considered that input also consists of these letters only as only 16 letters could be represented by four bits and each alphabet was mapped with a number from 0 to 15.

5) We used differential iterative characteristic of 6-round DES 405c0000 04000000 to break the code, which gives the differential '00540000 04000000' after 4 rounds with probability 0.000381. For this we need approximately around one lakh pairs of plaintext & cipher text.

6) We used inputgen.ipynb to generate one lakh random inputs and also to get input pairs whose XOR is equal to "0000901010005000' which we get from inverse initial permutation of '405c0000 04000000' and it is stored in inputs.txt. Now we used assign4.ipynb to generate ciphertext corresponding to inputs we just generated and stored them in outputs.txt. (Server was crashing thus we could generate lesser pairs compared to input [Around 2000] but we made sure that pairs aren't affected)

7) Now we use diff_crypt.ipynb where first we reverse final permutation of block R6 to get the output of the sixth round of the DES (let's say it as xor_outs). We then find out the output differentials (i.e. the XOR of alternate pairs of xor outs). The xor outs's left half is equal to the right half output of round 5. So, we expand that to get the input differential of the S-Boxes (the differential doesn't get changed after key XORing) . Now, we inverse permuted the right half of the xor outs to get the S-Box's output differential . From every two entries in xero outs (Out1, Out2) we extract the left half of Out, expand it and store it . 

8) In sbox_phase.ipynb, for every correct possible corresponding input-output differential pairs we can extract the 6-bit key set corresponding to that S-Box. This is done in the following manner: For every entry in XS_inp, we generate input pairs for each S-Box so that the XOR of the two inputs is equal to that iteration's XS_inp value (let them be s_inp1 and s_inp1 ). And if the output pair XOR is equal to the that iteration's XS_out value, we update the counter of XEXP out text
XOR s_inp1 (that is the corresponding key bits for that S-Box). After the complete iteration over XS inp, we then find out the 6 bit key sets for each S-Box that are highly probable. The stats of the 6-bit key values is given for each S-Box.

9) Now, we get 6 blocks values out of 8 blocks as their frequency is way above mean. But we cannot get key from S-Boxes S3 and S4. So, now we have knowledge of 36 bits out of 56 bits. We then use the permutation using key scheduling and map it in the latter half of sbox_phase.ipynb. Next, we apply brute force on the remaining 20 bits of the key.
Using these we got the key 01110000001010000010010001011010001010101101010101010001

10) Then we ran Decryption function from DES implementation for 6 Rounds for 16 letters (8 Bytes) at a time and decrypt the password using the key which came out in numbers. We tried mapping it back to characters using the initial mappings 'f' to 'u'. But, unfortunately the resultant password didn't help in passing the level. We thought that these numbers may be ASCII codes but we didn't pass the level assuming that too.
