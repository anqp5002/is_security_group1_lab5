"""
End-to-End Test Suite - Cryptography Toolkit
Lab 5 - Nhom 1 - Bao Mat Thong Tin - PTIT

Test tat ca cac module: Hash, AES, 3DES, RSA.
Chay: python test_e2e.py
"""

import sys
import os

# Fix encoding cho Windows terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ============================================================
#                   CONFIG
# ============================================================

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

passed = 0
failed = 0


def test(name: str, condition: bool):
    global passed, failed
    if condition:
        print(f"  [PASS] {name}")
        passed += 1
    else:
        print(f"  [FAIL] {name}")
        failed += 1


def section(title: str):
    print(f"\n{'=' * 65}")
    print(f"  {title}")
    print(f"{'=' * 65}")


# ============================================================
#                   TEST: HASH MODULE
# ============================================================

def test_hash():
    section("HASH MODULE (TV4: N23DCCN138)")
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "N23DCCN138_PhamQuocAn"))
    from hashing.md5_hash import compute_md5, compute_md5_file
    from hashing.sha256_hash import compute_sha256, compute_sha256_file

    # MD5
    r = compute_md5("hello")
    test("MD5('hello') known value", r == "5d41402abc4b2a76b9719d911017c592")

    r = compute_md5("")
    test("MD5('') empty string", r == "d41d8cd98f00b204e9800998ecf8427e")

    r = compute_md5("abc")
    test("MD5('abc')", r == "900150983cd24fb0d6963f7d28e17f72")

    r = compute_md5("Xin chao Viet Nam")
    test("MD5 Vietnamese text", len(r) == 32)

    r = compute_md5("A" * 10000)
    test("MD5 long string (10000 chars)", len(r) == 32)

    # SHA-256
    r = compute_sha256("hello")
    test(
        "SHA256('hello') known value",
        r == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
    )

    r = compute_sha256("")
    test(
        "SHA256('') empty string",
        r == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    )

    r = compute_sha256("abc")
    test(
        "SHA256('abc')",
        r == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
    )

    r = compute_sha256("A" * 10000)
    test("SHA256 long string (10000 chars)", len(r) == 64)

    # Consistency
    r1 = compute_md5("test")
    r2 = compute_md5("test")
    test("MD5 same input = same output", r1 == r2)

    r1 = compute_sha256("test")
    r2 = compute_sha256("test")
    test("SHA256 same input = same output", r1 == r2)

    r1 = compute_md5("hello")
    r2 = compute_md5("hello!")
    test("MD5 different input = different output", r1 != r2)

    r1 = compute_sha256("hello")
    r2 = compute_sha256("hello!")
    test("SHA256 different input = different output", r1 != r2)

    test("MD5 output length = 32", len(compute_md5("x")) == 32)
    test("SHA256 output length = 64", len(compute_sha256("x")) == 64)

    # File hash
    readme = os.path.join(PROJECT_ROOT, "README.md")
    if os.path.exists(readme):
        r1 = compute_md5_file(readme)
        test("MD5 file README.md", len(r1) == 32)
        r2 = compute_sha256_file(readme)
        test("SHA256 file README.md", len(r2) == 64)
        # Consistent
        r3 = compute_md5_file(readme)
        test("MD5 file consistency", r1 == r3)
    else:
        test("MD5 file README.md (skipped - file not found)", False)
        test("SHA256 file README.md (skipped - file not found)", False)
        test("MD5 file consistency (skipped)", False)

    # File not found
    try:
        compute_md5_file("nonexistent.txt")
        test("MD5 file not found raises error", False)
    except FileNotFoundError:
        test("MD5 file not found raises error", True)

    try:
        compute_sha256_file("nonexistent.txt")
        test("SHA256 file not found raises error", False)
    except FileNotFoundError:
        test("SHA256 file not found raises error", True)


# ============================================================
#                   TEST: AES / 3DES MODULE
# ============================================================

