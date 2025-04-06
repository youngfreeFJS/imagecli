<p align="center">
  <img alt="Imagecli"  width="260" src="static/logo.png">
</p>


<h1 align="center">ImageCli</h1>
<div align="center">
    一种开箱即用，使用通用语言描述的 📷 图像命令行工具。🔧
</div>

<div align="center">

[English](./README.md) | [简体中文](./README_ZH.md)

</div>

## 概述
ImageCli是一个简单的命令行界面，旨在有效地处理图像操作，允许用户通过简单的描述性命令执行基本任务（无需理解复杂的工具设计，言出法随🪄）


## 示例

### 1. 获取图像像素尺寸
```bash
img size -f '/Users/youngfreefjs/Downloads/logo.png'

>> Image Pixels Size: 1024x1024
```

### 2. 获取图像文件大小
```bash
img file-size -f '/Users/youngfreefjs/Downloads/logo.png'

>> Image File Size: 496470.00 bytes
```
设置返回文件大小的单位 (e.g. bytes, KB, MB):
```bash
img file-size -f '/Users/youngfreefjs/Downloads/logo.png' -u MB

>> Image File Size: 0.47 MB
```

### 3. 压缩图片
```bash
img compress -f '/Users/youngfreefjs/Downloads/logo.png' -t 0.1 -u MB

>> Compressed image saved to: /Users/youngfreefjs/Downloads/compressed_logo.png
>> Compressed Image Size: 0.09 MB
```


### 4. 修改照片背景色
```bash
img background -f '/Users/youngfreefjs/Desktop/code/github/imagecli/static/passport_photo_blue.png' -c 'RED' 

>> Image resolution: 1536x1024, Channels: 3
>> Modified image background `red` saved to: /Users/youngfreefjs/Desktop/code/github/imagecli/static/background_RED_passport_photo_blue.png
```
| Original Photo        | RED Background Photo         | WHITE Background Photo        |
|-----------------------|------------------------------|-------------------------------|
| <img src="./static/passport_photo_blue.png" alt="Original Photo" width="100"/> | <img src="./static/background_RED_passport_photo_blue.png" alt="RED Background Photo" width="100"/> | <img src="./static/background_WHITE_passport_photo_blue.png" alt="WHITE Background Photo" width="100"/> |
