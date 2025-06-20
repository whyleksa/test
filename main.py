def reverse_string(string):
    index = len(string) - 1
    reversed_string = ""
    
    while index >= 0:
        current_char = string[index]
        reversed_string = reversed_string + current_char
        index = index - 1
    
    return reversed_string

def main():
    user_input = input("Введите текст, который нужно перевернуть: ")
    result = reverse_string(user_input)
    print(f"Перевернутый текст: {result}")

main()  # Просто вызываем функцию напрямую!