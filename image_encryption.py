from PIL import Image
import random


def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    random.seed(key)
    random.shuffle(pixels)

    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(pixels)
    encrypted_image.save(output_path)
    print(f"Your Encrypted image is saved as {output_path}")


def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    encrypted_pixels = list(image.getdata())

    random.seed(key)

    # Create a list of indices and shuffle them using the same seed
    indices = list(range(len(encrypted_pixels)))
    random.shuffle(indices)

    # Create a list to hold the decrypted pixels
    decrypted_pixels = [None] * len(encrypted_pixels)

    # Place each pixel back to its original position based on shuffled indices
    for i, index in enumerate(indices):
        decrypted_pixels[index] = encrypted_pixels[i]

    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save(output_path)
    print(f"Your Decrypted image is saved as {output_path}")


def main():
    choice = input("Would you like to encrypt or decrypt an image?: ").lower()

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice! Please enter 'encrypt' for encryption or 'decrypt' for decryption.")
        return

    image_path = input("Enter the path to your image file: ")
    output_path = input("Enter the path to save your output image: ")
    key = int(input("Enter the key (integer): "))

    if choice == 'encrypt':
        encrypt_image(image_path, output_path, key)
    else:
        decrypt_image(image_path, output_path, key)


if __name__ == "__main__":
    main()