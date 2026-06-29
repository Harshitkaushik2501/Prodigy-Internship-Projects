from PIL import Image

def process_image(input_path, output_path):
    try:
        image = Image.open(input_path)

        encrypted_image = image.rotate(180)

        encrypted_image.save(output_path)

        print("Image processed successfully!")
        print("Saved as:", output_path)

    except Exception as e:
        print("Error:", e)


print("=== Simple Image Encryption Tool ===")

input_image = input("Enter input image path: ")
output_image = input("Enter output image path: ")

process_image(input_image, output_image)
