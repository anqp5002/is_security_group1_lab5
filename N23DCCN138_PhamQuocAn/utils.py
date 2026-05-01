"""
Utility Functions
Thành viên 4 - Cryptography Toolkit Lab 5

Các hàm tiện ích dùng chung cho toàn bộ project.
"""
import os
import platform


# ============================================================
#                   CONVERSION FUNCTIONS
# ============================================================

def hex_to_bytes(hex_string: str) -> bytes:
    """
    Convert hex string → bytes.
    Ví dụ: "48656c6c6f" → b'Hello'
    """
    try:
        return bytes.fromhex(hex_string)
    except ValueError:
        raise ValueError(f"Chuỗi hex không hợp lệ: {hex_string}")


def bytes_to_hex(data: bytes) -> str:
    """
    Convert bytes → hex string.
    Ví dụ: b'Hello' → "48656c6c6f"
    """
    return data.hex()


def text_to_hex(text: str) -> str:
    """
    Convert text → hex representation (UTF-8).
    Ví dụ: "Hello" → "48656c6c6f"
    """
    return text.encode('utf-8').hex()


def hex_to_text(hex_string: str) -> str:
    """
    Convert hex → readable text (UTF-8).
    Ví dụ: "48656c6c6f" → "Hello"
    """
    try:
        return bytes.fromhex(hex_string).decode('utf-8')
    except (ValueError, UnicodeDecodeError) as e:
        raise ValueError(f"Không thể convert hex → text: {e}")


# ============================================================
#                   FORMAT / DISPLAY FUNCTIONS
# ============================================================

def format_hash_output(algorithm: str, input_data: str, hash_value: str):
    """In kết quả hash với format đẹp."""
    bit_length = len(hash_value) * 4
    print("\n  ╔═══════════════════════════════════════════════════════════════════╗")
    print(f"  ║  Algorithm : {algorithm}")
    print(f"  ║  Input     : {input_data}")
    print(f"  ║  Hash      : {hash_value}")
    print(f"  ║  Length    : {len(hash_value)} hex chars = {bit_length} bits")
    print("  ╚═══════════════════════════════════════════════════════════════════╝")


def format_hex_block(hex_string: str, block_size: int = 8) -> str:
    """
    Format hex string thành dạng block cho dễ đọc.
    Ví dụ: "5d41402abc4b2a76" → "5d41402a bc4b2a76"
    """
    return ' '.join(
        hex_string[i:i + block_size]
        for i in range(0, len(hex_string), block_size)
    )


# ============================================================
#                   FILE FUNCTIONS
# ============================================================

def read_file_bytes(filepath: str) -> bytes:
    """Đọc toàn bộ file dưới dạng binary."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Không tìm thấy file: {filepath}")
    with open(filepath, 'rb') as f:
        return f.read()


def read_file_text(filepath: str, encoding: str = 'utf-8') -> str:
    """Đọc toàn bộ file dưới dạng text."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Không tìm thấy file: {filepath}")
    with open(filepath, 'r', encoding=encoding) as f:
        return f.read()


# ============================================================
#                   TERMINAL FUNCTIONS
# ============================================================

def clear_screen():
    """Xóa màn hình terminal."""
    os.system("cls" if platform.system() == "Windows" else "clear")


def pause(message: str = "Nhấn Enter để tiếp tục..."):
    """Tạm dừng và chờ user nhấn Enter."""
    input(f"\n{message}")


# ============================================================
#                   VALIDATION FUNCTIONS
# ============================================================

def is_valid_hex(hex_string: str) -> bool:
    """Kiểm tra xem chuỗi có phải hex hợp lệ không."""
    try:
        bytes.fromhex(hex_string)
        return True
    except ValueError:
        return False


def validate_input_not_empty(text: str, field_name: str = "Input") -> str:
    """Kiểm tra input không rỗng, trả về text đã strip."""
    text = text.strip()
    if not text:
        raise ValueError(f"{field_name} không được để trống!")
    return text
