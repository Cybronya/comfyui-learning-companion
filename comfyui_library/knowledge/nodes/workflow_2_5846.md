# workflow>图片处理2

## 节点类型

`workflow>图片处理2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `configs:LIST`（1 次）
- `mask:MASK`（1 次）
- `background_color:STRING`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `proportional_width:INT`（1 次）
- `proportional_height:INT`（1 次）
- `fit:COMBO`（1 次）
- `method:COMBO`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `原始大小:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `batch_size:INT`（1 次）
- `configs:LIST`（1 次）
- `config:ANY`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["#000000", "custom", 1, 1, "letterbox", "lanczos", "16", "longest", 1024, true, 384, "center", true, false, 1024, "pad"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
