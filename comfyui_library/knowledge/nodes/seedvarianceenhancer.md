# SeedVarianceEnhancer

## 节点类型

`SeedVarianceEnhancer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（1 次）
- `randomize_percent:FLOAT`（1 次）
- `strength:FLOAT`（1 次）
- `noise_insert:COMBO`（1 次）
- `steps_switchover_percent:FLOAT`（1 次）
- `seed:INT`（1 次）
- `mask_starts_at:COMBO`（1 次）
- `mask_percent:FLOAT`（1 次）
- `log_to_console:BOOLEAN`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20, 20, "noise on beginning steps", 20, 1113511765134387, "randomize", "beginning", 0, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
