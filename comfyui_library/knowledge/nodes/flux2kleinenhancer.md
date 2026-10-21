# Flux2KleinEnhancer

## 节点类型

`Flux2KleinEnhancer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（4 次）
- `active_scale:FLOAT`（4 次）
- `per_token_whiten:FLOAT`（4 次）
- `norm_equalize:FLOAT`（4 次）
- `early_layer_scale:FLOAT`（4 次）
- `mid_layer_scale:FLOAT`（4 次）
- `late_layer_scale:FLOAT`（4 次）
- `preserve_original:FLOAT`（4 次）
- `active_end_override:INT`（4 次）
- `device:COMBO`（4 次）

## 输出

- `CONDITIONING:CONDITIONING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 0, 0, 1, 1, 1, 0, 0, "auto", false]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
