<p align="center">
  <img alt="Imagecli"  width="260" src="https://private-user-images.githubusercontent.com/46949537/430684829-e19917c0-6d16-4ff6-8de5-866967451410.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5MjQzNjgsIm5iZiI6MTc0MzkyNDA2OCwicGF0aCI6Ii80Njk0OTUzNy80MzA2ODQ4MjktZTE5OTE3YzAtNmQxNi00ZmY2LThkZTUtODY2OTY3NDUxNDEwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA0MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNDA2VDA3MjEwOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTZiMjA0YzhhMmViNzJjYzgyMzJmMTg5ZWQ2OTk2MTExYjU5ODQxMDdmMzdkYThkYjFmZmQxOWUxZDE5MDVlOGYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.-Fa6Tv60ZssWQjHpfzTrptYibMnRcz0fK-cWldAk3Os">
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


## 下载安装
```shell 
pip install open-image-cli
`````

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
| Original Backgdound Photo        | RED Background Photo         | WHITE Background Photo        |
|-----------------------|------------------------------|-------------------------------|
| <img src="https://private-user-images.githubusercontent.com/46949537/430684826-817c9758-3815-4043-8e4a-d7f9adecddc6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5MjQzNjgsIm5iZiI6MTc0MzkyNDA2OCwicGF0aCI6Ii80Njk0OTUzNy80MzA2ODQ4MjYtODE3Yzk3NTgtMzgxNS00MDQzLThlNGEtZDdmOWFkZWNkZGM2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA0MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNDA2VDA3MjEwOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWJiNGJjNjQxMTNhY2ZjZDdiY2U1OGRlM2EyYzY2N2QxZGFiYTk3NjNkODA1NTM5OWFmZjg5NzZlNDVmYTY1N2YmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.fGWxgCMcNoOoxXCOMNq3h4pzZ8nJ94Ld9-7i5TlMPwM" alt="Original Photo" width="100"/> | <img src="https://private-user-images.githubusercontent.com/46949537/430684828-f09eaef5-fce7-4702-a327-e67305fbc5f8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5MjQzNjgsIm5iZiI6MTc0MzkyNDA2OCwicGF0aCI6Ii80Njk0OTUzNy80MzA2ODQ4MjgtZjA5ZWFlZjUtZmNlNy00NzAyLWEzMjctZTY3MzA1ZmJjNWY4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA0MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNDA2VDA3MjEwOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNmNzJhMmRlZDliZGI1NjdmZDQ0ODM4YWZjZGViOGViMGNhYTEwZjQ2YTMxNjUxNjcyNTUyY2E2NDNhMmI4M2EmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.LAETS0iVKwARO75up4d4ObmUbmyaRwodF350s-KrmcU" alt="RED Background Photo" width="100"/> | <img src="https://private-user-images.githubusercontent.com/46949537/430684827-2f8b7185-5f24-4033-ac47-2f845237ac37.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5MjQzNjgsIm5iZiI6MTc0MzkyNDA2OCwicGF0aCI6Ii80Njk0OTUzNy80MzA2ODQ4MjctMmY4YjcxODUtNWYyNC00MDMzLWFjNDctMmY4NDUyMzdhYzM3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA0MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNDA2VDA3MjEwOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTkyOTA2MWRjZmI1M2FiOWZkZjQxZTg0Y2VkNTdjMzE4YzNhN2E0M2EyZmE3MDgxZDU0YmJkYjFlMmFmNjBjNzcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.4xVkHztn-5bu1cKMnXa3bJi6F53ruINnXIsSJhEWch4" alt="WHITE Background Photo" width="100"/> |
