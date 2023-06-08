# string = "geruvrrucrhhc"
# print(string)
# print(type(string))
# string_encoded_utf = string.encode(encoding="utf-8")
# print(string_encoded_utf)
# print(type(string_encoded_utf))
# string_encoded_utf = string_encoded_utf.decode(encoding="utf-8")
# assert string_encoded_utf == string
# print(string_encoded_utf)

# my_string = "test"
# my_byte_string = my_string.encode(encoding="utf-8")
# # assert my_byte_string == b'test'
# print(my_byte_string)

string_1 = b'r\xc3\xa9sum\xc3\xa9'.decode("utf-8")
print(string_1)
string_2 = string_1.encode("Latin1")
print(string_2)
string_3 = b'r\xe9sum\xe9'.decode("Latin1")
print(string_3)

