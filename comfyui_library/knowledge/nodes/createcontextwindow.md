# CreateContextWindow

## 节点类型

`CreateContextWindow`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `input_image:IMAGE`（4 次）
- `input_mask:MASK`（4 次）
- `patch_mode:COMBO`（4 次）
- `patch_type:COMBO`（4 次）
- `output_length:INT`（4 次）
- `pixel_buffer:INT`（4 次）

## 输出

- `prepared_image:IMAGE`（4 次）
- `prepared_mask:MASK`（4 次）
- `patch_mode:STRING`（4 次）
- `x_offset_of_ori:INT`（4 次）
- `y_offset_of_ori:INT`（4 次）
- `scale:FLOAT`（4 次）
- `crop_area:IMAGE`（4 次）
- `crop_mask:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["patch_right", "1:1", 1536, 64]`（2 次）
- `["auto", "1:1", 1536, 64]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
