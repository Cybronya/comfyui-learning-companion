# MuyeImageBlendingMode

## 节点类型

`MuyeImageBlendingMode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `前景图像:IMAGE`（3 次）
- `背景图像:IMAGE`（3 次）
- `混合模式:COMBO`（3 次）
- `系数:FLOAT`（3 次）
- `数量差异补齐:COMBO`（3 次）
- `色彩空间:COMBO`（3 次）
- `输出格式:COMBO`（3 次）

## 输出

- `混合图像:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["色相", 0.7500000000000001, "无", "Lab", "RGB"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
