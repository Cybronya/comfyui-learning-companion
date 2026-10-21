# Krea2TwoStyleTransfer

## 节点类型

`Krea2TwoStyleTransfer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:MODEL`（6 次）
- `style_refs:STYLE_REFS`（6 次）
- `ref_conditioning:CONDITIONING`（6 次）
- `mode:COMBO`（6 次）
- `primary_reference:COMBO`（6 次）
- `style_strength:FLOAT`（6 次）
- `ref_k_1:FLOAT`（6 次）
- `ref_k_2:FLOAT`（6 次）
- `stage_focus:FLOAT`（6 次）
- `ref_value_mix:FLOAT`（6 次）

## 输出

- `model:MODEL`（6 次）
- `debug:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["recommended", "1", 1, 1.08, 1.08, 0.85, 1, 1.1, "flowturbo_pc", 0.5, 2.5, 1.04, 0, 1, 0.85, "7-27"]`（2 次）
- `["recommended", 1, "1", 1.08, 1.08, "forward", 0, 0.85, 0, 0.65, 1, 1.1, 0, 0, 0, "flowturbo_pc"]`（1 次）
- `["custom", "1", 1, 1.08, 1.08, 0.85, 1, 1.1, "flowturbo_pc", 0.5, 2.5, 1.04, 0, 1, 0.85, "7-27"]`（1 次）
- `["recommended", "2", 1, 1.08, 1.08, 0.85, 1, 1.1, "flowturbo_pc", 0.5, 2.5, 1.04, 0, 1, 0.85, "7-27"]`（1 次）
- `["custom", "2", 1, 1.08, 1.08, 0.85, 1, 1.1, "flowturbo_pc", 0.5, 2.5, 1.04, 0, 1, 0.85, "7-27"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
