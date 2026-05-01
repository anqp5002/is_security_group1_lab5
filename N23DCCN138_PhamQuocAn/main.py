"""
Cryptography Toolkit - Main Menu
Lab 5 - Bảo Mật Thông Tin - Nhóm 1

Main entry point cho ứng dụng Cryptography Toolkit.
Hỗ trợ: Symmetric Encryption, Asymmetric Encryption, Hash Functions.
"""
import os
import sys
import platform

# Fix encoding cho Windows terminal
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")


def main_menu():
    print("\n╔══════════════════════════════════════════╗")
    print("║       CRYPTOGRAPHY TOOLKIT               ║")
    print("║       Lab 5 - Nhóm 1                     ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Symmetric Encryption (DES/3DES/AES)  ║")
    print("║  2. Asymmetric Encryption (RSA)           ║")
    print("║  3. Hash Functions (MD5/SHA-256)           ║")
    print("║  0. Thoát                                ║")
    print("╚══════════════════════════════════════════╝")


def main():
    while True:
        clear_screen()
        main_menu()
        choice = input("Chọn chức năng: ").strip()

        match choice:
            case "1":
                # TODO: Symmetric Encryption - TV1 (DES) + TV2 (3DES, AES)
                print("\n  [THÔNG BÁO] Module Symmetric Encryption chưa được implement.")
                print("  Đang chờ TV1 (DES) và TV2 (3DES, AES) hoàn thành.")
                input("\nNhấn Enter để tiếp tục...")

            case "2":
                # TODO: Asymmetric Encryption - TV3 (RSA)
                print("\n  [THÔNG BÁO] Module Asymmetric Encryption chưa được implement.")
                print("  Đang chờ TV3 (RSA) hoàn thành.")
                print("  Tạm thời có thể chạy: python RSA.py")
                input("\nNhấn Enter để tiếp tục...")

            case "3":
                # Hash Functions - TV4
                from hashing import hash_menu
                hash_menu()

            case "0":
                print("\n  Chương trình đã kết thúc. Tạm biệt!")
                break

            case _:
                print("  [LỖI] Lựa chọn không hợp lệ! Vui lòng chọn lại.")
                input("\nNhấn Enter để tiếp tục...")


if __name__ == "__main__":
    main()
