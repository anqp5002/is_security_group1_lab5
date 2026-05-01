"""
Cryptography Toolkit - Main Entry Point
Lab 5 - Nhóm 1 - Bảo Mật Thông Tin - PTIT

Unified toolkit kết hợp tất cả modules:
  - Symmetric Encryption (AES / 3DES)  -- TV2: N23DCCN071 Hoàng Anh
  - Asymmetric Encryption (RSA)         -- TV1: N23DCCN001 Đặng Kim An
  - Hash Functions (MD5 / SHA-256)     -- TV4: N23DCCN138 Phạm Quốc An
"""

import os
import sys
import platform
import config

# Fix encoding cho Windows terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ============================================================
#                   INTERNAL MODULE IMPORTS
# ============================================================

# -- AES / 3DES (TV2: N23DCCN071 Hoàng Anh) --
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "N23DCCN071_hoanganh", "AES_3DES"))
from app.symmetric import (
    generate_key as _generate_symmetric_key,
    encrypt_data as _encrypt_symmetric,
    decrypt_data as _decrypt_symmetric,
)

# -- Hash Functions (TV4: N23DCCN138 Phạm Quốc An) --
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "N23DCCN138_PhamQuocAn"))
from hashing.md5_hash import compute_md5, compute_md5_file, md5_menu
from hashing.sha256_hash import compute_sha256, compute_sha256_file, sha256_menu
from hashing import compare_hashes as _compare_hashes

# ============================================================
#                   UTILITY FUNCTIONS
# ============================================================

def clear_screen():
    os.system(config.get_clear_screen_cmd())


def pause(message: str = "Nhan Enter de tiep tuc..."):
    input(f"\n{message}")


def _message_to_int(message: str) -> int:
    """Convert text message to integer (hex representation)."""
    return int(message.encode("utf-8").hex(), 16)


def _int_to_message(value: int) -> str:
    """Convert integer back to text message."""
    byte_count = (value.bit_length() + 7) // 8
    return value.to_bytes(byte_count, byteorder="big").decode("utf-8")


# ============================================================
#                   RSA HELPERS (TV1: N23DCCN001)
# ============================================================

def _rsa_calculate_d(p: int, q: int, e: int) -> int | None:
    """Calculate private exponent d = e^(-1) mod phi(n)."""
    phi = (p - 1) * (q - 1)
    try:
        return pow(e, -1, phi)
    except ValueError:
        return None


def _rsa_encrypt(m_int: int, e: int, n: int) -> int:
    """RSA encryption: c = m^e mod n."""
    return pow(m_int, e, n)


def _rsa_decrypt(c: int, d: int, n: int) -> int:
    """RSA decryption: m = c^d mod n."""
    return pow(c, d, n)


def _rsa_sign(m_int: int, d: int, n: int) -> int:
    """RSA signing: s = m^d mod n (same as encrypt with private key)."""
    return pow(m_int, d, n)


def _rsa_verify(s: int, e: int, n: int) -> int:
    """RSA verification: m = s^e mod n (same as decrypt with public key)."""
    return pow(s, e, n)


# ============================================================
#                   MENU: SYMMETRIC ENCRYPTION
# ============================================================

def symmetric_encrypt_menu():
    """Menu mã hóa đối xứng."""
    while True:
        clear_screen()
        print("\n╔══════════════════════════════════════╗")
        print("║   SYMMETRIC ENCRYPTION MENU        ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. AES Encrypt / Decrypt           ║")
        print("║  2. 3DES Encrypt / Decrypt         ║")
        print("║  0. Quay lai Main Menu              ║")
        print("╚══════════════════════════════════════╝")
        choice = input("Chon: ").strip()

        match choice:
            case "1":
                _aes_menu()
            case "2":
                _tdes_menu()
            case "0":
                break
            case _:
                print("  [LOI] Lua chon khong hop le!")
                pause()


