import os 
import platform
def menu():
    print("===========MENU===========")
    print("1. CHECK d ")
    print("2. ENCRYPT")
    print("3. DECRYPT")
    print("4. SIGNING")
    print("5. VERIFY")
    print("0. EXIT")

def calcd(p, q, e):
    phi = (p - 1) * (q - 1)
    try:
        return pow(e, -1, phi)
    except ValueError:
        return None # e không nguyên tố cùng nhau với phi


def encrypt(messageInt , e,n ):
    return pow(messageInt, e,n);

def decrypt(c ,   d , n ):
    return pow(c,d,n)

def signing(messgaeInt ,d ,n ):
    return encrypt(messgaeInt ,  d, n)

def verify(c, e,n):
    return decrypt(c, e,n)

if __name__ == "__main__":

    print("input hex(p) : ")
    p = int(input().strip(), 16)
    print("input hex(q) : ")
    q = int(input().strip(), 16)
    print("input hex(e) : ")
    e = int(input().strip() , 16)
    d=  calcd(p,q,e)
    n= p*q
    while True:
        os.system("cls" if platform.system() == "Windows" else "clear")
        menu()
        ip = input()
        
            
        match ip: 
            case "0":
                print("Chuong trinh da ket thuc ")
                break
            case "1":
                print("d = " +  str(d))
                input("Nhan nut bat ki de thoat")
            case "2":
                message = input("input message:  ")
                messageInt = int(message.encode("utf-8").hex(),16)
                c = encrypt(messageInt ,e,n )
                print("n = " + str(n))
                print("e = " + str(e))
                print("M = " + message)
                print("c = "+  str(c))
                print("Note: pls copy c value")
                input("Nhan nut bat ki de thoat")
            case "3":
                c = int(input("input int(c)  : "))
                decryptCode = decrypt(c,d,n)
                print("decrypt code int : " +  str(decryptCode))
                so_byte = (decryptCode.bit_length() + 7) // 8
                mang_byte = decryptCode.to_bytes(so_byte, byteorder='big')

                chuoi_ban_dau = mang_byte.decode('utf-8')
                print("message decrypted  =  " + chuoi_ban_dau)  # Kết quả: 'Hello'
                input("Nhan nut bat ki de thoat")

            case "4":

                message = input("Input message : ")
                messageInt = int(message.encode("utf-8").hex(),16)
                S = signing(messageInt ,d,n )
                print("hex(M) = " + str(hex(messageInt)))
                print("S = " + str(S))
                print("Note: pls copy S value")

                input("Nhan nut bat ki de thoat")

            case "5":
                S = int(input("input int(S)  : " ))
                verifyCode = verify(S,e,n)
                print("verify code int" +  str(verifyCode))
                so_byte = (verifyCode.bit_length() + 7) // 8
                mang_byte = verifyCode.to_bytes(so_byte, byteorder='big')

                chuoi_ban_dau = mang_byte.decode('utf-8')
                print("message verifyied = " + chuoi_ban_dau)
                input("Nhan nut bat ki de thoat")

            case _:
                print("Wrong option! please try again")
        print("hello")
        
        