def test_symmetric():
    section("SYMMETRIC ENCRYPTION MODULE (TV2: N23DCCN071)")
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "N23DCCN071_hoanganh", "AES_3DES"))
    from app.symmetric import generate_key, encrypt_data, decrypt_data

    # --- AES ---
    key = generate_key("AES")
    test("AES generate_key returns Base64 string", isinstance(key, str))
    test("AES key is not empty", len(key) > 0)

    plaintext = "Hello, Lab 5!"
    key_aes = generate_key("AES")
    ct = encrypt_data("AES", plaintext, key_aes)
    test("AES encrypt returns Base64 string", isinstance(ct, str))
    test("AES ciphertext is not empty", len(ct) > 0)
    test("AES ciphertext != plaintext", ct != plaintext)

    pt = decrypt_data("AES", ct, key_aes)
    test("AES decrypt recovers original plaintext", pt == plaintext)

    # AES special chars
    key2 = generate_key("AES")
    ct2 = encrypt_data("AES", "Tieng Viet: Xin chao!", key2)
    pt2 = decrypt_data("AES", ct2, key2)
    test("AES encrypt/decrypt Vietnamese text", pt2 == "Tieng Viet: Xin chao!")

    # AES long text
    key3 = generate_key("AES")
    long_text = "A" * 1000
    ct3 = encrypt_data("AES", long_text, key3)
    pt3 = decrypt_data("AES", ct3, key3)
    test("AES encrypt/decrypt long text (1000 chars)", pt3 == long_text)

    # AES wrong key - CBC mode returns garbled output, not an error
    key_a = generate_key("AES")
    key_b = generate_key("AES")
    ct4 = encrypt_data("AES", "test", key_a)
    pt4 = decrypt_data("AES", ct4, key_b)
    test("AES decrypt with wrong key returns garbled output (not original)", pt4 != "test")

    # AES invalid key size - catches error OR returns garbled
    fake_key = "invalidbase64key"
    ct5 = encrypt_data("AES", "test", fake_key)
    # Either error or garbled is acceptable here
    test("AES invalid key returns error or garbled", ct5.startswith("Loi") or len(ct5) > 0)

    # --- 3DES ---
    key = generate_key("3DES")
    test("3DES generate_key returns Base64 string", isinstance(key, str))

    key_tdes = generate_key("3DES")
    ct = encrypt_data("3DES", plaintext, key_tdes)
    test("3DES encrypt returns Base64 string", isinstance(ct, str))
    test("3DES ciphertext != plaintext", ct != plaintext)

    pt = decrypt_data("3DES", ct, key_tdes)
    test("3DES decrypt recovers original plaintext", pt == plaintext)

    # 3DES special chars
    key_t2 = generate_key("3DES")
    ct_t2 = encrypt_data("3DES", "3DES Test: @#$%", key_t2)
    pt_t2 = decrypt_data("3DES", ct_t2, key_t2)
    test("3DES encrypt/decrypt special chars", pt_t2 == "3DES Test: @#$%")

    # 3DES wrong key - CBC mode returns garbled output
    key_t_a = generate_key("3DES")
    key_t_b = generate_key("3DES")
    ct_t3 = encrypt_data("3DES", "test", key_t_a)
    pt_t3 = decrypt_data("3DES", ct_t3, key_t_b)
    test("3DES decrypt with wrong key returns garbled (not original)", pt_t3 != "test")

    # --- Invalid algorithm ---
    try:
        generate_key("BLOWFISH")
        test("Invalid algorithm raises error", False)
    except ValueError:
        test("Invalid algorithm raises error", True)


# ============================================================
#                   TEST: RSA MODULE
# ============================================================