def _aes_menu():
    """Menu AES."""
    while True:
        clear_screen()
        print("\n╔══════════════════════════════════════╗")
        print("║          AES MENU                   ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Tao key ngau nhien              ║")
        print("║  2. Ma hoa (Encrypt)                ║")
        print("║  3. Giai ma (Decrypt)              ║")
        print("║  0. Quay lai                       ║")
        print("╚══════════════════════════════════════╝")
        choice = input("Chon: ").strip()

        match choice:
            case "1":
                key = _generate_symmetric_key("AES")
                print(f"\n  Key AES (Base64): {key}")
                pause()

            case "2":
                plaintext = input("  Nhap plaintext: ").strip()
                auto = input("  Tao key ngau nhien? (y/n): ").lower().strip()
                key = _generate_symmetric_key("AES") if auto == "y" else input("  Nhap key (Base64): ").strip()
                result = _encrypt_symmetric("AES", plaintext, key)
                if result.startswith("Loi"):
                    print(f"\n  [LOI] {result}")
                else:
                    print(f"\n  Ciphertext (Base64): {result}")
                pause()

            case "3":
                ciphertext = input("  Nhap ciphertext (Base64): ").strip()
                key = input("  Nhap key (Base64): ").strip()
                result = _decrypt_symmetric("AES", ciphertext, key)
                if result.startswith("Loi"):
                    print(f"\n  [LOI] {result}")
                else:
                    print(f"\n  Plaintext: {result}")
                pause()

            case "0":
                break
            case _:
                print("  [LOI] Lua chon khong hop le!")
                pause()


def _tdes_menu():
    """Menu 3DES."""
    while True:
        clear_screen()
        print("\n╔══════════════════════════════════════╗")
        print("║         3DES MENU                   ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Tao key ngau nhien              ║")
        print("║  2. Ma hoa (Encrypt)                ║")
        print("║  3. Giai ma (Decrypt)              ║")
        print("║  0. Quay lai                       ║")
        print("╚══════════════════════════════════════╝")
        choice = input("Chon: ").strip()

        match choice:
            case "1":
                key = _generate_symmetric_key("3DES")
                print(f"\n  Key 3DES (Base64): {key}")
                pause()

            case "2":
                plaintext = input("  Nhap plaintext: ").strip()
                auto = input("  Tao key ngau nhien? (y/n): ").lower().strip()
                key = _generate_symmetric_key("3DES") if auto == "y" else input("  Nhap key (Base64): ").strip()
                result = _encrypt_symmetric("3DES", plaintext, key)
                if result.startswith("Loi"):
                    print(f"\n  [LOI] {result}")
                else:
                    print(f"\n  Ciphertext (Base64): {result}")
                pause()

            case "3":
                ciphertext = input("  Nhap ciphertext (Base64): ").strip()
                key = input("  Nhap key (Base64): ").strip()
                result = _decrypt_symmetric("3DES", ciphertext, key)
                if result.startswith("Loi"):
                    print(f"\n  [LOI] {result}")
                else:
                    print(f"\n  Plaintext: {result}")
                pause()

            case "0":
                break
            case _:
                print("  [LOI] Lua chon khong hop le!")
                pause()


# ============================================================
#                   MENU: RSA
# ============================================================

