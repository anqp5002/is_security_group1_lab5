RUN LAB RSA with c :
```
gcc rsa.c -o output.exe -lcrypto && ./output.exe 
```

Test GUI terminal with python.

```
python RSA.py
```


Tutorial test task6:

Install lib:
```
cp env-example .env 
pip install -r requiremnents.txt 
```

========= GET  .ENV VALUE ====================== 

STEP 1: Get certificates

Run:
```
        openssl s_client -connect portal.ptit.edu.vn:443 -showcerts
```
Save certificates
Server certificate → c0.pem

First certificate:

0 s:CN = *.ptit.edu.vn

Copy:

-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----
CA certificate → c1.pem

Second certificate:

1 s:CN = GlobalSign GCC R6 AlphaSSL CA 2023
STEP 2: Get public key from CA
Get modulus (n)
```
        openssl x509 -in c1.pem -noout -modulus
```
Get exponent (e)
```
        openssl x509 -in c1.pem -text -noout
```
Find:

Exponent: 65537
STEP 3: Get signature from server certificate
```
        openssl x509 -in c0.pem -text -noout
```
Find:

Signature Value:
Clean signature

Remove : and spaces.

Example:

ab:cd:12 → abcd12

Save to file:
```
        cat signature.txt | tr -d ':\n ' > sig_clean.txt
```
STEP 4: Extract certificate body
```
        openssl asn1parse -i -in c0.pem
```
Find line:

4:d=1 ...
Extract body
```
openssl asn1parse -i -in c0.pem -strparse 4 -out c0_body.bin -noout
```
STEP 5: Hash the body
```
        sha256sum c0_body.bin
```
This is the hash used by CA.


RUN : 
```
python task6.py
```