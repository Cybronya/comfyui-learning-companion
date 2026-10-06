# ImagePadForOutpaint

## 节点类型

`ImagePadForOutpaint`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `image:IMAGE`（12 次）
- `left:INT`（12 次）
- `top:INT`（12 次）
- `right:INT`（12 次）
- `bottom:INT`（12 次）
- `feathering:INT`（12 次）

## 输出

- `IMAGE:IMAGE`（12 次）
- `MASK:MASK`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[400, 400, 400, 200, 40]`（6 次）
- `[304, 0, 304, 104, 0]`（2 次）
- `[200, 200, 200, 200, 40]`（2 次）
- `[304, 0, 304, 0, 75]`（1 次）
- `[200, 0, 200, 512, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