def rsa_menu():
    """Menu RSA - ket hop TV1."""
    # Precomputed from config
    p = config.RSA_P
    q = config.RSA_Q
    e = config.RSA_E
    n = config.RSA_N
    d = _rsa_calculate_d(p, q, e)

    if d is None:
        print("\n  [LOI] Khong the tinh private exponent d!")
        pause()
        return

    while True:
        clear_screen()
        print("\n╔══════════════════════════════════════╗")
        print("║     RSA ASYMMETRIC ENCRYPTION        ║")
        print("╠══════════════════════════════════════╣")
        print(f"║  p (hex): {config.RSA_P_HEX}     ║")
        print(f"║  q (hex): {config.RSA_Q_HEX}     ║")
        print(f"║  e     : {e} (0x{e:X})         ║")
        print(f"║  n     : {n} (={p*q})    ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Tinh d (private exponent)       ║")
        print("║  2. Ma hoa (Encrypt)                ║")
        print("║  3. Giai ma (Decrypt)               ║")
        print("║  4. Ky so (Sign)                   ║")
        print("║  5. Xac minh (Verify)               ║")
        print("║  0. Quay lai Main Menu             ║")
        print("╚══════════════════════════════════════╝")
        choice = input("Chon: ").strip()

        match choice:
            case "1":
                print(f"\n  n = p * q = {n}")
                print(f"  d = e^(-1) mod phi(n) = {d}")
                print(f"  Public Key (e, n) = ({e}, {n})")
                print(f"  Private Key (d, n) = ({d}, {n})")
                pause()

            case "2":
                message = input("  Nhap message: ").strip()
                m_int = _message_to_int(message)
                c = _rsa_encrypt(m_int, e, n)
                print(f"\n  Message: {message}")
                print(f"  m (hex): {hex(m_int)}")
                print(f"  c = m^e mod n: {c}")
                pause()

            case "3":
                c = int(input("  Nhap ciphertext (c): ").strip())
                m = _rsa_decrypt(c, d, n)
                try:
                    message = _int_to_message(m)
                    print(f"\n  c = {c}")
                    print(f"  m (hex): {hex(m)}")
                    print(f"  Message: {message}")
                except Exception:
                    print(f"\n  [LOI] Khong the giai ma thanh text.")
                    print(f"  m (hex): {hex(m)}")
                pause()

            case "4":
                message = input("  Nhap message can ky: ").strip()
                m_int = _message_to_int(message)
                s = _rsa_sign(m_int, d, n)
                print(f"\n  Message: {message}")
                print(f"  m (hex): {hex(m_int)}")
                print(f"  Signature s = m^d mod n: {s}")
                print(f"  Signature (hex): {hex(s)}")
                pause()

            case "5":
                try:
                    s = int(input("  Nhap signature (s): ").strip())
                except ValueError:
                    print("  [LOI] Signature phai la so nguyen.")
                    pause()
                    continue
                m_recovered = _rsa_verify(s, e, n)
                try:
                    recovered_msg = _int_to_message(m_recovered)
                    print(f"\n  s = {s}")
                    print(f"  Recovered m (hex): {hex(m_recovered)}")
                    print(f"  Recovered message: {recovered_msg}")
                except Exception:
                    print(f"\n  [LOI] Khong the chuyen thanh text.")
                    print(f"  Recovered m (hex): {hex(m_recovered)}")
                pause()

            case "0":
                break
            case _:
                print("  [LOI] Lua chon khong hop le!")
                pause()


# ============================================================
#                   MENU: HASH FUNCTIONS
# ============================================================

def hash_menu():
    """Menu Hash Functions - ket hop TV4."""
    while True:
        clear_screen()
        print("\n╔══════════════════════════════════════╗")
        print("║        HASH FUNCTIONS MENU          ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. MD5 Hash                        ║")
        print("║  2. SHA-256 Hash                    ║")
        print("║  3. So sanh MD5 vs SHA-256          ║")
        print("║  0. Quay lai Main Menu              ║")
        print("╚══════════════════════════════════════╝")
        choice = input("Chon: ").strip()

        match choice:
            case "1":
                _md5_submenu()
            case "2":
                _sha256_submenu()
            case "3":
                text = input("  Nhap text de so sanh: ").strip()
                _compare_hashes(text)
                pause()
            case "0":
                break
            case _:
                print("  [LOI] Lua chon khong hop le!")
                pause()


def _md5_submenu():
    """Sub-menu MD5."""
    while True:
        clear_screen()
        print("\n╔══════════════════════════════╗")
        print("║        MD5 HASH MENU         ║")
        print("╠══════════════════════════════╣")
        print("║  1. Hash tu text            ║")
        print("║  2. Hash tu file           ║")
        print("║  0. Quay lai                ║")
        print("╚══════════════════════════════╝")
        choice = input("Chon: ").strip()

        match choice:
            case "1":
                text = input("  Nhap text can hash: ").strip()
                result = compute_md5(text)
                print(f"\n  Input  : {text}")
                print(f"  MD5    : {result}")
                print(f"  Length : 128 bits (32 hex chars)")
                pause()
            case "2":
                filepath = input("  Nhap duong dan file: ").strip()
                try:
                    result = compute_md5_file(filepath)
                    print(f"\n  File   : {filepath}")
                    print(f"  MD5    : {result}")
                    print(f"  Length : 128 bits (32 hex chars)")
                except FileNotFoundError as err:
                    print(f"\n  [LOI] Khong tim thay file: {err}")
                pause()
            case "0":
                break
            case _:
                print("  [LOI] Lua chon khong hop le!")
                pause()


