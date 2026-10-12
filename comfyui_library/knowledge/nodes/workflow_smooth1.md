# workflow>SMOOTH1

## 节点类型

`workflow>SMOOTH1`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `compile_args:WANCOMPILEARGS`（3 次）
- `WanVideoModelLoader compile_args:WANCOMPILEARGS`（3 次）
- `block_swap_args:BLOCKSWAPARGS`（3 次）
- `lora:WANVIDLORA`（3 次）
- `vram_management_args:VRAM_MANAGEMENTARGS`（3 次）
- `extra_model:VACEPATH`（3 次）
- `fantasytalking_model:FANTASYTALKINGMODEL`（3 次）
- `multitalk_model:MULTITALKMODEL`（3 次）
- `fantasyportrait_model:FANTASYPORTRAITMODEL`（3 次）
- `WanVideoModelLoader 2 compile_args:WANCOMPILEARGS`（3 次）

## 输出

- `upscale_factor:FLOAT`（3 次）
- `batch_size:INT`（3 次）
- `empty_latent:LATENT`（3 次）
- `show_help:STRING`（3 次）
- `FLOAT:FLOAT`（3 次）
- `output:*`（3 次）
- `mask:MASK`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `ImageResizeKJv2 mask:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["wan_2.1_vae.safetensors", "bf16", "umt5-xxl-enc-bf16.safetensors", "bf16", "offload_device", "disabled", "", 5, "fixed`（1 次）
- `["wan_2.1_vae.safetensors", "bf16", "umt5-xxl-enc-bf16.safetensors", "bf16", "offload_device", "disabled", "", 5, "fixed`（1 次）
- `["wan_2.1_vae.safetensors", "bf16", "umt5-xxl-enc-bf16.safetensors", "bf16", "offload_device", "disabled", "", 5, "fixed`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
