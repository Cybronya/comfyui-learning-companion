# TextEncodeMOSSImageEdit

## 节点类型

`TextEncodeMOSSImageEdit`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `clip:CLIP`（12 次）
- `images.image_0:IMAGE`（12 次）
- `images.image_1:IMAGE`（12 次）
- `vae:VAE`（12 次）
- `prompt:STRING`（12 次）
- `edit_format:COMBO`（12 次）
- `image_strength:FLOAT`（12 次）
- `images.image_2:IMAGE`（6 次）
- `images.image_3:IMAGE`（6 次）
- `images.image_4:IMAGE`（3 次）

## 输出

- `CONDITIONING:CONDITIONING`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["nsfw, worst quality, bad anatomy, watermark, jpeg artifact", "Moss-Image-Edit", 1]`（6 次）
- `["头发变成红色", "Moss-Image-Edit", 1]`（3 次）
- `["", "Moss-Image-Edit", 1]`（1 次）
- `["把图1角色绿色衣服改成红色", "Moss-Image-Edit", 1]`（1 次）
- `["仅将那件黑色连衣裙换成白色旗袍。其余部分——包括一位女性、她的面容、姿态、衣服上的花朵刺绣，以及背景——均保持不变。加上封面字体，顶部封面艺术大字配花朵装饰：MOSS EDIT，底部副标题艺术手写小字：ComfyUI LoRA", "M`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
