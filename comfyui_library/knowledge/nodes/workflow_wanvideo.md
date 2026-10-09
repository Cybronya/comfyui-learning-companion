# workflow>WanVideo

## 节点类型

`workflow>WanVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `compile_args:WANCOMPILEARGS`（1 次）
- `block_swap_args:BLOCKSWAPARGS`（1 次）
- `lora:WANVIDLORA`（1 次）
- `vram_management_args:VRAM_MANAGEMENTARGS`（1 次）
- `extra_model:VACEPATH`（1 次）
- `fantasytalking_model:FANTASYTALKINGMODEL`（1 次）
- `multitalk_model:MULTITALKMODEL`（1 次）
- `fantasyportrait_model:FANTASYPORTRAITMODEL`（1 次）
- `prev_lora:WANVIDLORA`（1 次）
- `blocks:SELECTEDBLOCKS`（1 次）

## 输出

- `model:WANVIDEOMODEL`（1 次）
- `lora:WANVIDLORA`（1 次）
- `WanVideoSetBlockSwap model:WANVIDEOMODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["disabled", "offload_device", "sageattn", "default", "Wan22Animate/Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
