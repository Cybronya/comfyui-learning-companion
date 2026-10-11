# MiniMaxH3EasySegmentRefine

## 节点类型

`MiniMaxH3EasySegmentRefine`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `h3_context:MINIMAX_H3_CONTEXT`（2 次）
- `segments:MINIMAX_H3_SEGMENTS`（2 次）
- `model:MODEL`（2 次）
- `sampler:SAMPLER`（2 次）
- `sigmas:SIGMAS`（2 次）
- `refine_mode:COMBO`（2 次）
- `seed:INT`（2 次）
- `refine_execution:COMBO`（2 次）
- `target_width:INT`（2 次）
- `target_height:INT`（2 次）

## 输出

- `refined_segments:MINIMAX_H3_SEGMENTS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Latent Upscale", 2, "fixed", "Standard", 0, 0, "minimax_h3_latent_upscaler_3d_fp16.safetensors", 2, "cuda", "fp16", 51`（1 次）
- `["Pixel Resize", 113, "fixed", "Standard", 0, "minimax_h3_latent_upscaler_3d_fp16.safetensors", "minimax_h3_latent_upsca`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
