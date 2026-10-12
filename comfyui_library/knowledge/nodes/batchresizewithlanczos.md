# BatchResizeWithLanczos

## 节点类型

`BatchResizeWithLanczos`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `width:INT`（4 次）
- `height:INT`（4 次）
- `resize_mode:COMBO`（4 次）
- `divisible_by:INT`（4 次）
- `max_batch_size:INT`（4 次）
- `sinc_window:INT`（4 次）
- `pad_color:STRING`（4 次）
- `crop_position:COMBO`（4 次）

## 输出

- `IMAGE:IMAGE`（4 次）
- `width:INT`（4 次）
- `height:INT`（4 次）
- `mask:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, "AR Scale + Divisible Crop", 32, 25, 3, "0, 0, 0", "center", "fp32"]`（2 次）
- `[1280, 1280, "Keep AR", 16, 3, 3, "0, 0, 0", "center", "fp32"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