def _sha256_submenu():
    """Sub-menu SHA-256."""
    while True:
        clear_screen()
        print("\n╔══════════════════════════════╗")
        print("║      SHA-256 HASH MENU      ║")
        print("╠══════════════════════════════╣")
        print("║  1. Hash tu text           ║")
        print("║  2. Hash tu file           ║")
        print("║  0. Quay lai                ║")
        print("╚══════════════════════════════╝")
        choice = input("Chon: ").strip()

        match choice:
            case "1":
                text = input("  Nhap text can hash: ").strip()
                result = compute_sha256(text)
                print(f"\n  Input   : {text}")
                print(f"  SHA-256 : {result}")
                print(f"  Length  : 256 bits (64 hex chars)")
                pause()
            case "2":
                filepath = input("  Nhap duong dan file: ").strip()
                try:
                    result = compute_sha256_file(filepath)
                    print(f"\n  File    : {filepath}")
                    print(f"  SHA-256 : {result}")
                    print(f"  Length  : 256 bits (64 hex chars)")
                except FileNotFoundError as err:
                    print(f"\n  [LOI] Khong tim thay file: {err}")
                pause()
            case "0":
                break
            case _:
                print("  [LOI] Lua chon khong hop le!")
                pause()


# ============================================================
#                   MENU: PKI DEMO
# ============================================================

def pki_demo_menu():
    """Menu PKI Demo - hien thi thong tin certificate."""
    while True:
        clear_screen()
        print("\n╔══════════════════════════════════════╗")
        print("║         PKI DEMO MENU               ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. PTIT Root CA (Task 1-2)         ║")
        print("║  2. Fake Hacker CA (Task 5)         ║")
        print("║  3. Compromised CA (Task 6)         ║")
        print("║  4. Huong dan su dung OpenSSL        ║")
        print("║  0. Quay lai Main Menu              ║")
        print("╚══════════════════════════════════════╝")
        choice = input("Chon: ").strip()

        match choice:
            case "1":
                _pki_show_task12()
            case "2":
                _pki_show_task5()
            case "3":
                _pki_show_task6()
            case "4":
                _pki_show_openssl_guide()
            case "0":
                break
            case _:
                print("  [LOI] Lua chon khong hop le!")
                pause()


def _pki_show_task12():
    clear_screen()
    print("\n  ===== TASK 1-2: ROOT CA & ptit.com CERTIFICATE =====")
    print("  " + "=" * 60)
    print("  PTIT Root CA:")
    print("    Issuer: C=VN, ST=Hanoi, L=Hanoi, O=PTIT, OU=ATTT,")
    print("            CN=PTIT Root CA, emailAddress=ptit@gmail.com")
    print("  Certificate cho ptit.com:")
    print("    Subject: C=VN, ST=Hanoi, L=Hanoi, O=PTIT, OU=ATTT,")
    print("             CN=ptit.com, emailAddress=ptit@gmail.com")
    print("    Issuer: PTIT Root CA (self-signed)")
    print("    Extensions: Basic Constraints CA:FALSE, Key Usage:")
    print("                Digital Signature, Key Encipherment")
    print("                Extended Key Usage: TLS Web Server Auth")
    print("                Subject Alternative Name: DNS:ptit.com")
    print("  " + "=" * 60)
    print("\n  Xem chi tiet: openssl x509 -in server.crt -text -noout")
    print("  Vi tri: N23DCCN071_hoanganh/PKI/task1_4_pki_lab/")
    pause()


