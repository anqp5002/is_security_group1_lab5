# Cryptography Toolkit - Lab 5 Bảo Mật Thông Tin

Nhóm 1 - Bảo Mật Thông Tin - PTIT

---

## 1. Giới thiệu Project

Project này thực hiện **4 SEED Labs** trong chương trình Bảo Mật Thông Tin:

| Lab | Tên | Trạng thái |
|-----|------|-------------|
| **Lab 1** | Cryptography Toolkit | Hoàn thành |
| **Lab 2** | MD5 Collision Attack | Tài liệu (yêu cầu môi trường Linux) |
| **Lab 3** | RSA Public-Key Encryption | Hoàn thành |
| **Lab 4** | PKI (Public Key Infrastructure) | Hoàn thành |

---

## 2. Cấu trúc nhóm

| Thành viên | Mã SV | Phần phụ trách |
|---|---|---|
| Đặng Kim An | N23DCCN001 | Lab 3 - RSA (C + Python), Task 6 X.509 Certificate Verification |
| Hồ Ngọc Hoàng Anh | N23DCCN071 | Lab 1 (AES/3DES), Lab 4 - PKI Tasks 1-6 |
| Phạm Quốc An | N23DCCN138 | Lab 1 - Hash Functions (MD5, SHA-256) |

---

## 3. Các thư viện sử dụng

| Thư viện | Version | Mục đích |
|---|---|---|
| **pycryptodome** | 3.23.0 | AES, 3DES encryption (Lab 1) |
| **python-dotenv** | >=1.0.0 | Đọc biến môi trường (Lab 3 - Task 6) |
| **OpenSSL** (C library) | hệ thống | RSA BIGNUM operations (Lab 3 - rsa.c) |

> Các thư viện chuẩn: `hashlib`, `os`, `platform`, `sys`, `base64` — không cần cài đặt thêm.

---

## 4. Hướng dẫn cài đặt

```bash
# Cài đặt Python dependencies
pip install -r requirements.txt

# Biên dịch RSA (C + OpenSSL) - Linux/macOS
cd N23DCCN001_DangKimAn
gcc rsa.c lib.c -o output -lcrypto
```

---

## 5. Cấu trúc thư mục

```
d-dev-is_security_group1_lab5/
│
├── main.py                      # Unified toolkit - điểm khởi đầu duy nhất
├── config.py                    # Cấu hình chung (key sizes, modes, constants)
├── requirements.txt             # Python dependencies
├── test_e2e.py                 # End-to-end test suite (69 tests)
├── README.md                   # File này
│
├── N23DCCN001_DangKimAn/       # Lab 3: RSA
│   ├── RSA.py                  # Giao diện tương tác RSA (Python)
│   ├── rsa.c                  # RSA implementation (C + OpenSSL BIGNUM)
│   ├── lib.c                  # Helper: hex/byte conversion, BIGNUM printing
│   ├── task6.py               # Xác minh chữ ký X.509 (portal.ptit.edu.vn)
│   ├── a.txt                  # Giá trị test: p, q, e (hex)
│   └── requirements.txt
│
├── N23DCCN138_PhamQuocAn/      # Lab 1: Hash Functions
│   ├── main.py                 # Entry point riêng (legacy)
│   ├── utils.py                # Hàm tiện ích chung
│   └── hashing/
│       ├── __init__.py        # Sub-menu Hash + compare_hashes
│       ├── md5_hash.py        # MD5 hash (text & file)
│       └── sha256_hash.py     # SHA-256 hash (text & file)
│
└── N23DCCN071_hoanganh/        # Lab 1: AES/3DES + Lab 4: PKI
    ├── AES_3DES/
    │   ├── main.py             # Entry point riêng (legacy)
    │   └── app/
    │       └── symmetric.py    # AES/3DES encrypt & decrypt
    └── PKI/                    # Lab 4: PKI Tasks 1-6
        ├── task1_4_pki_lab/    # Task 1-4: Root CA + ptit.com certificate
        ├── task5_hacker_lab/   # Task 5: Fake CA MITM attack
        ├── task6_compromised_ca_lab/ # Task 6: Compromised CA attack
        ├── evidence/            # Kết quả terminal
        └── apache_configs/      # Apache SSL VirtualHost configs
```

---

## 6. Hướng dẫn chạy

### Chạy bộ công cụ tổng hợp (Khuyến nghị)

```bash
python main.py
```

Menu chính:

```
╔══════════════════════════════════════════╗
║       CRYPTOGRAPHY TOOLKIT           ║
║       Lab 5 - Nhóm 1               ║
╠══════════════════════════════════════════╣
║  1. Symmetric Encryption (AES / 3DES)║
║  2. Asymmetric Encryption (RSA)      ║
║  3. Hash Functions (MD5 / SHA-256)    ║
║  4. PKI Demo (Certificate Info)     ║
║  0. Thoát                           ║
╚══════════════════════════════════════════╝
```

### Chạy từng module riêng lẻ

