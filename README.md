<p align="center">
  <img alt="Imagecli"  width="260" src="static/logo.png">
</p>


<h1 align="center">ImageCli</h1>
<div align="center">
    A natural language described, out of the box 📷 image command line tools. 🔧
</div>


<div align="center">

[English](./README.md) | [简体中文](./README_ZH.md)

</div>


## Overview
ImageCli is a simple command-line interface designed to effectively handle image operations, allowing users to perform basic tasks through simple descriptive commands (without the need to understand complex tool design, speak freely)

## Examples

### 1. Image size
```bash
img size -f '/Users/youngfreefjs/Downloads/logo.png'

>> Image Pixels Size: 1024x1024
```

### 2. Image file size
```bash
img file-size -f '/Users/youngfreefjs/Downloads/logo.png'

>> Image File Size: 496470.00 bytes
```
Specify Return Unit  
You can also specify the output unit for the file size (e.g. bytes, KB, MB):
```bash
img file-size -f '/Users/youngfreefjs/Downloads/logo.png' -u MB

>> Image File Size: 0.47 MB
```

### 3. Compress image file size
```bash
img compress -f '/Users/youngfreefjs/Downloads/logo.png' -t 0.1 -u MB

>> Compressed image saved to: /Users/youngfreefjs/Downloads/compressed_logo.png
>> Compressed Image Size: 0.09 MB
```
