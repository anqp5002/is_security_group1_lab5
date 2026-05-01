from app.symmetric import generate_key, encrypt_data, decrypt_data


def algorithm_menu(algorithm):
    while True:
        print(f"\n===== {algorithm} MENU =====")
        print("1. Tạo key ngẫu nhiên")
        print("2. Mã hóa")
        print("3. Giải mã")
        print("0. Quay lại")

        choice = input("Chọn: ")

        if choice == "1":
            key = generate_key(algorithm)
            print(f"Key {algorithm}: {key}")

        elif choice == "2":
            plaintext = input("Nhập plaintext: ")

            auto_key = input("Tạo key ngẫu nhiên? (y/n): ").lower()

            if auto_key == "y":
                key = generate_key(algorithm)
                print(f"Key {algorithm}: {key}")
            else:
                key = input(f"Nhập key {algorithm} dạng Base64: ")

            ciphertext = encrypt_data(algorithm, plaintext, key)
            print("Ciphertext:", ciphertext)

        elif choice == "3":
            ciphertext = input("Nhập ciphertext dạng Base64: ")
            key = input(f"Nhập key {algorithm} dạng Base64: ")

            plaintext = decrypt_data(algorithm, ciphertext, key)
            print("Plaintext:", plaintext)

        elif choice == "0":
            break

        else:
            print("Lựa chọn không hợp lệ.")


def symmetric_menu():
    while True:
        print("\n===== SYMMETRIC ENCRYPTION =====")
        print("1. 3DES")
        print("2. AES")
        print("0. Quay lại")

        choice = input("Chọn thuật toán: ")

        if choice == "1":
            algorithm_menu("3DES")
        elif choice == "2":
            algorithm_menu("AES")
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")


def main_menu():
    while True:
        print("\n===== CRYPTOGRAPHY TOOLKIT =====")
        print("1. Symmetric Encryption")
        print("2. Asymmetric Encryption")
        print("3. Hash Functions")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            symmetric_menu()
        elif choice == "2":
            print("Phần RSA do thành viên khác làm.")
        elif choice == "3":
            print("Phần Hash do thành viên khác làm.")
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main_menu()
