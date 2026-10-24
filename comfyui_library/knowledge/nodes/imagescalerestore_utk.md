# ImageScaleRestore_UTK

## 节点类型

`ImageScaleRestore_UTK`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 25 个 workflow 中。

## 输入

- `image:IMAGE`（27 次）
- `mask:MASK`（27 次）
- `original_size:BOX`（27 次）
- `scale:FLOAT`（27 次）
- `method:COMBO`（27 次）
- `scale_to_side:COMBO`（27 次）
- `scale_to_length:INT`（27 次）
- `round_to_multiple:COMBO`（27 次）

## 输出

- `image:IMAGE`（27 次）
- `mask:MASK`（27 次）
- `original_size:BOX`（27 次）
- `width:INT`（27 次）
- `height:INT`（27 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.30000000000000004, "lanczos", "longest", 768, "8"]`（23 次）
- `[1, "lanczos", "None", 1024, "8"]`（2 次）
- `[0.5, "lanczos", "longest", 768, "8"]`（1 次）
- `[1, "lanczos", "None", 1024, "None"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
