#pragma once
#include <openssl/bn.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

void hexToByteArray(const char *hexString, unsigned char *byteArray)
{
    int len = strlen(hexString);

    for (int i = 0; i < len; i += 2)
    {
        char temp[3] = {hexString[i], hexString[i + 1], '\0'};

        byteArray[i / 2] = (unsigned char)strtol(temp, NULL, 16);
    }
}

void ByteArrayToHex(unsigned char *byteArray, char *hexString)
{
    // Tự tính độ dài bên trong hàm
    int len = (int)strlen((char *)byteArray);

    for (int i = 0; i < len; i++)
    {
        sprintf(hexString + (i * 2), "%02x", byteArray[i]);
    }
    hexString[len * 2] = '\0';
}

void printBN(char *msg, BIGNUM *a)
{
    // Convert the BIGNUM to number string
    char *number_str = BN_bn2dec(a);
    // Print out the number string

    printf("%s %s\n", msg, number_str);
    // Free the dynamically allocated memory
    OPENSSL_free(number_str);
}


void printBNtoHex(char *msg, BIGNUM * a)
{
// Convert the BIGNUM to number string
char * number_str = BN_bn2hex(a);
// Print out the number string

printf("%s %s\n", msg, number_str);
// Free the dynamically allocated memory
OPENSSL_free(number_str);
}