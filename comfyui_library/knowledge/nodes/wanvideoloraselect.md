# WanVideoLoraSelect

## 节点类型

`WanVideoLoraSelect`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prev_lora:WANVIDLORA`（2 次）
- `blocks:SELECTEDBLOCKS`（2 次）
- `lora:COMBO`（2 次）
- `strength:FLOAT`（2 次）
- `low_mem_load:BOOLEAN`（2 次）
- `merge_loras:BOOLEAN`（2 次）

## 输出

- `lora:WANVIDLORA`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Wan21_I2V_14B_lightx2v_cfg_step_distill_lora_rank64.safetensors", 1.0000000000000002, false, false]`（1 次）
- `["Wan_2_1_T2V_14B_rCM_lora_average_rank_83_bf16.safetensors", 0.5000000000000001, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
