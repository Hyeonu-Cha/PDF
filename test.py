import os
from PyPDF2 import PdfReader, PdfWriter

def batch_remove_password(input_folder, output_folder, password):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.pdf'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            try:
                reader = PdfReader(input_path)
                reader.decrypt(password)

                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)

                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)

                print(f"Password removed for: {file_name}")
            except Exception as e:
                print(f"Failed to process {file_name}: {e}")

# Configure paths and password, example
input_folder = r"C:\Users\gotow\Downloads\input"
output_folder = r"C:\Users\gotow\Downloads\output"
password = "psw"

batch_remove_password(input_folder, output_folder, password)
