#include <openssl/bn.h>
#include <stdio.h>
#include<string.h>
#include "lib.c"



void task1(BIGNUM *p , BIGNUM *q , BIGNUM *e, BIGNUM *d, BN_CTX *ctx, BIGNUM * one ){

    printf("\n\n==================  TASK 1  ==================\n\n");

    
    BIGNUM *pSubOne = BN_new();
    BIGNUM *qSUbOne = BN_new();
    
    BIGNUM *phi = BN_new();

    // declare  p -1 , q-1 
    BN_sub(pSubOne , p , one);
    BN_sub(qSUbOne, q, one);
    

    // phi(n) = (p-1)*(q-1)
    BN_mul(phi, pSubOne, qSUbOne , ctx);    
    
    // d : e.d = 1 (mod phi)

    BN_mod_inverse(d, e,phi,ctx);

}

// encrypt
void task2(char *message , BIGNUM *n , BIGNUM *e, BIGNUM *d, BN_CTX *ctx ,BIGNUM *c){
    printf("\n\n==================  TASK 2  ==================\n\n");
    
    char messageToHex [100000];
    ByteArrayToHex(message, messageToHex);
    BIGNUM *messageToBIGNUM = BN_new();
    BN_hex2bn(&messageToBIGNUM , messageToHex);

    // c = m^e % n 
    BN_mod_exp(c , messageToBIGNUM, e,n , ctx);
}

void task3(BIGNUM *c , BIGNUM *d , BIGNUM *n , BN_CTX  * ctx, BIGNUM *m){

    printf("\n\n==================  TASK 3  ==================\n\n");

    BN_mod_exp(m , c, d, n, ctx );
}

void task4(BIGNUM *d, BIGNUM *c, BIGNUM *n , BN_CTX *ctx , char * M ,char *MHex , BIGNUM *MSign){

    printf("\n\n==================  TASK 4  ==================\n\n");

    ByteArrayToHex(M , MHex);
    // signing message 
    // s  =  m^d % n
    BIGNUM *MHexToBN =  BN_new();
    BN_hex2bn(&MHexToBN , MHex);
    BN_mod_exp(MSign,MHexToBN , d,n,ctx);
}

void task5(BIGNUM *e, BIGNUM *n , BN_CTX *ctx , BIGNUM *MVerifyBN , BIGNUM *MSign , char * MVerifyMessage){

    printf("\n\n==================  TASK 5  ==================\n\n");

    BN_mod_exp(MVerifyBN, MSign , e, n , ctx);
    char *MVerifytoHex = BN_bn2hex(MVerifyBN);
     hexToByteArray(MVerifytoHex,MVerifyMessage);
}
int main(){

    BIGNUM *p = BN_new();
    BIGNUM *q = BN_new();
    BIGNUM *e = BN_new();
    BIGNUM *one = BN_new();
    BN_CTX *ctx = BN_CTX_new();
    BIGNUM *d = BN_new();
    BIGNUM * n = BN_new();

    // declare  p  , q , e
    BN_hex2bn(&p ,"F7E75FDC469067FFDC4E847C51F452DF");
    BN_hex2bn(&q, "E85CED54AF57E53E092113E62F436F4F");
    BN_hex2bn(&e,"0D88C3");
    
    printf("q hex is  : F7E75FDC469067FFDC4E847C51F452DF\n");
    printf("p hex is : E85CED54AF57E53E092113E62F436F4F\n");

    printBN("q dec is : " , q);
    printBN("p dex is : ", p);
    // declare 1 
    BN_dec2bn(&one, "1");

    // declare n : public key
    BN_mul(n, p, q , ctx);
    printf("\n\n(e , n = p*q) is public key : \n");

    printBN("   - e : ", e);
    printBN("   - n : ", n);



    // TASK 1 : FIND d 

    task1(p,q,e,d,ctx,one);
    printBN("d =  " ,d);


    // TASK 2 : encrypt 


    char message [] = "A top secret!";
    BIGNUM *c = BN_new();

    task2(message,n,e,d,ctx,c);
    printf("message is : %s\n", message);
    printBN("n = " , n);
    printBN("e = ", e);
    printf("M =  %s\n",message );
    printBN("c = " , c);


    // TASK 3 : decrypt 

    BIGNUM *m_reverse = BN_new();
    task3(c,d,n,ctx , m_reverse);
    printBN( "m_reverse  = " , m_reverse);
    char byteArray  [1000];
    hexToByteArray(BN_bn2hex(m_reverse) , byteArray);
    printf("M decrypt = %s" , byteArray);

    // task 4 : signing 
    char *M= "I owe you $2000.";
    char MHex[10000];
    BIGNUM *MSign = BN_new();

    char *M1= "I owe you $3000.";
    char M1Hex[10000];
    BIGNUM *M1Sign = BN_new();

    task4(d,c,n,ctx,M,MHex,MSign);
    task4(d,c,n,ctx,M1,M1Hex,M1Sign);
    
    printf("M = %s\n" , M);
    printf("M1 = %s\n" , M1);
    printf("M  hex = %s\n" , MHex);
    printf("M1 hex = %s\n" , M1Hex);
    printBN("M  sign = " , MSign);
    printBN("M1 Sign = " , M1Sign);
    //  TASK 5
 
    
    BIGNUM *MVerifyBN = BN_new();
    char MVerifyMessage[100];

    task5(e,n,ctx,MVerifyBN,MSign,MVerifyMessage);

    
    BIGNUM *M1VerifyBN = BN_new();
    char M1VerifyMessage[100];

    task5(e,n,ctx,M1VerifyBN,M1Sign,M1VerifyMessage);

    printBN("M  verify = " , MVerifyBN);
    printBN("M1 verify = " , M1VerifyBN);

    printf("M  verify message = %s \n" , MVerifyMessage );
    printf("M1 verify message = %s \n" , M1VerifyMessage );
}