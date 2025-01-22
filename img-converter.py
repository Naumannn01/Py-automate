from PIL import Image
import os

# Define input and output folder paths
input_folder = r"C:/Users/HP/Desktop/img-converter/imp-jpg"
output_folder = os.path.join(input_folder, "output2_webp")
os.makedirs(output_folder, exist_ok=True)

# Target file size in bytes (200 KB = 200 * 1024)
max_file_size = 200 * 1024  

# Convert all JPG images in the input folder
for file in os.listdir(input_folder):
    if file.lower().endswith(".jpg"):
        try:
            file_path = os.path.join(input_folder, file)
            img = Image.open(file_path)
            
            output_file = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.webp")
            
            # Start with a high quality and gradually reduce if needed
            quality = 95
            while True:
                # Save the image with the current quality
                img.save(output_file, "WEBP", quality=quality)
                
                # Check the file size
                if os.path.getsize(output_file) <= max_file_size or quality <= 10:
                    break
                
                # Reduce the quality for the next iteration
                quality -= 5
            
        except Exception as e:
            print(f"Error converting {file}: {e}")
        
print("Conversion complete!")









# exit()
# from PIL import Image
# import os

# # Define input and output folder paths
# input_folder = r"C:/Users/HP/Desktop/img-converter/imp-jpg"
# output_folder = os.path.join(input_folder, "output_webp")
# os.makedirs(output_folder, exist_ok=True)

# # Convert all JPG images in the input folder
# for file in os.listdir(input_folder):
#     if file.endswith(".jpg"):
#         file_path = os.path.join(input_folder, file)
#         img = Image.open(file_path)
#         output_file = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.webp")
#         img.save(output_file, "WEBP")
        
# print("Conversion complete!")
