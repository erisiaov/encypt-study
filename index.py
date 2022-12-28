import hashlib

plain_pw = str(input("여기에 암호화할 비밀번호 입력"))

lv_encrypt = hashlib.sha256(plain_pw.encode())
encrypt_pw = lv_encrypt.hexdigest()

print(encrypt_pw)