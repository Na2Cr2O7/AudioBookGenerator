
# 📚 AudioBookGenerator - 合成有声书视频的工具

> 一个用于将文本自动合成为有声书视频的工具，适用于生成教学视频、朗读视频等内容。

## ⚠️ 仅支持 Windows 系统

---

## ✅ 功能简介

- 文本转语音（TTS）
- 支持 GUI 图形界面操作
- 提供 PDF 提取、OCR 识别、文本清理等辅助脚本

---

## 🛠️ 安装指南

### 1. 安装依赖包

```bash
pip install -r requirements.ini
```

### 2. 安装 FFmpeg（新增）

> **注意：此工具依赖 FFmpeg，请确保已安装并配置好环境变量。**

#### 安装方法：

1. 前往 [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/) 下载 Windows 版本。
2. 解压后将 `ffmpeg/bin` 路径添加到系统环境变量 `PATH` 中。
3. 验证安装：

```bash
ffmpeg -version
```

如果输出版本信息，则表示安装成功。

---

## 🧰 使用方式

### 方式一：命令行运行

```bash
python gg.py [文本文件或直接输入的文本]
```

### 方式二：图形界面运行

```bash
有声书生成器可视化界面.cmd
```

---

## ⚙️ 配置选项

你可以在 `config.ini` 中修改以下设置：

- 视频帧宽度与高度
---

## 📎 辅助工具

| 工具名             | 功能描述                             |
|------------------|------------------------------------|
| `quickOCR.py`     | 快速从图片中提取文字                   |
| `ExtractPDF.py`   | 从 PDF 文件中提取纯文本                 |
| `replacen.exe`    | 去除文本中的所有换行符                  |

---
#### 你需要安装easyOCR和pdfplumber
```python
pip install easyocr
pip install pdfplumber
```

## 📝 示例用法

```bash
# 使用 OCR 提取图片中的文字
python quickOCR.py image.png

# 从 PDF 提取文本
python ExtractPDF.py book.pdf

# 合成有声书视频
python gg.py content.txt
```

---

## 💡 注意事项

- 所有生成文件保存在根文件夹中。
- 如遇音频/视频处理错误，请确认 FFmpeg 是否正确安装。
- GUI 版本更适合非技术用户使用。

---

如有问题欢迎提交 Issue 或联系作者。欢迎贡献代码和改进建议！
