# Krea2StyleTransfer

## 节点类型

`Krea2StyleTransfer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `reference_latent:LATENT`（2 次）
- `ref_conditioning:CONDITIONING`（2 次）
- `mode:COMBO`（2 次）
- `style_strength:FLOAT`（2 次）
- `value_adain_strength:FLOAT`（2 次）
- `ref_value_mix:FLOAT`（2 次）
- `ref_k_strength:FLOAT`（2 次）
- `rf_mode:COMBO`（2 次）
- `gamma:FLOAT`（2 次）

## 输出

- `model:MODEL`（2 次）
- `rf_reference:LATENT`（2 次）
- `debug:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["custom", 1.0000000000000002, 0.65, 1, 1.06, "flowturbo_pc", 0.5, 2.5, 1.04, 0, 1, 1.1, 0.85, "7-27"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
