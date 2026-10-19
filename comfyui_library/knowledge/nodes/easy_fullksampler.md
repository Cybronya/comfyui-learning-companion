# easy fullkSampler

## 节点类型

`easy fullkSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipe:PIPE_LINE`（1 次）
- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `vae:VAE`（1 次）
- `clip:CLIP`（1 次）
- `xyPlot:XYPLOT`（1 次）
- `image:IMAGE`（1 次）
- `steps:INT`（1 次）

## 输出

- `pipe:PIPE_LINE`（1 次）
- `image:IMAGE`（1 次）
- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `vae:VAE`（1 次）
- `clip:CLIP`（1 次）
- `seed:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[25, 8, "dpmpp_2m_sde", "karras", 1, "Save", 0, "ComfyUI", 109007946043773, "randomize", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
