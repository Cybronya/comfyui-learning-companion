# SeedVCRun

## 节点类型

`SeedVCRun`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `source_audio:AUDIO`（6 次）
- `ref_audio:AUDIO`（6 次）
- `steps:INT`（1 次）
- `speed:FLOAT`（1 次）
- `inference_cfg_rate:FLOAT`（1 次）
- `f0_condition:BOOLEAN`（1 次）
- `auto_f0_adjust:BOOLEAN`（1 次）
- `pitch_shift:INT`（1 次）
- `unload_model:BOOLEAN`（1 次）

## 输出

- `audio:AUDIO`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[50, 1, 1, true, true, -1, false]`（3 次）
- `[30, 1, 1, true, true, -1, true]`（2 次）
- `[30, 1, 0.7, true, true, 0, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
