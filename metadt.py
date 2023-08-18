import json

## Hàm gộp file
def combine_json_files(file_names, output_filename):
    combined_metadata = {
        "files": []
    }

    for file_name in file_names:
        with open(file_name, 'r') as file:
            data = json.load(file)
            combined_metadata["files"].append({
                "name": file_name,
                "metadata": data
            })

    with open(output_filename, 'w') as output_file:
        json.dump(combined_metadata, output_file, indent=4)

    print(f"Tổng hợp thành công vào {output_filename}")

input_files = ["file1.json", "file2.json", "file3.json", "file4.json", "file5.json"]
output_file = "combined_files.json"

combine_json_files(input_files, output_file)

# Đọc nội dung của file "combined_files"
with open("combined_files.json", "r") as file:
    combined_data = json.load(file)

# Nhập danh sách các thông tin metadata và danh sách các tên file
metadata_list = input("Nhập danh sách metadata (cách nhau bằng dấu phẩy): ").lower().split(", ")
name_list = input("Nhập danh sách tên file (cách nhau bằng dấu phẩy): ").split(", ")

# Tạo danh sách để lưu các tên file phù hợp và không phù hợp với metadata
matching_names = []
non_matching_names = []

# Duyệt qua từng file trong danh sách
for file_info in combined_data["files"]:
    file_name = file_info["name"]
    file_metadata = file_info["metadata"]

    # Kiểm tra xem tất cả các metadata nhập vào có trong danh sách metadata của file (không phân biệt hoa thường)
    if all(metadata.lower() in [value.lower() for value in file_metadata.values()] for metadata in metadata_list):
        # Kiểm tra xem tên file có trong danh sách tên nhập vào
        if file_name in name_list:
            matching_names.append(file_name)
    else:
        non_matching_names.append(file_name)

# Lọc các tên file còn lại sau khi đã lọc ra từ matching_names
remaining_names = [name for name in name_list if name not in matching_names]

# In danh sách các tên file phù hợp và không phù hợp
print("\nDanh sách các tệp chứa metadata cần tìm:")
for name in matching_names:
    print(name)

print("\nDanh sách các tệp không chứa metadata cần tìm:")
for name in remaining_names:
    print(name)
