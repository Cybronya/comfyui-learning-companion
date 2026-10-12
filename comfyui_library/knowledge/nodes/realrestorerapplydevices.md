# RealRestorerApplyDevices

## 节点类型

`RealRestorerApplyDevices`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:ANY`（1 次）
- `use_manual_placement:BOOLEAN`（1 次）
- `device_strategy:COMBO`（1 次）
- `text_encoder_device:COMBO`（1 次）
- `transformer_device:COMBO`（1 次）
- `vae_device:COMBO`（1 次）

## 输出

- `pipeline:ANY`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "model_cpu_offload", "cuda", "cuda", "cuda"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
