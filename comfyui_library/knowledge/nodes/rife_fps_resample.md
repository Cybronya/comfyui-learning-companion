# RIFE_FPS_Resample

## 节点类型

`RIFE_FPS_Resample`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `frames:IMAGE`（2 次）
- `ckpt_name:COMBO`（2 次）
- `fps_in:FLOAT`（2 次）
- `fps_out:FLOAT`（2 次）
- `scale_factor:COMBO`（2 次）
- `ensemble:BOOLEAN`（2 次）
- `linearize:BOOLEAN`（2 次）
- `lf_guardrail:BOOLEAN`（2 次）
- `lf_sigma:FLOAT`（2 次）
- `source_pair_match:BOOLEAN`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["rife47.pth", 24, 60, 1, true, true, true, 13.5, true, 0.02, 0.00784313725490196, true, 0.0058823529411764705, 0.023529`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
