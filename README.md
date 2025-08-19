![1](/2A2.png)

# 📚 AudioBookGenerator - 合成有声书视频的工具

> 一个用于将文本自动合成为有声书视频的工具，适用于生成教学视频、朗读视频等内容。

### ⚠️ **仅支持 Windows 系统**

---

## ✅ 功能简介

- 文本转语音（TTS）
- 自动生成背景视频画面
- 支持 GUI 图形界面操作
- 提供 PDF 提取、OCR 识别、文本清理等辅助脚本

---

## 🛠️ 安装指南

### 1. 安装 Python（推荐版本）

请先安装 Python（建议使用 Python 3.12.2）：

🔗 [Python 3.12.2 下载地址](https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe)

安装完成后，在命令行中验证是否成功：

```bash
python --version
```

### 2. 安装项目依赖

```bash
pip install -r requirements.ini
```

### 3. 安装 EasyOCR 和 pdfplumber（额外依赖- 提供 PDF 提取、OCR 识别、文本清理等辅助脚本）

这两个库未包含在 `requirements.ini` 中，请手动安装：

```bash
pip install easyocr pdfplumber
```

### 4. 安装 FFmpeg

> **⚠️ 注意：此工具依赖 FFmpeg，请确保已安装并配置好环境变量。**

#### 安装方法：

1. 下载地址（推荐完整版）：
   🔗 [https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)
2. 解压后将 `ffmpeg/bin` 路径添加到系统环境变量 `PATH` 中。
3. 验证安装：

```bash
ffmpeg -version
```

如果输出版本信息，则表示安装成功。
## config.ini
```text
[general]
frameX=1080;输出大小
frameY=1920
fontName=AlibabaPuHuiTi-3-55-Regular.ttf ;字体文件
rate=300 ;TTS音调
server=localhost:5001 ;getAudioBackends=getAudio2时选择地址，(http://{server}/{text})
audioConcentrator=moviepy ;or wavConcentrator
;使用moviepy或者wavConcentrator合并音频
```
---

## 🧰 使用方式

### 方式一：命令行运行

```bash
python gg.py [文本文件或直接输入的文本]
```

示例：

```bash
python gg.py content.txt
```

### 方式二：图形界面运行

双击运行：

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

## 📝 示例用法

```bash
# 使用 OCR 提取图片中的文字
python quickOCR.py image.png

# 从 PDF 提取文本
python ExtractPDF.py book.pdf

# 合成有声书视频
python gg.py content.txt

# 去除换行
replacen.exe 1.txt>2.txt
```

---

## 💡 注意事项

- 所有生成文件默认保存在根目录下。
- 如遇音频/视频处理错误，请确认 FFmpeg 是否正确安装。
- GUI 版本更适合非技术用户使用。
- 编码为 UTF-8。

---

如有问题欢迎提交 Issue 或联系作者。欢迎贡献代码和改进建议！
