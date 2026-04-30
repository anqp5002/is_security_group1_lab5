# PKI Lab - N23DCCN071 Hoàng Anh

## Thông tin

- Họ tên: Hồ Ngọc Hoàng Anh
- Mã sinh viên: N23DCCN071
- Vai trò: Người 2
- Phần phụ trách: Public Key Infrastructure - PKI

## Nội dung thực hiện

Thư mục này chứa phần thực hành PKI của Người 2.

Các task đã thực hiện:

- Task 1: Becoming a Certificate Authority
- Task 2: Creating a Certificate for ptit.com
- Task 3: Deploying Certificate on HTTPS Server Using OpenSSL
- Task 4: Deploying Certificate on Apache HTTPS Website
- Task 5: Launching a MITM Attack with Fake CA
- Task 6: Launching a MITM Attack with Compromised CA

## Cấu trúc thư mục

PKI/
- task1_4_pki_lab/
- task5_hacker_lab/
- task6_compromised_ca_lab/
- evidence/

## task1_4_pki_lab

Thư mục này chứa các file liên quan đến Task 1 đến Task 4.

Nội dung chính:

- Tạo Root CA bằng OpenSSL.
- Tạo certificate cho domain ptit.com.
- Triển khai HTTPS bằng OpenSSL s_server.
- Triển khai HTTPS bằng Apache.

Một số file chính:

- ca.crt
- server.crt
- server.csr
- server_ext.cnf
- openssl.cnf

Ghi chú:

- ca.key không được upload lên GitHub.
- server.key không được upload lên GitHub.
- demoCA không được upload lên GitHub.

## task5_hacker_lab

Thư mục này chứa các file liên quan đến Task 5.

Nội dung chính:

- Tạo Fake Hacker Root CA.
- Tạo certificate giả cho ptit.com.
- Dùng certificate giả để mô phỏng MITM Attack.
- Quan sát Firefox cảnh báo vì Fake Hacker Root CA không được tin cậy.

Một số file chính:

- ca-hacker.crt
- hacker.crt
- hacker.csr
- openssl.cnf

Ghi chú:

- ca-hacker.key không được upload lên GitHub.
- hacker.key không được upload lên GitHub.

## task6_compromised_ca_lab

Thư mục này chứa các file liên quan đến Task 6.

Nội dung chính:

- Mô phỏng tình huống CA thật bị compromise.
- Dùng CA thật để ký certificate cho hacker.com.
- Phân tích rủi ro khi private key của Root CA bị lộ.
- Quan sát browser có thể không cảnh báo nếu certificate được ký bởi CA đã tin cậy.

Một số file chính:

- trusted-ca.crt
- hacker6.crt
- hacker6.csr
- openssl.cnf

Ghi chú:

- trusted-ca.key không được upload lên GitHub.
- hacker6.key không được upload lên GitHub.

## evidence

Thư mục này chứa kết quả kiểm tra bằng terminal.

Các file chính:

- task1_task2_result.txt
- task5_fake_ca_result.txt
- task6_compromised_ca_result.txt

Các file evidence dùng để chứng minh:

- CA đã được tạo.
- Certificate của ptit.com đã được ký bởi CA.
- Certificate giả ở Task 5 được ký bởi Fake Hacker Root CA.
- Certificate ở Task 6 được ký bởi CA thật bị compromise.

## Ghi chú bảo mật

Các private key không được upload lên GitHub.

Các file không upload:

- *.key
- *.pem
- demoCA/

Chỉ giữ lại certificate, CSR, config và evidence để làm minh chứng cho quá trình thực hiện.
