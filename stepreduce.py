import os
import subprocess
import sys

def reduce_step_file(input_file, output_file):
    """
    使用stepreduce.exe工具来压缩STEP文件。
    """
    try:
        subprocess.run(["stepreduce.exe", input_file, output_file], check=True)
        print(f"成功压缩文件: {input_file} -> {output_file}")
        os.remove(input_file)

    except subprocess.CalledProcessError as e:
        print(f"压缩文件时出错: {e}")

def process_directory(input_directory, output_directory):
    """
    遍历给定目录下的STEP文件，压缩并输出带后缀_small的STEP文件到指定的输出目录。
    """
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.lower().endswith(".stp") or file.lower().endswith(".step"):
                if file.lower().endswith("_small.stp") or file.lower().endswith("_small.step"):
                    break
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_directory, f"{os.path.splitext(file)[0]}_small.step")
                reduce_step_file(input_file_path, output_file_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python script.py <输入目录路径> <输出目录路径>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    if not os.path.isdir(input_directory):
        print("错误: 提供的输入路径不是一个目录。")
        sys.exit(1)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    process_directory(input_directory, output_directory)
