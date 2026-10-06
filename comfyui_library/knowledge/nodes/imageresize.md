# ImageResize+

## 节点类型

`ImageResize+`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 23 个 workflow 中。

## 输入

- `image:IMAGE`（63 次）
- `width:INT`（63 次）
- `height:INT`（63 次）
- `interpolation:COMBO`（63 次）
- `method:COMBO`（63 次）
- `condition:COMBO`（63 次）
- `multiple_of:INT`（63 次）

## 输出

- `IMAGE:IMAGE`（63 次）
- `width:INT`（63 次）
- `height:INT`（63 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, "lanczos", "stretch", "always", 8]`（42 次）
- `[1536, 1536, "bilinear", "keep proportion", "always", 16]`（10 次）
- `[512, 512, "lanczos", "keep proportion", "always", 8]`（2 次）
- `[512, 512, "lanczos", "fill / crop", "always", 32]`（2 次）
- `[["22", 0], ["22", 1], "lanczos", "stretch", "always", 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
