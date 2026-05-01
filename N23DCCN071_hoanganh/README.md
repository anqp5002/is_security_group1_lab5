# Lab 5 - N23DCCN071 Hoàng Anh

## Thông tin sinh viên

- Họ tên: Hồ Ngọc Hoàng Anh
- Mã sinh viên: N23DCCN071
- Vai trò trong nhóm: Người 2

## Nội dung phụ trách

Người 2 phụ trách hai phần chính trong Lab 5:

### 1. Cryptography Toolkit

Phần code trong project Cryptography Toolkit:

- AES Encrypt / Decrypt
- 3DES Encrypt / Decrypt
- Random key generator
- Kiểm tra key size
- Xử lý lỗi input không hợp lệ

Thư mục chứa phần này:

- AES_3DES/

### 2. Public Key Infrastructure - PKI

Phần thực hành PKI gồm 6 task:

- Task 1: Becoming a Certificate Authority
- Task 2: Creating a Certificate for ptit.com
- Task 3: Deploying Certificate on HTTPS Server Using OpenSSL
- Task 4: Deploying Certificate on Apache HTTPS Website
- Task 5: Launching a MITM Attack with Fake CA
- Task 6: Launching a MITM Attack with Compromised CA

Thư mục chứa phần này:

- PKI/

## Cấu trúc thư mục

N23DCCN071_hoanganh/
- README.md
- AES_3DES/
  - Source code phần AES và 3DES
- PKI/
  - task1_4_pki_lab/
  - task5_hacker_lab/
  - task6_compromised_ca_lab/
  - evidence/

## Ghi chú bảo mật

Các file private key không được upload lên GitHub.

Các file không upload:

- *.key
- *.pem
- demoCA/

Các file được giữ lại để làm minh chứng:

- certificate file: *.crt
- certificate signing request: *.csr
- file cấu hình: openssl.cnf
- file evidence kết quả chạy lệnh
