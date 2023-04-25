def generate_long_username(max_allowed_length):
    long_username = ""
    while len(long_username) <= max_allowed_length:
        long_username += "a"

    return long_username

length = 255
print(generate_long_username(length))
print(len(generate_long_username(length)))