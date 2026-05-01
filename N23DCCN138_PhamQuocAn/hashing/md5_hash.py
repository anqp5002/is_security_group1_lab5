"""
MD5 Hash Module
Thanh vien 4 - Cryptography Toolkit Lab 5
"""
import hashlib
import os
import sys

# Fix encoding cho Windows terminal
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def compute_md5(text: str) -> str:
    """Tính MD5 digest từ chuỗi text."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def compute_md5_file(filepath: str) -> str:
    """Tính MD5 digest từ file (đọc theo chunk để xử lý file lớn)."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Không tìm thấy file: {filepath}")
    h = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()


def md5_menu():
    """Sub-menu cho MD5 Hash."""
    while True:
        print("\n╔══════════════════════════════╗")
        print("║        MD5 HASH MENU         ║")
        print("╠══════════════════════════════╣")
        print("║  1. Hash từ text             ║")
        print("║  2. Hash từ file             ║")
        print("║  0. Quay lại                 ║")
        print("╚══════════════════════════════╝")
        choice = input("Chọn: ").strip()

        match choice:
            case "1":
                text = input("Nhập text cần hash: ")
                result = compute_md5(text)
                print(f"\n  Input  : {text}")
                print(f"  MD5    : {result}")
                print(f"  Length : 128 bits (32 hex chars)")
                input("\nNhấn Enter để tiếp tục...")

            case "2":
                filepath = input("Nhập đường dẫn file: ").strip()
                try:
                    result = compute_md5_file(filepath)
                    print(f"\n  File   : {filepath}")
                    print(f"  MD5    : {result}")
                    print(f"  Length : 128 bits (32 hex chars)")
                except FileNotFoundError as e:
                    print(f"\n  [LỖI] {e}")
                input("\nNhấn Enter để tiếp tục...")

            case "0":
                break

            case _:
                print("  [LỖI] Lựa chọn không hợp lệ!")