```bash
# Hash Functions
cd N23DCCN138_PhamQuocAn && python main.py

# AES / 3DES
cd N23DCCN071_hoanganh/AES_3DES && python main.py

# RSA (Python)
cd N23DCCN001_DangKimAn && python RSA.py

# RSA (C + OpenSSL)
cd N23DCCN001_DangKimAn && gcc rsa.c lib.c -o output -lcrypto && ./output
```

### Chạy Test End-to-End

```bash
python test_e2e.py
```

---

## 7. Chi tiết các Lab

### Lab 1: Cryptography Toolkit

**Symmetric Encryption (AES / 3DES)**

| Thuật toán | Key Size | Chế độ | Padding |
|---|---|---|---|
| **AES** | 128/192/256 bit | CBC | PKCS7 |
| **3DES** | 168 bit (hiệu dụng 112 bit) | CBC | PKCS7 |

Các chức năng: tạo khóa ngẫu nhiên, mã hóa, giải mã.

**Asymmetric Encryption (RSA)** — sử dụng giá trị test từ Lab 3:

| Tham số | Giá trị (hex) |
|---|---|
| p | F7E75FDC469067FFDC4E847C51F452DF |
| q | E85CED54AF57E53E092113E62F436F4F |
| e | 0D88C3 |
| n = p × q | (tính tự động) |

Các chức năng: tính d, mã hóa, giải mã, ký, xác minh.

**Hash Functions**

| Thuật toán | Output Size | Trạng thái |
|---|---|---|
| **MD5** | 128 bit (32 hex chars) | Hoàn thành |
| **SHA-256** | 256 bit (64 hex chars) | Hoàn thành |

---

### Lab 2: MD5 Collision Attack

Lab này yêu cầu môi trường Linux với tool `md5collgen`. Các bước chính:

**Task 1**: Tạo 2 file khác nhau với cùng MD5 hash (dùng `md5collgen`)

```bash
md5collgen -p prefix.txt -o out1.bin out2.bin
```

**Task 2**: Chứng minh MD5 suffix property:
- Nếu MD5(M) = MD5(N), thì với mọi suffix T: MD5(M+T) = MD5(N+T)

**Task 3**: Tạo 2 file thực thi (.out) có cùng MD5 hash nhưng in ra giá trị khác nhau

**Task 4**: Tạo 2 chương trình C có cùng MD5 hash nhưng thực thi logic khác nhau (benign vs malicious)

---

### Lab 3: RSA Public-Key Encryption and Signature

**Task 1**: Tính private exponent `d = e^(-1) mod phi(n)` từ p, q, e đã cho

**Task 2**: Mã hóa message `"A top secret!"` bằng public key (e, n)

**Task 3**: Giải mã ciphertext đã cho về ASCII text

**Task 4**: Ký message `"I owe you $2000."` bằng private key, so sánh signature khi đổi thành `"$3000"`

**Task 5**: Xác minh signature của Alice cho message `"Launch a missile."`

**Task 6**: Xác minh chữ ký X.509 certificate từ `portal.ptit.edu.vn`:
```bash
openssl s_client -connect portal.ptit.edu.vn:443 -showcerts
```
Lưu certificate → `.pem`, lấy modulus (n), exponent (e), signature → `task6.py`

---

### Lab 4: Public Key Infrastructure (PKI)

**Task 1**: Tạo Root CA — `openssl req -new -x509 -keyout ca.key -out ca.crt`

**Task 2**: Tạo certificate cho `ptit.com` — CSR + ký bởi CA

**Task 3**: Triển khai HTTPS bằng OpenSSL — `openssl s_server -cert server.pem -www`

**Task 4**: Triển khai HTTPS bằng Apache — cấu hình VirtualHost SSL

**Task 5**: MITM với Fake CA:
- Hacker tạo Fake Hacker Root CA (không được browser tin tưởng)
- Hacker tạo certificate giả cho `ptit.com` → Browser **CẢNH BÁO**

**Task 6**: MITM với Compromised CA:
- Hacker lấy được private key của CA thật
- Hacker tạo certificate hợp lệ cho `hacker.com` → Browser **KHÔNG cảnh báo**

---

## 8. Ghi chú bảo mật

- Private keys (`.key`, `.pem`) và `demoCA/` không được commit lên GitHub
- MD5 và DES không còn an toàn cho mục đích bảo mật thực tế — chỉ dùng để **học tập**
- SHA-256 là thuật toán hash được khuyến nghị sử dụng
- RSA key size 2048-bit trở lên được khuyến nghị cho production
- Root CA private key là tài sản quan trọng nhất của hệ thống PKI

---

## 9. Mục lục đầy đủ

```
1.  Giới thiệu Project
2.  Cấu trúc nhóm
3.  Các thư viện sử dụng
4.  Hướng dẫn cài đặt
5.  Cấu trúc thư mục
6.  Hướng dẫn chạy
7.  Chi tiết các Lab
    7.1 Lab 1: Cryptography Toolkit
    7.2 Lab 2: MD5 Collision Attack
    7.3 Lab 3: RSA Public-Key Encryption
    7.4 Lab 4: PKI
8.  Ghi chú bảo mật
9.  Mục lục đầy đủ
```
