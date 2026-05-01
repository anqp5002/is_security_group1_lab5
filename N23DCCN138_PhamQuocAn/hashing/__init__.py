"""
Hash Functions Sub-Menu
Thành viên 4 - Cryptography Toolkit Lab 5

Module này cung cấp giao diện CLI để sử dụng MD5 và SHA-256 hash.
"""
import os
import platform
from .md5_hash import compute_md5, compute_md5_file, md5_menu
from .sha256_hash import compute_sha256, compute_sha256_file, sha256_menu


def compare_hashes(text: str):
    """So sánh kết quả MD5 và SHA-256 cho cùng một input."""
    md5_result = compute_md5(text)
    sha256_result = compute_sha256(text)

    print("\n  ┌─────────────────────────────────────────────────────────────────────┐")
    print(f"  │  Input   : {text}")
    print(f"  ├─────────────────────────────────────────────────────────────────────┤")
    print(f"  │  MD5     : {md5_result}")
    print(f"  │  Length  : 128 bits (32 hex chars)")
    print(f"  ├─────────────────────────────────────────────────────────────────────┤")
    print(f"  │  SHA-256 : {sha256_result}")
    print(f"  │  Length  : 256 bits (64 hex chars)")
    print(f"  └─────────────────────────────────────────────────────────────────────┘")
    print("\n  ⚠ Lưu ý: MD5 không còn an toàn, SHA-256 được khuyến nghị sử dụng.")


def hash_menu():
    """Menu chính cho Hash Functions - được gọi từ main menu."""
    while True:
        os.system("cls" if platform.system() == "Windows" else "clear")
        print("\n╔══════════════════════════════════════╗")
        print("║        HASH FUNCTIONS MENU           ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. MD5 Hash                         ║")
        print("║  2. SHA-256 Hash                     ║")
        print("║  3. So sánh MD5 vs SHA-256            ║")
        print("║  0. Quay lại Main Menu               ║")
        print("╚══════════════════════════════════════╝")
        choice = input("Chọn: ").strip()

        match choice:
            case "1":
                md5_menu()

            case "2":
                sha256_menu()

            case "3":
                text = input("Nhập text để so sánh: ")
                compare_hashes(text)
                input("\nNhấn Enter để tiếp tục...")

            case "0":
                break

            case _:
                print("  [LỖI] Lựa chọn không hợp lệ!")
                input("\nNhấn Enter để tiếp tục...")
