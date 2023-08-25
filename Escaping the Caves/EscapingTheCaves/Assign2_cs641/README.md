# Level 2
#### **PlayFair Cipher** and **Morse Code**
## Steps to get to Cipher text
read - For the cipher text
go - For the key
## Decryption method used
Playfair Cipher was used to encrypt the ciphertext and Morse code was used for the encryption key, "SECURITY"
## Ciphertext
  TR XYCB MH AFC MUVY EOHPTCS, AFCSS TE QCSI NTYIMS TNA AFCSC. 
	EMRBH XAA VAFR MIUCQPUH "LMRL_CCETOT" FN HM AKUXAHK. OTA WANA
	OTXT FFU EISCWNAF HME BFU MCVA UGTOTRE. BM HYLF IFU UVTY ANE 
	HBSEI QYOQM OUVSF AM EAFTE PYHYS XNSKE IFUSC.
  
  And we had "... . -.-. ..- .-. .. - -.--" for the key.
## Decrypted text
BE WARY OF THE NEXT CHAMBER, THERE IS VERY LITTLE JOY THERE. SPEAK OUT THE PASSWORD "OPEN_SESAME" TO GO THROUGH. MAY YOU HAVE THE STRENGTH FOR THE NEXT CHAMBER. TO FIND THE EXIT YOU FIRST WILL NEED TO UTTER MAGIC WORDS THERE.
key: "SECURITY"
## Analysis
To decrypt the Morse code, we replaced each Morse code symbol by the corresponding alphabet and got the word "security".

To decrypt the text we first created a 5x5 key matrix (which we handled in the form of a list while coding). The cipher text was then divided into groups of 2 letters.

Then each pair was decrypted according to the following rules - 

1. If both letters were in the same row of the key matrix, they were substituted by the letters in the same row and previous column, wrapping around to the right side of the matrix if the letters were in the leftmost column. 

2. If both letters were in the same column of the key matrix, they were substituted by the letters in the same column and above row,  wrapping around to the bottom side of the matrix if the letters were in the top row.

3. If both the above conditions don’t hold, then both the letters are used to form a rectangle 
 and are substituted by the letters in the adjacent vertex but in the same row.

After substituting each pair of letters, the substituted letters were recombined to form the plaintext.
