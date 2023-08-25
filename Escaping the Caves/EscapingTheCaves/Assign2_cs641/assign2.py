text = 'TR XYCB MH AFC MUVY EOHPTCS, AFCSS TE QCSI NTYIMS TNA AFCSC. EMRBH XAA VAFR MIUCQPUH "LMRL_CCETOT" FN HM AKUXAHK. OTA WANA OTXT FFU EISCWNAF HME BFU MCVA UGTOTRE. BM HYLF IFU UVTY ANE HBSEI QYOQM OUVSF AM EAFTE PYHYS XNSKE IFUSC.'
key = ['S','E','C','U','R','I','T','Y']
cleaned = text.replace(" ","")
cleaned = cleaned.replace(",","")
cleaned = cleaned.replace(".","")
cleaned = cleaned.replace('"','')
cleaned = cleaned.replace("_","")

cleaned = [(cleaned[i:i+2]) for i in range(0, len(cleaned), 2)]
alpha = 'abcdefghiklmnopqrstuvwxyz'.upper()
for i in alpha:
    if i not in key:
        key.append(i)
print("key_matrix: ",key)
print("text_pair: ",cleaned)
#algo
def decrypt(key, pair):
    idx1 = key.index(pair[0])
    idx2 = key.index(pair[1])
    decrypt_pair = ''
    if idx1%5 == idx2%5 :
        decrypt_pair += key[(idx1+20)%25] + key[(idx2+20)%25]
    elif idx1//5 == idx2//5 :
        decrypt_pair += key[(idx1//5)*5 + (idx1-1)%5] + key[(idx2//5)*5 + (idx2-1)%5]
    else:
        decrypt_pair += key[(idx1//5)*5 + idx2%5] + key[(idx2//5)*5 + idx1%5]
    return decrypt_pair
decoded = ''
for i in cleaned:
    decoded += decrypt(key, i)

i = 0
j = 0
while j!=len(text):
    if not text[j].isalpha():
        decoded = decoded[:i]+text[j]+decoded[i:]
    i+=1
    j+=1
print("decrypted_text: ",decoded)
#BE WARY OF THE NEXT CHAMBER, THERE IS VERY LITTLE IOY THERE. SPEAK OUT XTHE PASSWORD "OPEN_SESAME" TO GO THROUGH. MAY XYOU HAVE THE STRENGTH FOR THE NEXT CHAMBER. TO FIND THE EXIT YOU FIRST WILXL NEXED TO UTTER MAGIC WORDS THERE.