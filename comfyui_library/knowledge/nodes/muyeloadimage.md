# MuyeLoadImage

## 节点类型

`MuyeLoadImage`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:COMBO`（2 次）
- `upload:IMAGEUPLOAD`（2 次）

## 输出

- `图像:IMAGE`（2 次）
- `遮罩:MASK`（2 次）
- `文件名称:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["d39d57a4cb8ea7873a0f95157c00067a20f0869df9b3e1ecb35036b675397224.png", "image"]`（1 次）
- `["pasted/d6fa89afb7e90be844797f5ede0d0d696022020c91bee1cb7b4d4748eaa7761a.png", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
