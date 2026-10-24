# ScaledSoftControlNetWeights

## 节点类型

`ScaledSoftControlNetWeights`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `cn_extras:CN_WEIGHTS_EXTRAS`（8 次）
- `base_multiplier:FLOAT`（4 次）
- `flip_weights:BOOLEAN`（4 次）
- `uncond_multiplier:FLOAT`（4 次）

## 输出

- `CN_WEIGHTS:CONTROL_NET_WEIGHTS`（8 次）
- `TK_SHORTCUT:TIMESTEP_KEYFRAME`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.825, false, 1]`（5 次）
- `[0.85, false, 1]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
