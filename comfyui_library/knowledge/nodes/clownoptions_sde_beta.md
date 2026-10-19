# ClownOptions_SDE_Beta

## 节点类型

`ClownOptions_SDE_Beta`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `etas:SIGMAS`（2 次）
- `etas_substep:SIGMAS`（2 次）
- `options:OPTIONS`（2 次）
- `noise_type_sde:COMBO`（2 次）
- `noise_type_sde_substep:COMBO`（2 次）
- `noise_mode_sde:COMBO`（2 次）
- `noise_mode_sde_substep:COMBO`（2 次）
- `eta:FLOAT`（2 次）
- `eta_substep:FLOAT`（2 次）
- `seed:INT`（2 次）

## 输出

- `options:OPTIONS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["brownian", "pink", "lorentzian", "hard", 0.8, 0.75, 503216301884577, "fixed"]`（1 次）
- `["white", "pink", "hard", "exp", 0.5, 0.5, 594905209065308, "fixed"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
