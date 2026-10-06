# WanVideoModelLoader

## 节点类型

`WanVideoModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `compile_args:WANCOMPILEARGS`（4 次）
- `block_swap_args:BLOCKSWAPARGS`（4 次）
- `lora:HYVIDLORA`（3 次）
- `lora:WANVIDLORA`（1 次）
- `vram_management_args:VRAM_MANAGEMENTARGS`（1 次）
- `extra_model:VACEPATH`（1 次）
- `fantasytalking_model:FANTASYTALKINGMODEL`（1 次）
- `multitalk_model:MULTITALKMODEL`（1 次）
- `fantasyportrait_model:FANTASYPORTRAITMODEL`（1 次）
- `model:COMBO`（1 次）

## 输出

- `model:WANVIDEOMODEL`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["wan2.1/Wan2_1-T2V-1_3B_fp8_e4m3fn.safetensors", "bf16", "fp8_e4m3fn", "offload_device", "sageattn"]`（1 次）
- `["wan2.1_i2v_720p_14B_bf16_Comfy-Org.safetensors", "bf16", "fp8_e4m3fn", "offload_device", "sageattn"]`（1 次）
- `["aniWan14BFp8E4m3fn_i2v480pNew.safetensors", "fp16_fast", "disabled", "offload_device", "sageattn", "default"]`（1 次）
- `["Wan2_1-I2V-14B-720P_fp8_e4m3fn.safetensors", "bf16", "fp8_e4m3fn", "offload_device", "sageattn"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
