# SeedVR2TilingUpscaler

## 节点类型

`SeedVR2TilingUpscaler`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `block_swap_config:block_swap_config`（2 次）
- `extra_args:extra_args`（2 次）
- `model:COMBO`（2 次）
- `seed:INT`（2 次）
- `new_resolution:INT`（2 次）
- `tile_width:INT`（2 次）
- `tile_height:INT`（2 次）
- `mask_blur:INT`（2 次）
- `tile_padding:INT`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["seedvr2_ema_7b_sharp_fp8_e4m3fn_mixed_block35_fp16.safetensors", 2817440240, "randomize", 2048, 512, 512, 0, 32, 1024,`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
