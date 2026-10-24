# Mask_image2mask

## 节点类型

`Mask_image2mask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `mask_type:COMBO`（2 次）
- `WB_low_threshold:INT`（2 次）
- `WB_high_threshold:INT`（2 次）
- `color:STRING`（2 次）
- `color_threshold:INT`（2 次）
- `channel:COMBO`（2 次）
- `depth:FLOAT`（2 次）
- `blur_radius:INT`（2 次）
- `expand:INT`（2 次）

## 输出

- `mask:MASK`（2 次）
- `invert_mask:MASK`（2 次）
- `mask2_img:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["White_Balance", 1, 255, "#ff0000", 10, "red", 0.2, 1, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
