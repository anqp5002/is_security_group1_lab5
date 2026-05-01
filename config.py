"""
Cryptography Toolkit - Cấu hình chung
Lab 5 - Nhóm 1 - Bảo Mật Thông Tin - PTIT

Chứa các hằng số, key sizes, modes, và cấu hình cho tất cả modules.
"""

# ============================================================
#                   AES CONFIGURATION
# ============================================================

AES_KEY_SIZES = {
    "AES-128": 16,   # 128-bit (16 bytes)
    "AES-192": 24,   # 192-bit (24 bytes)
    "AES-256": 32,   # 256-bit (32 bytes)
}
AES_DEFAULT_KEY_SIZE = 16        # AES-128 by default
AES_IV_SIZE = 16                 # 16 bytes for AES CBC IV
AES_MODE = "CBC"                 # Block cipher mode

# ============================================================
#                   3DES CONFIGURATION
# ============================================================

TDES_KEY_SIZE = 24               # 168-bit key (24 bytes)
TDES_IV_SIZE = 8                 # 8 bytes for 3DES CBC IV
TDES_MODE = "CBC"                # Block cipher mode
TDES_BLOCK_SIZE = 8              # DES block size

# ============================================================
#                   RSA CONFIGURATION
# ============================================================

# Test values from a.txt (hex)
RSA_P_HEX = "F7E75FDC469067FFDC4E847C51F452DF"
RSA_Q_HEX = "E85CED54AF57E53E092113E62F436F4F"
RSA_E_HEX = "0D88C3"

RSA_P = int(RSA_P_HEX, 16)
RSA_Q = int(RSA_Q_HEX, 16)
RSA_E = int(RSA_E_HEX, 16)
RSA_N = RSA_P * RSA_Q
RSA_PHI = (RSA_P - 1) * (RSA_Q - 1)

# Calculate d = e^(-1) mod phi (will be computed at runtime)
RSA_PUBLIC_EXP = RSA_E
RSA_PUBLIC_MODULUS = RSA_N

# ============================================================
#                   HASH CONFIGURATION
# ============================================================

HASH_ALGORITHMS = {
    "MD5": {
        "output_bits": 128,
        "output_hex_chars": 32,
        "description": "128-bit hash (deprecated for security)",
    },
    "SHA-256": {
        "output_bits": 256,
        "output_hex_chars": 64,
        "description": "256-bit hash (recommended)",
    },
}

HASH_CHUNK_SIZE = 4096           # Bytes to read per chunk when hashing files

# ============================================================
#                   ENCODING CONFIGURATION
# ============================================================

DEFAULT_ENCODING = "utf-8"
TERMINAL_ENCODING = "utf-8"

# ============================================================
#                   MENU CONFIGURATION
# ============================================================

import platform as _platform


def _get_platform() -> str:
    return _platform.system()


def get_clear_screen_cmd() -> str:
    return "cls" if _get_platform() == "Windows" else "clear"


MENU_CLEAR_CMD = get_clear_screen_cmd()
