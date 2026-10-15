# ttN pipeKSampler_v2

## 节点类型

`ttN pipeKSampler_v2`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipe:PIPE_LINE`（1 次）
- `optional_model:MODEL`（1 次）
- `optional_positive:CONDITIONING`（1 次）
- `optional_negative:CONDITIONING`（1 次）
- `optional_latent:LATENT`（1 次）
- `optional_vae:VAE`（1 次）
- `optional_clip:CLIP`（1 次）
- `input_image_override:IMAGE`（1 次）
- `adv_xyPlot:ADV_XYPLOT`（1 次）
- `seed:INT`（1 次）

## 输出

- `pipe:PIPE_LINE`（1 次）
- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `vae:VAE`（1 次）
- `clip:CLIP`（1 次）
- `images:IMAGE`（1 次）
- `seed:INT`（1 次）
- `plot_image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["None", 1, "None", "4x_NMKD-Superscale-SP_178000_G.pth", 2, "by percentage", 50, 1024, 1024, 1024, "disabled", 20, 8, "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
