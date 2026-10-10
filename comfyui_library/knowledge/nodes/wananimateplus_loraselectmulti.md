# WanAnimatePlus LoraSelectMulti

## 节点类型

`WanAnimatePlus LoraSelectMulti`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `prev_lora:WANVIDLORA`（3 次）
- `blocks:SELECTEDBLOCKS`（3 次）
- `lora_0:COMBO`（3 次）
- `strength_0:FLOAT`（3 次）
- `lora_1:COMBO`（3 次）
- `strength_1:FLOAT`（3 次）
- `lora_2:COMBO`（3 次）
- `strength_2:FLOAT`（3 次）
- `lora_3:COMBO`（3 次）
- `strength_3:FLOAT`（3 次）

## 输出

- `lora:WANVIDLORA`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank256_bf16.safetensors", 1, "none", 1, "none", 1, "none", 1, "none", 1, fa`（2 次）
- `["none", 0, "lightx2v_I2V_14B_480p_cfg_step_distill_rank256_bf16.safetensors", 1, "wan2.1_SCAIL_2_DPO_lora_bf16.safetens`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
