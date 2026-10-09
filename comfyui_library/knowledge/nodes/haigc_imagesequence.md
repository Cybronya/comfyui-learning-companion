# HAIGC_ImageSequence

## 节点类型

`HAIGC_ImageSequence`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（3 次）
- `上一层:HAIGC_IMAGE_STACK`（3 次）
- `图层名:STRING`（3 次）

## 输出

- `图像序列:IMAGE`（3 次）
- `图层连接:HAIGC_IMAGE_STACK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["前景手和挂绳"]`（2 次）
- `["完整风扇"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