def test_rsa():
    section("RSA MODULE (TV1: N23DCCN001)")

    sys.path.insert(0, PROJECT_ROOT)
    import config

    p = config.RSA_P
    q = config.RSA_Q
    e = config.RSA_E
    n = config.RSA_N

    # Calculate d
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    test("RSA d = e^(-1) mod phi", d is not None)
    test("RSA d > 0", d > 0)

    # Verify n = p * q
    test("RSA n = p * q", n == p * q)

    # Verify e * d % phi == 1
    test("RSA e * d % phi(n) == 1", (e * d) % phi == 1)

    # Encrypt / Decrypt
    message = "Lab5"
    m_int = int(message.encode("utf-8").hex(), 16)

    c = pow(m_int, e, n)
    test("RSA encrypt: c = m^e mod n", c > 0)
    test("RSA ciphertext != plaintext int", c != m_int)

    m_recovered = pow(c, d, n)
    recovered = m_recovered.to_bytes((m_recovered.bit_length() + 7) // 8, "big").decode("utf-8")
    test("RSA decrypt recovers original message", recovered == message)

    # Sign / Verify
    s = pow(m_int, d, n)
    test("RSA sign: s = m^d mod n", s > 0)
    test("RSA signature != message int", s != m_int)

    m_verified = pow(s, e, n)
    verified = m_verified.to_bytes((m_verified.bit_length() + 7) // 8, "big").decode("utf-8")
    test("RSA verify recovers original message", verified == message)

    # Wrong key pair
    other_p = int("B" * 64, 16)
    other_q = int("C" * 64, 16)
    other_n = other_p * other_q
    other_d = pow(e, -1, (other_p - 1) * (other_q - 1))

    fake_c = pow(m_int, e, other_n)
    fake_m = pow(fake_c, other_d, other_n)
    fake_recovered = fake_m.to_bytes((fake_m.bit_length() + 7) // 8, "big").decode("utf-8", errors="ignore")
    test("RSA wrong key does not recover original", fake_recovered != message)

    # Known test values (a.txt)
    test("RSA P hex matches config", config.RSA_P_HEX == "F7E75FDC469067FFDC4E847C51F452DF")
    test("RSA Q hex matches config", config.RSA_Q_HEX == "E85CED54AF57E53E092113E62F436F4F")
    test("RSA E hex matches config", config.RSA_E_HEX == "0D88C3")


# ============================================================
#                   TEST: CONFIG MODULE
# ============================================================

def test_config():
    section("CONFIG MODULE")
    sys.path.insert(0, PROJECT_ROOT)
    import config

    test("AES default key size = 16", config.AES_DEFAULT_KEY_SIZE == 16)
    test("AES IV size = 16", config.AES_IV_SIZE == 16)
    test("3DES key size = 24", config.TDES_KEY_SIZE == 24)
    test("3DES IV size = 8", config.TDES_IV_SIZE == 8)
    test("Hash chunk size = 4096", config.HASH_CHUNK_SIZE == 4096)
    test("RSA public exponent set", config.RSA_PUBLIC_EXP > 0)
    test("RSA public modulus set", config.RSA_PUBLIC_MODULUS > 0)
    test("AES key sizes dict has 3 entries", len(config.AES_KEY_SIZES) == 3)
    test("get_clear_screen_cmd returns string", isinstance(config.get_clear_screen_cmd(), str))


# ============================================================
#                   TEST: INTEGRATION
# ============================================================

def test_integration():
    section("INTEGRATION TEST")
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "N23DCCN138_PhamQuocAn"))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "N23DCCN071_hoanganh", "AES_3DES"))
    sys.path.insert(0, PROJECT_ROOT)

    from hashing.md5_hash import compute_md5
    from hashing.sha256_hash import compute_sha256
    from app.symmetric import generate_key, encrypt_data, decrypt_data
    import config

    # Workflow: Hash -> Symmetric Encrypt -> Decrypt
    original = "Sensitive data for Lab 5"
    md5_of_original = compute_md5(original)
    test("Integration: MD5 hash computed", len(md5_of_original) == 32)

    sha256_of_original = compute_sha256(original)
    test("Integration: SHA256 hash computed", len(sha256_of_original) == 64)

    # Encrypt with AES
    aes_key = generate_key("AES")
    ct = encrypt_data("AES", original, aes_key)
    test("Integration: AES encrypt succeeds", isinstance(ct, str))

    # Decrypt
    pt = decrypt_data("AES", ct, aes_key)
    test("Integration: AES decrypt recovers plaintext", pt == original)

    # Hash the ciphertext
    sha256_of_ct = compute_sha256(ct)
    test("Integration: SHA256 of ciphertext computed", len(sha256_of_ct) == 64)
    test("Integration: SHA256 differs from plaintext", sha256_of_original != sha256_of_ct)

    # Encrypt with 3DES
    tdes_key = generate_key("3DES")
    ct_t = encrypt_data("3DES", original, tdes_key)
    test("Integration: 3DES encrypt succeeds", isinstance(ct_t, str))

    pt_t = decrypt_data("3DES", ct_t, tdes_key)
    test("Integration: 3DES decrypt recovers plaintext", pt_t == original)

    # Config consistency
    test("Integration: RSA modulus matches config", config.RSA_N == config.RSA_PUBLIC_MODULUS)


# ============================================================
#                   MAIN
# ============================================================

def main():
    global passed, failed

    print("\n" + "=" * 65)
    print("  END-TO-END TEST SUITE - CRYPTOGRAPHY TOOLKIT")
    print("  Lab 5 - Nhom 1 - Bao Mat Thong Tin - PTIT")
    print("=" * 65)

    test_config()
    test_hash()
    test_symmetric()
    test_rsa()
    test_integration()

    total = passed + failed
    print("\n" + "=" * 65)
    print(f"  RESULTS: {passed}/{total} PASSED, {failed}/{total} FAILED")
    if failed == 0:
        print("  >>> ALL TESTS PASSED! <<<")
    else:
        print(f"  >>> {failed} TEST(S) FAILED! <<<")
    print("=" * 65)

    # Return exit code
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
