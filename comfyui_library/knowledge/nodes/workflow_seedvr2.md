# workflow>SeedVR2

## 节点类型

`workflow>SeedVR2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `resized_images:IMAGE`（5 次）
- `original_resized_images:IMAGE`（5 次）
- `unet_name:COMBO`（5 次）
- `weight_dtype:COMBO`（5 次）
- `vae_name:COMBO`（5 次）
- `tile_size:INT`（5 次）
- `overlap:INT`（5 次）
- `temporal_size:INT`（5 次）
- `temporal_overlap:INT`（5 次）
- `seed:INT`（5 次）

## 输出

- `images:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["seedvr2_7b_int8_convrot.safetensors", "default", "seedvr2_ema_vae_fp16.safetensors", 512, 128, 4096, 8, 95994890215606`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
