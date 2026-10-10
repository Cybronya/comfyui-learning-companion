# GPENO Face Restoration

## 节点类型

`GPENO Face Restoration`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `use_global_cache:BOOLEAN`（1 次）
- `unload:BOOLEAN`（1 次）
- `backbone:COMBO`（1 次）
- `resolution_preset:COMBO`（1 次）
- `downscale_method:COMBO`（1 次）
- `channel_multiplier:FLOAT`（1 次）
- `narrow:FLOAT`（1 次）
- `alpha:FLOAT`（1 次）
- `device:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, false, "RetinaFace-R50", "512", "Bilinear", 2, 1, 1, "cuda", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
