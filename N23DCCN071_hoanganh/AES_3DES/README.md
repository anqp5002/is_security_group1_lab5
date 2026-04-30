# AES và 3DES - N23DCCN071 Hoàng Anh

## Thông tin

- Họ tên: Hồ Ngọc Hoàng Anh
- Mã sinh viên: N23DCCN071
- Vai trò: Người 2
- Phần phụ trách: AES và 3DES trong Cryptography Toolkit

## Nội dung thực hiện

Thư mục này chứa source code phần mã hóa đối xứng do Người 2 phụ trách.

Các chức năng chính:

- AES Encrypt
- AES Decrypt
- 3DES Encrypt
- 3DES Decrypt
- Random key generator
- Kiểm tra key size
- Xử lý lỗi input không hợp lệ

## AES

AES là thuật toán mã hóa đối xứng hiện đại, được sử dụng phổ biến trong các hệ thống bảo mật.

Trong project này, AES được dùng để:

- Mã hóa plaintext thành ciphertext.
- Giải mã ciphertext về plaintext ban đầu.
- Kiểm tra khóa hợp lệ trước khi mã hóa hoặc giải mã.
- Hỗ trợ tạo khóa ngẫu nhiên để người dùng không phải nhập key thủ công.

## 3DES

3DES là thuật toán mã hóa đối xứng được phát triển từ DES.

Trong project này, 3DES được dùng để:

- Mã hóa plaintext thành ciphertext.
- Giải mã ciphertext về plaintext ban đầu.
- Kiểm tra khóa hợp lệ trước khi mã hóa hoặc giải mã.
- Hỗ trợ tạo khóa ngẫu nhiên đúng kích thước.

## Vai trò trong project

Phần AES và 3DES thuộc nhóm chức năng Symmetric Encryption của Cryptography Toolkit.

Nhóm chức năng này giúp người dùng thực hiện mã hóa và giải mã dữ liệu bằng các thuật toán mã hóa đối xứng.

## Xử lý lỗi

Phần code cần xử lý các trường hợp lỗi như:

- Key sai kích thước.
- Input bị thiếu.
- Ciphertext sai định dạng.
- Người dùng chọn sai chức năng.

Mục tiêu là chương trình báo lỗi rõ ràng thay vì bị crash.
