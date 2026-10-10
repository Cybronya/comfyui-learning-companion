# MMH3UltimateUpscale

## 节点类型

`MMH3UltimateUpscale`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `noise:NOISE`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent_upscale_param:H3_UPSCALE_PARAM`（1 次）
- `temporal_split_param:H3_TEMPORAL_PARAM`（1 次）
- `spatial_split_param:H3_SPATIAL_PARAM`（1 次）

## 输出

- `latent:LATENT`（1 次）
- `segments_info:DICT`（1 次）
- `tiles_info:DICT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
