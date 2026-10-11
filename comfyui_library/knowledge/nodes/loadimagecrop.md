# LoadImageCrop

## 节点类型

`LoadImageCrop`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:COMBO`（6 次）
- `crop:STRING`（6 次）
- `max_megapixels:FLOAT`（6 次）
- `upload:IMAGEUPLOAD`（6 次）

## 输出

- `image:IMAGE`（6 次）
- `mask:MASK`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["undefined", "", 1, "image"]`（3 次）
- `["06a6364b3688bb3ee7cb8cf1c37bc4bf07fe2018ef026d93d0aa34a9f5226c5f.png", "", 1, "image"]`（2 次）
- `["84f97c9edce45e1f7eafb6097152d7176dea0af5f69b8e2e7774464fe8d52ff2.jpg", "", 1, "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
