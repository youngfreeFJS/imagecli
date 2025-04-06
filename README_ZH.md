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


## Download
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
| Original Photo        | RED Background Photo         | WHITE Background Photo        |
|-----------------------|------------------------------|-------------------------------|
| <img src="./static/passport_photo_blue.png" alt="Original Photo" width="100"/> | <img src="./static/background_RED_passport_photo_blue.png" alt="RED Background Photo" width="100"/> | <img src="./static/background_WHITE_passport_photo_blue.png" alt="WHITE Background Photo" width="100"/> |


### 5. 合并截图为长图
> Code by: my former company [`@Meituan-Dianping`](https://github.com/Meituan-Dianping/vision-ui/blob/master/resources/vision_merge.md)


> 请保障前面一张截图后，向上滚动1/3再截图第二张图  
你可以手工操作截图（从屏幕高度2/3，向上滑动至1/3）  
或者通过UI自动化截图，屏幕高度2/3 to 1/3

```bash
img merge -i '/Users/youngfreefjs/Desktop/code/github/imagecli/static/image_merge/taobaoPage1.JPG' -i '/Users/youngfreefjs/Desktop/code/github/imagecli/static/image_merge/taobaoPage2.JPG' -i '/Users/youngfreefjs/Desktop/code/github/imagecli/static/image_merge/taobaoPage3.JPG' -o '/Users/youngfreefjs/Desktop/code/github/imagecli/static/image_merge/merged.png'


>> Merged image saved to: /Users/youngfreefjs/Desktop/code/github/imagecli/static/image_merge/merged.png
```
| Original Images        | Page1 Images        | Page2 Images        | Page3 Image         |
|-----------------------|-----------------------|-----------------------|-----------------------|
| <img src="./static/image_merge/merged.png" alt="Merged Image" width="100"/> | <img src="./static/image_merge/taobaoPage1.JPG" alt="Original Photo" width="100"/> |<img src="./static/image_merge/taobaoPage2.JPG" alt="Original Photo" width="100"/> | <img src="./static/image_merge/taobaoPage3.JPG" alt="Original Photo" width="100"/> |



### 6. OCR (current version macOS only)
```bash
img ocr -f '/Users/youngfreefjs/Desktop/code/github/imagecli/static/image_merge/taobaoPage720P.JPG'

>> [
      {
          "content": "19:29",
          "leftTopX": 42.00000074999997,
          "leftTopY": 23.999999724999952,
          "width": 71.5,
          "height": 22.00000000000003,
          "tags": {
              "confidence": 0.5
          }
      },

      ...
  ]
```
| Image                                                   | OCR result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="./static/image_merge/taobaoPage720P.JPG" alt="Merged Image" width="100"/> | ```[{"content":"19:29","leftTopX":42.00000074999997,"leftTopY":23.999999724999952,"width":71.5,"height":22.00000000000003,"tags":{"confidence":0.5}},{"content":"关注","leftTopX":23.999999700000004,"leftTopY":140.00000010000008,"width":48,"height":24.000000000000057,"tags":{"confidence":1}},{"content":"包头鞋","leftTopX":98.00000044999999,"leftTopY":81.99999991250002,"width":72,"height":26.000000000000085,"tags":{"confidence":1}},{"content":"推荐","leftTopX":92.00000025454545,"leftTopY":137.99999990000015,"width":56,"height":30,"tags":{"confidence":1}},{"content":"我的淘宝","leftTopX":499.9375748301192,"leftTopY":1211.7545823228884,"width":62.1248512268066,"height":16.490835189819393,"tags":{"confidence":1}}]```
 |