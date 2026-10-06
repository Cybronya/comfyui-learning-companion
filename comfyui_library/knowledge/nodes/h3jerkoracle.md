# H3JerkOracle

## 节点类型

`H3JerkOracle`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `samples:LATENT`（4 次）
- `length:INT`（4 次）
- `q:FLOAT`（4 次）
- `d_max:INT`（4 次）
- `ramp:BOOLEAN`（4 次）
- `preset:COMBO`（4 次）
- `bridge:INT`（4 次）

## 输出

- `hold_map:STRING`（4 次）
- `segments:STRING`（4 次）
- `window_start:INT`（4 次）
- `window_len:INT`（4 次）
- `profile:STRING`（4 次）
- `report:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[124, 0.75, 4, true, "balanced (default)", 8]`（3 次）
- `[124, 0.75, 4, true, "economy (tight spans)", 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
