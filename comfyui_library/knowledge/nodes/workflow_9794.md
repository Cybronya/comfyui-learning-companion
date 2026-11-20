# workflow>遮罩转颜色

## 节点类型

`workflow>遮罩转颜色`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `遮罩:MASK`（5 次）
- `参考大小:*`（4 次）
- `目标图像:IMAGE`（4 次）
- `color:LYCOLOR`（4 次）
- `mode:COMBO`（4 次）
- `size:COMBO`（4 次）
- `custom_width:INT`（4 次）
- `custom_height:INT`（4 次）
- `x:INT`（4 次）
- `y:INT`（4 次）

## 输出

- `图像:IMAGE`（5 次）
- `原始大小:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `ImageCompositeMasked 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["#FFFFFF", "HEX", "custom", 512, 512, 0, 0, false]`（4 次）
- `["original", 1, 1, "letterbox", "lanczos", "8", "None", 1024, "#000000", "custom", 512, 512, 0, 0, false, "#000000"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
