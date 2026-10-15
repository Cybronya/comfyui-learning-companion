# RIFE_VFI_Opt

## 节点类型

`RIFE_VFI_Opt`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `frames:IMAGE`（1 次）
- `optional_interpolation_states:INTERPOLATION_STATES`（1 次）
- `ckpt_name:COMBO`（1 次）
- `multiplier:INT`（1 次）
- `scale_factor:COMBO`（1 次）
- `ensemble:BOOLEAN`（1 次）
- `clear_cache_after_n_frames:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["rife49.pth", 2, 1, true, 24]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
