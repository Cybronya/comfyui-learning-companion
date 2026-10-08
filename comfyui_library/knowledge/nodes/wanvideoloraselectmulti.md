# WanVideoLoraSelectMulti

## 节点类型

`WanVideoLoraSelectMulti`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prev_lora:WANVIDLORA`（2 次）
- `blocks:SELECTEDBLOCKS`（2 次）
- `lora_0:COMBO`（2 次）
- `strength_0:FLOAT`（2 次）
- `lora_1:COMBO`（2 次）
- `strength_1:FLOAT`（2 次）
- `lora_2:COMBO`（2 次）
- `strength_2:FLOAT`（2 次）
- `lora_3:COMBO`（2 次）
- `strength_3:FLOAT`（2 次）

## 输出

- `lora:WANVIDLORA`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Wan21_I2V_14B_lightx2v_cfg_step_distill_lora_rank64_official.safetensors", 1, "Wan2.2-Fun-A14B-InP-high-noise-MPS.safe`（1 次）
- `["Wan21_I2V_14B_lightx2v_cfg_step_distill_lora_rank64_official.safetensors", 1.5, "Wan2.2-Fun-A14B-InP-low-noise-MPS.saf`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
