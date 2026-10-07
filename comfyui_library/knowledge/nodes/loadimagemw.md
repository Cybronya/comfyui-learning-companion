# LoadImageMW

## 节点类型

`LoadImageMW`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:COMBO`（4 次）
- `upload:IMAGEUPLOAD`（4 次）

## 输出

- `IMAGE:IMAGE`（4 次）
- `MASK:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["bef8700d2380334857de3d0644583df42e0070aeb877529ef09eb34b5a185cec.png", "image"]`（1 次）
- `["bbab3f1793da40065f98c5ccca8ee3adc1bfceccbb9b1dcb73deafef30a1ffe2.png", "image"]`（1 次）
- `["4914b82d6536848c37c4636bdde7937042c232e88241d98e7bbf46fc12f87de8.png", "image"]`（1 次）
- `["c80c2414bce2885b1c59c23f59b347846261fc3b22d917c34b90e08fc7e93f89.png", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
