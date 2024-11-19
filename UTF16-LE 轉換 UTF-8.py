import os

def is_utf8(file):
    #檢查文件是否是UTF-8編碼，如果是則跳過
    try:
        with open(file, 'r', encoding='utf-8') as f:
            f.read()
        return True
    except UnicodeDecodeError:
        return False

def convert_to_utf8(file):
    #將UTF-16LE文件轉換為UTF-8 With BOM
    with open(file, 'r', encoding='utf-16le') as f:
        content = f.read()

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

def remove_bom(file):
    #移除UTF-8文件的BOM字元
    BOM = b'\xef\xbb\xbf'
    with open(file, 'rb') as f:
        if f.read(3) == BOM:
            content = f.read()
            with open(file, 'wb') as f:
                f.write(content)

if __name__ == '__main__':
    folder_path = "C:\IN"  
    # 修改為你的資料夾路徑，可指定最上層，他會連下層內所有的檔案都一起變更
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):  # 只處理.txt文件
                file_path = os.path.join(root, file)
                if not is_utf8(file_path):
                    convert_to_utf8(file_path)
                remove_bom(file_path)               

#Yen Yu & ChatGPT製作
#2024/07/31