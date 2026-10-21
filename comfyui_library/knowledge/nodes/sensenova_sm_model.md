# SenseNova_SM_Model

## 节点类型

`SenseNova_SM_Model`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `diffusion_models:COMBO`（11 次）
- `gguf:COMBO`（11 次）
- `lora:COMBO`（11 次）
- `attn_backend:COMBO`（11 次）

## 输出

- `model:MODEL`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SenseNova-U1-8B-MoT-8step-merge_bf16.safetensors", "none", "none", "flash"]`（5 次）
- `["SenseNova-U1-8B-MoT-SFT-merge_bf16.safetensors", "none", "SenseNova-U1-8B-MoT-LoRA-8step-V1.0.safetensors", "auto"]`（2 次）
- `["SenseNova-U1-8B-MoT-8step-merge_bf16.safetensors", "none", "none", "auto"]`（2 次）
- `["none", "SenseNova-U1-8B-MoT-8step-Q8_0.gguf", "none", "flash"]`（1 次）
- `["none", "SenseNova-U1-8B-MoT-8step-Q8_0.gguf", "none", "auto"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
