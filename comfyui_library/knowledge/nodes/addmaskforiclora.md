# AddMaskForICLora

## 节点类型

`AddMaskForICLora`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `first_image:IMAGE`（4 次）
- `first_mask:MASK`（4 次）
- `second_image:IMAGE`（4 次）
- `second_mask:MASK`（4 次）
- `patch_mode:COMBO`（2 次）
- `output_length:INT`（2 次）
- `patch_color:COMBO`（2 次）

## 输出

- `IMAGE:IMAGE`（4 次）
- `MASK:MASK`（4 次）
- `x_offset:INT`（4 次）
- `y_offset:INT`（4 次）
- `target_width:INT`（4 次）
- `target_height:INT`（4 次）
- `total_width:INT`（4 次）
- `total_height:INT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["patch_bottom", 2048, "#FF0000"]`（1 次）
- `["patch_right", 1024, "#FF0000"]`（1 次）
- `["patch_right", 1536, "#FF0000"]`（1 次）
- `["auto", 1536, "#FF0000"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
