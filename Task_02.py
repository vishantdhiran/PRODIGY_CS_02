from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    try:
        print(f"Trying to open the image from path: {image_path}")
        # Open the image
        img = Image.open(image_path)
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return
    except PermissionError:
        print("Permission denied. Please check your file permissions.")
        return

    # Convert image to numpy array
    img_array = np.array(img)

    # Encrypt the image by applying a basic mathematical operation
    encrypted_array = (img_array + key) % 256

    # Convert encrypted array back to image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))

    # Save encrypted image
    encrypted_img.save('encrypted_image.png')
    print("Encryption complete. Encrypted image saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key):
    try:
        print(f"Trying to open the encrypted image from path: {encrypted_image_path}")
        # Open the encrypted image
        encrypted_img = Image.open(encrypted_image_path)
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return
    except PermissionError:
        print("Permission denied. Please check your file permissions.")
        return

    # Convert image to numpy array
    encrypted_array = np.array(encrypted_img)

    # Decrypt the image by reversing the mathematical operation
    decrypted_array = (encrypted_array - key) % 256

    # Convert decrypted array back to image
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))

    # Save decrypted image
    decrypted_img.save('decrypted_image.png')
    print("Decryption complete. Decrypted image saved as 'decrypted_image.png'.")

def main():
    while True:
        choice = input("Would you like to encrypt or decrypt an image? (e/d): ").lower()
        if choice in ['e', 'd']:
            image_path = input("Enter the path to the image file: ").strip()
            key = int(input("Enter the encryption/decryption key (integer value): "))

            if choice == 'e':
                encrypt_image(image_path, key)
            else:
                decrypt_image(image_path, key)
        else:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

        another = input("Would you like to encrypt/decrypt another image? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
