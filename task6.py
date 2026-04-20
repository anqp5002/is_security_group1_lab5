import hashlib
import os
import RSA
from dotenv import load_dotenv

# ====== Load .env ======
load_dotenv()

signature_hex = os.getenv("SIGNATURE")
n_hex = os.getenv("MODULUS")
e = int(os.getenv("EXPONENT"))
body_file = os.getenv("BODY_FILE")

# ====== STEP 1: Hash BODY ======
with open(body_file, "rb") as f:
    body = f.read()

hash1 = hashlib.sha256(body).hexdigest()
print("Hash từ body:", hash1)


# ====== STEP 2: RSA verify ======
S = int(signature_hex, 16)
n = int(n_hex, 16)

M = RSA.verify(S,e,n)

M_hex = hex(M)[2:]
if len(M_hex) % 2 != 0:
    M_hex = "0" + M_hex

print("Giải mã signature (M):", M_hex)


# ====== STEP 3: lấy hash từ M ======
hash2 = M_hex[-64:]
print("Hash từ signature:", hash2)


# ====== STEP 4: So sánh ======
if hash1.lower() == hash2.lower():
    print("VERIFY THÀNH CÔNG: Signature hợp lệ")
else:
    print("VERIFY THẤT BẠI: Signature không hợp lệ")