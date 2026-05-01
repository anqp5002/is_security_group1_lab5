"""
Auto Test - Kiem tra tat ca chuc nang Hash Module
Nhom 1 - Cryptography Toolkit Lab 5
"""
import sys
import os

# Fix encoding
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from hashing.md5_hash import compute_md5, compute_md5_file
from hashing.sha256_hash import compute_sha256, compute_sha256_file
from hashing import compare_hashes

passed = 0
failed = 0

def test(name, condition):
    global passed, failed
    if condition:
        print(f"  [PASS] {name}")
        passed += 1
    else:
        print(f"  [FAIL] {name}")
        failed += 1

print("=" * 65)
print("  AUTO TEST - Hash Module (TV4) - Nhom 1")
print("=" * 65)

# ===== TEST GROUP 1: MD5 Hash =====
print("\n--- MD5 Hash Tests ---")

r = compute_md5("hello")
test("MD5('hello')", r == "5d41402abc4b2a76b9719d911017c592")

r = compute_md5("")
test("MD5('') empty string", r == "d41d8cd98f00b204e9800998ecf8427e")

r = compute_md5("abc")
test("MD5('abc')", r == "900150983cd24fb0d6963f7d28e17f72")

r = compute_md5("abc123!@#")
test("MD5 special chars", len(r) == 32)

r = compute_md5("A" * 10000)
test("MD5 long string (10000 chars)", len(r) == 32)

r = compute_md5("Xin chào Việt Nam")
test("MD5 Vietnamese text", len(r) == 32)

# ===== TEST GROUP 2: SHA-256 Hash =====
print("\n--- SHA-256 Hash Tests ---")

r = compute_sha256("hello")
test("SHA256('hello')", r == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824")

r = compute_sha256("")
test("SHA256('') empty string", r == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")

r = compute_sha256("abc")
test("SHA256('abc')", r == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

r = compute_sha256("abc123!@#")
test("SHA256 special chars", len(r) == 64)

r = compute_sha256("A" * 10000)
test("SHA256 long string (10000 chars)", len(r) == 64)

# ===== TEST GROUP 3: File Hash =====
print("\n--- File Hash Tests ---")

r1 = compute_md5_file("README.md")
test("MD5 file README.md", len(r1) == 32)

r2 = compute_sha256_file("README.md")
test("SHA256 file README.md", len(r2) == 64)

r3 = compute_md5_file("RSA.py")
test("MD5 file RSA.py", len(r3) == 32)

# ===== TEST GROUP 4: Error Handling =====
print("\n--- Error Handling Tests ---")

try:
    compute_md5_file("khong_ton_tai_abc.txt")
    test("MD5 file not found raises error", False)
except FileNotFoundError:
    test("MD5 file not found raises error", True)

try:
    compute_sha256_file("khong_ton_tai_abc.txt")
    test("SHA256 file not found raises error", False)
except FileNotFoundError:
    test("SHA256 file not found raises error", True)

# ===== TEST GROUP 5: Consistency =====
print("\n--- Consistency Tests ---")

# Same input = same output
r1 = compute_md5("test")
r2 = compute_md5("test")
test("MD5 same input = same output", r1 == r2)

r1 = compute_sha256("test")
r2 = compute_sha256("test")
test("SHA256 same input = same output", r1 == r2)

# Different input = different output
r1 = compute_md5("hello")
r2 = compute_md5("hello!")
test("MD5 different input = different output", r1 != r2)

r1 = compute_sha256("hello")
r2 = compute_sha256("hello!")
test("SHA256 different input = different output", r1 != r2)

# MD5 != SHA256 for same input
r1 = compute_md5("test")
r2 = compute_sha256("test")
test("MD5 != SHA256 for same input", r1 != r2)

# MD5 = 32 chars, SHA256 = 64 chars
test("MD5 output length = 32", len(compute_md5("x")) == 32)
test("SHA256 output length = 64", len(compute_sha256("x")) == 64)

# ===== TEST GROUP 6: Import Tests =====
print("\n--- Import & Module Tests ---")

try:
    from hashing import hash_menu
    test("Import hash_menu from hashing", True)
except ImportError:
    test("Import hash_menu from hashing", False)

try:
    from hashing import compare_hashes
    test("Import compare_hashes from hashing", True)
except ImportError:
    test("Import compare_hashes from hashing", False)

try:
    import utils
    test("Import utils module", True)
except ImportError:
    test("Import utils module", False)

# ===== TEST GROUP 7: Utils Functions =====
print("\n--- Utils Tests ---")

from utils import hex_to_bytes, bytes_to_hex, text_to_hex, hex_to_text
from utils import is_valid_hex, validate_input_not_empty, format_hex_block

test("hex_to_bytes('48656c6c6f')", hex_to_bytes("48656c6c6f") == b'Hello')
test("bytes_to_hex(b'Hello')", bytes_to_hex(b'Hello') == "48656c6c6f")
test("text_to_hex('Hello')", text_to_hex("Hello") == "48656c6c6f")
test("hex_to_text('48656c6c6f')", hex_to_text("48656c6c6f") == "Hello")
test("is_valid_hex('abcd')", is_valid_hex("abcd") == True)
test("is_valid_hex('xyz')", is_valid_hex("xyz") == False)
test("format_hex_block", "5d41402a" in format_hex_block("5d41402abc4b2a76"))

try:
    validate_input_not_empty("  ", "test")
    test("validate_input_not_empty rejects blank", False)
except ValueError:
    test("validate_input_not_empty rejects blank", True)

test("validate_input_not_empty accepts text", validate_input_not_empty(" hello ", "test") == "hello")

# ===== SUMMARY =====
print("\n" + "=" * 65)
total = passed + failed
print(f"  RESULTS: {passed}/{total} PASSED, {failed}/{total} FAILED")
if failed == 0:
    print("  >>> ALL TESTS PASSED! <<<")
else:
    print(f"  >>> {failed} TEST(S) FAILED! <<<")
print("=" * 65)
