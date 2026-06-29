def caesar_cipher(text, shift, mode):
    result = ""
    if mode.lower() == 'decrypt':
        shift = -shift      

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


def main():
    print("--- Caesar Cipher Program ---")

    while True:
        mode = input("Choose an option (encrypt / decrypt / quit): ").strip().lower()

        if mode == 'quit':
            print("Goodbye!")
            break

        if mode not in ['encrypt', 'decrypt']:
            print("Invalid option. Please type 'encrypt', 'decrypt', or 'quit'.\n")
            continue

        message = input("Enter your message: ")

        try:
            shift = int(input("Enter shift value (integer): "))
        except ValueError:
            print("Please enter a valid integer for the shift value.\n")
            continue

        output = caesar_cipher(message, shift, mode)
        print(f"Result ({mode}ed): {output}\n")


if __name__ == "__main__":
    main()
