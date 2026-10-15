# WujiImageLoader

## 节点类型

`WujiImageLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:COMBO`（1 次）
- `BEN2抠图:BOOLEAN`（1 次）
- `百万像素开关:BOOLEAN`（1 次）
- `百万像素:FLOAT`（1 次）
- `upload:IMAGEUPLOAD`（1 次）
- `背景:COMBO`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `反向遮罩:MASK`（1 次）
- `反向图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["4592db3c5e189a16ba1af515b1497066ae68f3754d6480aa51fecfc33c8f632a.jpg", false, true, 1, "image", "透明"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
