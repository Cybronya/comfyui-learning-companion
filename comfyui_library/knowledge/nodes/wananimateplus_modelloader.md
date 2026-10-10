# WanAnimatePlus ModelLoader

## 节点类型

`WanAnimatePlus ModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `compile_args:WANCOMPILEARGS`（5 次）
- `block_swap_args:BLOCKSWAPARGS`（5 次）
- `lora:WANVIDLORA`（5 次）
- `vram_management_args:VRAM_MANAGEMENTARGS`（5 次）
- `extra_model:VACEPATH`（5 次）
- `fantasytalking_model:FANTASYTALKINGMODEL`（5 次）
- `multitalk_model:MULTITALKMODEL`（5 次）
- `fantasyportrait_model:FANTASYPORTRAITMODEL`（5 次）
- `model:COMBO`（5 次）
- `base_precision:COMBO`（5 次）

## 输出

- `model:WANVIDEOMODEL`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["wan2.1_14B_SCAIL_2_fp8_scaled.safetensors", "fp16", "disabled", "offload_device", "sageattn", "default", null]`（1 次）
- `["Wan22_Bernini_HIGH_fp16.safetensors", "bf16", "fp8_e4m3fn", "offload_device", "sageattn", "default", null]`（1 次）
- `["Wan22_Bernini_LOW_fp16.safetensors", "bf16", "fp8_e4m3fn", "offload_device", "sageattn", "default", null]`（1 次）
- `["Wan22_Bernini_HIGH_fp16.safetensors", "bf16", "fp8_e4m3fn", "offload_device", "sageattn", "default"]`（1 次）
- `["Wan22_Bernini_LOW_fp16.safetensors", "bf16", "fp8_e4m3fn", "offload_device", "sageattn", "default"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
