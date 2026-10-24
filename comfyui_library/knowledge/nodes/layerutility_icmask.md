# LayerUtility: ICMask

## 节点类型

`LayerUtility: ICMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 11 个 workflow 中。

## 输入

- `first_image:IMAGE`（12 次）
- `first_mask:MASK`（12 次）
- `second_image:IMAGE`（12 次）
- `second_mask:MASK`（12 次）
- `patch_mode:COMBO`（4 次）
- `output_length:INT`（4 次）
- `patch_color:COMBO`（4 次）

## 输出

- `image:IMAGE`（12 次）
- `mask:MASK`（12 次）
- `icmask_data:ICMASK_DATA`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", 2048, "#FF0000"]`（6 次）
- `["auto", 1920, "#FF0000"]`（3 次）
- `["patch_right", 1588, "#FFFFFF"]`（2 次）
- `["patch_right", 1440, "#FFFFFF"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
