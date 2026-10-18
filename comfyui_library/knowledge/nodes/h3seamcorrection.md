# H3SeamCorrection

## 节点类型

`H3SeamCorrection`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `fix_color_preset:COMBO`（1 次）
- `fix_motion_preset:COMBO`（1 次）
- `fix_flash:BOOLEAN`（1 次）
- `flash_threshold:FLOAT`（1 次）
- `cut_threshold:FLOAT`（1 次）
- `blend_frames:INT`（1 次）
- `use_gpu:BOOLEAN`（1 次）

## 输出

- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["medium", "low", false, 0.3, 15, 2, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
