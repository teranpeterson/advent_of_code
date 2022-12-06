import hashlib

i = 0
while True:
    i += 1

    text = "yzbqklnj" + str(i)

    m = hashlib.md5()
    m.update(text.encode('UTF-8'))
    if m.hexdigest().startswith("00000"):
        print(i)
        break
