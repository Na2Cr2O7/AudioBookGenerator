import tkinter as tk
from tkinter import filedialog, messagebox
import os

PythonDir='python.cmd'

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, text_content)
        entry.delete(0, tk.END)
        entry.insert(tk.END, file_path)
        return file_path
    return None

def run_gg_py():
    file_path = entry.get()

    if not file_path:
        messagebox.showwarning("警告", "未输入文件地址,将使用文本框中的内容作为输入")
        file_path=text_box.get(1.0, tk.END)
        with open('temp.txt', 'w', encoding='utf-8') as file:
            file.write(file_path)
        file_path='temp.txt'
        
    try:
        X=os.system(f'"{PythonDir}" gg.py {file_path}')
    except Exception as e:
        messagebox.showerror("错误", f"{e}")
    if X:
        messagebox.showerror("错误", f"合成音频书失败({X})")
    else:
        messagebox.showinfo("提示", f"合成音频书成功({X})")

# 创建主窗口
root = tk.Tk()
root.title("有声读物生成器可视化界面")

# 创建文本框用于显示文件内容
text_box = tk.Text(root, height=20, width=60)
text_box.pack(pady=20)

# 创建Entry用于显示文件地址
entry = tk.Entry(root, width=60)
entry.pack(pady=10)

# 创建选择文件按钮
open_button = tk.Button(root, text="选择文件", command=open_file)
open_button.pack(side=tk.LEFT, padx=20, pady=20)

# 创建运行gg.py按钮
run_button = tk.Button(root, text="合成音频书", command=run_gg_py)
run_button.pack(side=tk.RIGHT, padx=20, pady=20)

# 运行主循环
root.mainloop()
