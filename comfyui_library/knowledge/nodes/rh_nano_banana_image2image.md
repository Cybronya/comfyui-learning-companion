# RH_Nano_Banana_Image2Image

## 节点类型

`RH_Nano_Banana_Image2Image`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `images:IMAGE`（3 次）
- `image1:IMAGE`（3 次）
- `image2:IMAGE`（3 次）
- `image3:IMAGE`（3 次）
- `image4:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `seed:INT`（3 次）
- `aspectRatio:COMBO`（3 次）
- `skip_error:BOOLEAN`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `image_url:STRING`（3 次）
- `response:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 1845643146, "randomize", "auto", false]`（1 次）
- `["", 1677794661, "randomize", "auto", false]`（1 次）
- `["", 251829885, "randomize", "auto", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
