# GuHaiAutoImageSplit

## 节点类型

`GuHaiAutoImageSplit`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `保存目录:STRING`（1 次）
- `水平张数:INT`（1 次）
- `垂直张数:INT`（1 次）
- `移除画布边缘:BOOLEAN`（1 次）
- `移除描边:INT`（1 次）
- `文件名前缀:STRING`（1 次）
- `保存格式:COMBO`（1 次）

## 输出

- `分割图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["output", 3, 3, true, 0, "孤海图像分割_", "PNG"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
