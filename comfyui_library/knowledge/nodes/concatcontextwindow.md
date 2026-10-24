# ConcatContextWindow

## 节点类型

`ConcatContextWindow`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `first_image:IMAGE`（2 次）
- `second_image:IMAGE`（2 次）
- `second_mask:MASK`（2 次）
- `patch_mode:COMBO`（2 次）
- `patch_type:COMBO`（2 次）
- `output_length:INT`（2 次）
- `patch_color:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）
- `target_width:INT`（2 次）
- `target_height:INT`（2 次）
- `x_offset:INT`（2 次）
- `y_offset:INT`（2 次）
- `total_width:INT`（2 次）
- `total_height:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", "1:1", "#FF0000", "#FF0000"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
