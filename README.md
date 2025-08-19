
# 📚 AudioBookGenerator - 一键生成有声书视频

> 一个基于 Python 的自动化工具，将文本转换为带语音朗读与背景画面的有声书视频，适用于教学视频、朗读内容、知识分享等场景。

<div align="center">
  <img src="./2A2.png" alt="Demo 示例截图" width="200" />
</div>

---

## ✅ 功能亮点

- 🔊 **文本转语音 (TTS)**：支持本地或远程语音引擎，清晰自然
- 🎬 **自动生成视频画面**：配合背景图/视频 + 滚动字幕，打造沉浸式体验
- 🖱️ **图形化界面 (GUI)**：非技术用户也能轻松上手
- 📄 **PDF 提取**：使用 `pdfplumber` 快速提取文档文字
- 🖼️ **OCR 识别**：通过 EasyOCR 从图片中提取中文/英文文本
- 🧹 **文本清理工具**：去除换行、冗余空格，提升朗读流畅度
- ⚙️ **高度可配置**：支持自定义字体、语速、分辨率、音频合并方式等

---

## ⚠️ 系统要求

- **操作系统**：仅支持 Windows（因依赖 `moviepy` 和 FFmpeg 环境）
- **Python 版本**：推荐 `Python 3.12.2`（兼容 3.9+）
---

## 🛠️ 安装指南

### 1. 安装 Python

👉 下载并安装 [Python 3.12.2](https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe)

安装时请勾选 **“Add Python to PATH”**

验证安装：
```bash
python --version
# 应输出：Python 3.12.2
```

---

### 2. 安装项目依赖

```bash
pip install -r requirements.ini
```

> 💡 注意：`requirements.ini` 是你的依赖文件名，通常标准为 `requirements.txt`，建议重命名为 `requirements.txt` 以符合惯例。

---

### 3. 安装额外依赖（OCR 与 PDF 支持）

```bash
pip install easyocr pdfplumber
```

> 📌 提示：EasyOCR 首次运行会自动下载模型（约 50MB），请确保网络畅通。

---

### 4. 安装 FFmpeg（关键步骤）

本工具依赖 FFmpeg 进行音视频合成，请务必正确安装并配置环境变量。

#### 安装步骤：

1. 下载完整版 FFmpeg：  
   🔗 [https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)

2. 解压后，将 `ffmpeg/bin` 目录添加到系统环境变量 `PATH` 中。

3. 验证安装：
```bash
ffmpeg -version
```
若显示版本信息，则安装成功 ✅

---

## 🧩 配置说明（config.ini）

你可以根据需求修改以下参数：

```ini
[general]
frameX = 1080           ; 视频宽度（像素）
frameY = 1920           ; 视频高度（像素），默认竖屏 9:16（适合手机）
fontName = AlibabaPuHuiTi-3-55-Regular.ttf  ; 使用的字体文件（需放在项目目录）
rate = 300              ; TTS 语速（单位：字/分钟，可调范围 150~400）
server = localhost:5001 ; 当 audioConcentrator=getAudio2 时，指定 TTS 服务地址
```

> ✅ 推荐字体：[阿里巴巴普惠体](https://alibabafonts.taobao.com/)（免费可商用）

---

## 🚀 使用方式

### 方式一：命令行运行

```bash
python gg.py content.txt
```

支持直接输入文本：
```bash
python gg.py "这是一个测试句子。"
```

---

### 方式二：图形界面（推荐新手使用）

双击运行：
```
有声书生成器可视化界面.cmd
```

无需代码，拖拽或粘贴文本即可生成视频。

---

## 🧰 辅助工具一览

| 工具 | 说明 |
|------|------|
| `quickOCR.py` | 从图片中快速提取文字（支持中英文） |
| `ExtractPDF.py` | 从 PDF 文件提取纯文本内容 |
| `replacen.exe` | 去除文本中的所有换行符（Windows 小工具） |

### 示例用法：

```bash
# OCR 图片识别
python quickOCR.py image.png

# 提取 PDF 文本
python ExtractPDF.py book.pdf

# 清理换行（生成单行文本）
replacen.exe input.txt > output.txt

# 生成有声书视频
python gg.py cleaned_text.txt
```

---

## 📁 输出路径

所有生成的音频、视频文件默认保存在项目根目录下：


---

## ❗ 常见问题

| 问题 | 解决方案 |
|------|----------|
| `ModuleNotFoundError` | 检查是否安装了所有依赖，尤其是 `easyocr` 和 `pdfplumber` |
| `FFmpeg not found` | 确保已添加 `ffmpeg/bin` 到系统 PATH 并重启终端 |
| GUI 启动闪退 | 右键 `.cmd` 文件 → “以管理员身份运行”，或查看日志输出 |
| 字体显示乱码 | 确保 `fontName` 指向正确的 `.ttf` 文件，且支持中文 |

---

## 🤝 贡献与反馈

欢迎提交 Issue 或 Pull Request！  
如果你有以下想法，非常期待你的参与：
- 支持 macOS/Linux
- 多语言语音切换（英文、日文等）
- 添加背景音乐淡入淡出
- 批量处理多个文本文件
- Web 版前端界面

---

