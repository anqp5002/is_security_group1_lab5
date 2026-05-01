"""
SHA-256 Hash Module
Thành viên 4 - Cryptography Toolkit Lab 5
"""
import hashlib
import os


def compute_sha256(text: str) -> str:
    """Tính SHA-256 digest từ chuỗi text."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def compute_sha256_file(filepath: str) -> str:
    """Tính SHA-256 digest từ file (đọc theo chunk để xử lý file lớn)."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Không tìm thấy file: {filepath}")
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_menu():
    """Sub-menu cho SHA-256 Hash."""
    while True:
        print("\n╔══════════════════════════════╗")
        print("║      SHA-256 HASH MENU       ║")
        print("╠══════════════════════════════╣")
        print("║  1. Hash từ text             ║")
        print("║  2. Hash từ file             ║")
        print("║  0. Quay lại                 ║")
        print("╚══════════════════════════════╝")
        choice = input("Chọn: ").strip()

        match choice:
            case "1":
                text = input("Nhập text cần hash: ")
                result = compute_sha256(text)
                print(f"\n  Input   : {text}")
                print(f"  SHA-256 : {result}")
                print(f"  Length  : 256 bits (64 hex chars)")
                input("\nNhấn Enter để tiếp tục...")

            case "2":
                filepath = input("Nhập đường dẫn file: ").strip()
                try:
                    result = compute_sha256_file(filepath)
                    print(f"\n  File    : {filepath}")
                    print(f"  SHA-256 : {result}")
                    print(f"  Length  : 256 bits (64 hex chars)")
                except FileNotFoundError as e:
                    print(f"\n  [LỖI] {e}")
                input("\nNhấn Enter để tiếp tục...")

            case "0":
                break

            case _:
                print("  [LỖI] Lựa chọn không hợp lệ!")
