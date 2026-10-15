# BerniniLoraSelectMulti

## 节点类型

`BerniniLoraSelectMulti`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `prev_lora:WANVIDLORA`（12 次）
- `blocks:SELECTEDBLOCKS`（12 次）
- `lora_0:COMBO`（12 次）
- `strength_0:FLOAT`（12 次）
- `lora_1:COMBO`（12 次）
- `strength_1:FLOAT`（12 次）
- `lora_2:COMBO`（12 次）
- `strength_2:FLOAT`（12 次）
- `lora_3:COMBO`（12 次）
- `strength_3:FLOAT`（12 次）

## 输出

- `lora:WANVIDLORA`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["wan2.2_t2v_A14b_high_noise_lora_rank64_lightx2v_4step_1217.safetensors", 1, "none", 1, "none", 1, "none", 1, "none", 1`（4 次）
- `["wan2.2_t2v_A14b_low_noise_lora_rank64_lightx2v_4step_1217.safetensors", 1, "none", 1, "none", 1, "none", 1, "none", 1,`（4 次）
- `["Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V2.0-low_noise_model.safetensors", 1.0000000000000002, "none", 1, "none", 1, "`（1 次）
- `["Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V2.0-high_noise_model.safetensors", 2.0000000000000004, "none", 1, "none", 1, `（1 次）
- `["Bernini-R_LightX2V_high_noise.safetensors", 1, "none", 1, "none", 1, "none", 1, "none", 1, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
