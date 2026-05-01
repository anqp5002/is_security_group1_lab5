from Crypto.Cipher import DES3, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


def b64_encode(data: bytes) -> str:
    return base64.b64encode(data).decode("utf-8")


def b64_decode(data: str) -> bytes:
    return base64.b64decode(data, validate=True)


def generate_3des_key() -> str:
    """
    3DES dùng key 24 bytes.
    DES3 yêu cầu key không bị suy biến thành single DES.
    """
    while True:
        try:
            key = DES3.adjust_key_parity(get_random_bytes(24))
            DES3.new(key, DES3.MODE_CBC, iv=get_random_bytes(8))
            return b64_encode(key)
        except ValueError:
            continue


def generate_aes_key() -> str:
    """
    AES-128 dùng key 16 bytes.
    """
    key = get_random_bytes(16)
    return b64_encode(key)


def generate_key(algorithm: str) -> str:
    if algorithm == "3DES":
        return generate_3des_key()
    elif algorithm == "AES":
        return generate_aes_key()
    else:
        raise ValueError("Thuật toán không hợp lệ.")


def encrypt_data(algorithm: str, plaintext: str, key_base64: str) -> str:
    try:
        key = b64_decode(key_base64)

        if algorithm == "3DES":
            if len(key) != 24:
                raise ValueError("Key 3DES phải đúng 24 bytes.")
            key = DES3.adjust_key_parity(key)
            iv = get_random_bytes(8)
            cipher = DES3.new(key, DES3.MODE_CBC, iv)
            ciphertext = cipher.encrypt(pad(plaintext.encode("utf-8"), 8))

        elif algorithm == "AES":
            if len(key) not in [16, 24, 32]:
                raise ValueError("Key AES phải là 16, 24 hoặc 32 bytes.")
            iv = get_random_bytes(16)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            ciphertext = cipher.encrypt(pad(plaintext.encode("utf-8"), 16))

        else:
            raise ValueError("Thuật toán không hỗ trợ.")

        return b64_encode(iv + ciphertext)

    except Exception as e:
        return f"Lỗi mã hóa: {e}"


def decrypt_data(algorithm: str, ciphertext_base64: str, key_base64: str) -> str:
    try:
        key = b64_decode(key_base64)
        raw_data = b64_decode(ciphertext_base64)

        if algorithm == "3DES":
            if len(key) != 24:
                raise ValueError("Key 3DES phải đúng 24 bytes.")
            key = DES3.adjust_key_parity(key)

            iv = raw_data[:8]
            ciphertext = raw_data[8:]

            cipher = DES3.new(key, DES3.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), 8)

        elif algorithm == "AES":
            if len(key) not in [16, 24, 32]:
                raise ValueError("Key AES phải là 16, 24 hoặc 32 bytes.")

            iv = raw_data[:16]
            ciphertext = raw_data[16:]

            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), 16)

        else:
            raise ValueError("Thuật toán không hỗ trợ.")

        return plaintext.decode("utf-8")

    except Exception as e:
        return f"Lỗi giải mã: {e}"