def _pki_show_task5():
    clear_screen()
    print("\n  ===== TASK 5: FAKE CA MITM ATTACK =====")
    print("  " + "=" * 60)
    print("  Hacker Fake CA (khong duoc browser tin tuong):")
    print("    Issuer: C=VN, ST=Hanoi, O=Fake Hacker CA, OU=MITM Lab,")
    print("            CN=Fake Hacker Root CA, emailAddress=fakeca@gmail.com")
    print("  Fake certificate cho ptit.com:")
    print("    Subject: C=VN, ST=Hanoi, O=Hacker, OU=Fake Web,")
    print("             CN=ptit.com, emailAddress=hacker@gmail.com")
    print("    Issuer: Fake Hacker Root CA")
    print("    SubjectAltName: DNS:ptit.com")
    print("  " + "=" * 60)
    print("\n  ATTACK: Hacker tao certificate gia cho ptit.com")
    print("          duoi ten cua Fake Hacker CA.")
    print("  RESULT: Browser se CANH BAO vi Fake CA khong duoc tin tuong.")
    print("  Vi tri: N23DCCN071_hoanganh/PKI/task5_hacker_lab/")
    pause()


def _pki_show_task6():
    clear_screen()
    print("\n  ===== TASK 6: COMPROMISED CA ATTACK =====")
    print("  " + "=" * 60)
    print("  Compromised CA (Root CA bi mat):")
    print("    Original: PTIT Root CA (trusted by browsers)")
    print("  Hacker certificate cho hacker.com:")
    print("    Subject: C=VN, ST=Hanoi, O=Hacker, OU=Compromised CA Lab,")
    print("             CN=hacker.com, emailAddress=hacker6@gmail.com")
    print("    Issuer: PTIT Root CA (legit, trusted)")
    print("    Serial: ABCD")
    print("  " + "=" * 60)
    print("\n  ATTACK: Hacker lay duoc private key cua Root CA")
    print("          va tao certificate hop le cho hacker.com.")
    print("  RESULT: Browser KHONG canh bao vi certificate")
    print("          duoc ky boi CA that (trusted).")
    print("  Vi tri: N23DCCN071_hoanganh/PKI/task6_compromised_ca_lab/")
    pause()


def _pki_show_openssl_guide():
    clear_screen()
    print("\n  ===== OPENSSL GUIDE =====")
    print("  " + "=" * 60)
    print("  1. Xem certificate:")
    print("     openssl x509 -in cert.crt -text -noout")
    print()
    print("  2. Xem CSR:")
    print("     openssl req -in request.csr -text -noout")
    print()
    print("  3. Xac minh certificate:")
    print("     openssl verify -CAfile ca.crt server.crt")
    print()
    print("  4. Tao self-signed certificate:")
    print("     openssl req -x509 -newkey rsa:2048 \\")
    print("       -keyout cakey.pem -out cacert.pem -days 365")
    print()
    print("  5. Ky certificate bang CA:")
    print("     openssl ca -config openssl.cnf \\")
    print("       -in server.csr -out server.crt")
    print()
    print("  6. Kiem tra private key:")
    print("     openssl rsa -in server.key -check")
    print()
    print("  7. HTTPS server (OpenSSL):")
    print("     openssl s_server -cert server.crt \\")
    print("       -key server.key -www -port 4433")
    pause()


# ============================================================
#                   MAIN MENU
# ============================================================

def main_menu():
    print("\n╔══════════════════════════════════════════╗")
    print("║       CRYPTOGRAPHY TOOLKIT              ║")
    print("║       Lab 5 - Nhom 1                    ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Symmetric Encryption (AES / 3DES)  ║")
    print("║  2. Asymmetric Encryption (RSA)         ║")
    print("║  3. Hash Functions (MD5 / SHA-256)      ║")
    print("║  4. PKI Demo (Certificate Info)         ║")
    print("║  0. Thoat                              ║")
    print("╚══════════════════════════════════════════╝")


def main():
    """Entry point."""
    while True:
        clear_screen()
        main_menu()
        choice = input("Chon chuc nang: ").strip()

        match choice:
            case "1":
                symmetric_encrypt_menu()
            case "2":
                rsa_menu()
            case "3":
                hash_menu()
            case "4":
                pki_demo_menu()
            case "0":
                print("\n  Chuong trinh ket thuc. Tam biet!")
                break
            case _:
                print("  [LOI] Lua chon khong hop le!")
                pause()


if __name__ == "__main__":
    main()
