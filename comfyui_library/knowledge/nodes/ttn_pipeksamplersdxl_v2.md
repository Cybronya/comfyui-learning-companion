# ttN pipeKSamplerSDXL_v2

## 节点类型

`ttN pipeKSamplerSDXL_v2`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `sdxl_pipe:PIPE_LINE_SDXL`（4 次）
- `optional_model:MODEL`（4 次）
- `optional_positive:CONDITIONING`（4 次）
- `optional_negative:CONDITIONING`（4 次）
- `optional_latent:LATENT`（4 次）
- `optional_vae:VAE`（4 次）
- `optional_refiner_model:MODEL`（4 次）
- `optional_refiner_positive:CONDITIONING`（4 次）
- `optional_refiner_negative:CONDITIONING`（4 次）
- `optional_clip:CLIP`（4 次）

## 输出

- `sdxl_pipe:PIPE_LINE_SDXL`（4 次）
- `pipe:PIPE_LINE`（4 次）
- `model:MODEL`（4 次）
- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `refiner_model:MODEL`（4 次）
- `refiner_positive:CONDITIONING`（4 次）
- `refiner_negative:CONDITIONING`（4 次）
- `latent:LATENT`（4 次）
- `vae:VAE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["None", 1, "None", "1x-ReFocus-V3.pth", 2, "by percentage", 50, 1024, 1024, 1024, "disabled", 30, 8, 0.4500000000000000`（1 次）
- `["None", 0.7000000000000002, "None", "1x-ReFocus-V3.pth", 2, "by percentage", 50, 1024, 1024, 1024, "disabled", 20, 2, 1`（1 次）
- `["None", 1, "None", "1x-ReFocus-V3.pth", 2, "by percentage", 50, 1024, 1024, 1024, "disabled", 20, 6, 1, 30, 8, 1, "eule`（1 次）
- `["None", 1, "None", "1x-ReFocus-V3.pth", 2, "by percentage", 50, 1024, 1024, 1024, "disabled", 30, 8, 1, 20, 8, 1, "eule`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
