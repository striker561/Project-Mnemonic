import os

def save_to_txt(data, file_name):
    os.makedirs("data", exist_ok=True)
    file_name = os.path.join("data", file_name)
    with open(file_name, "w", encoding="utf-8") as txt_file:
        txt_file.write(data)

    print(f"{file_name}' - Saved !!")
