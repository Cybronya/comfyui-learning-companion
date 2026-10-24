# ttN pipeKSampler

## 节点类型

`ttN pipeKSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `pipe:PIPE_LINE`（2 次）
- `optional_model:MODEL`（2 次）
- `optional_positive:CONDITIONING`（2 次）
- `optional_negative:CONDITIONING`（2 次）
- `optional_latent:LATENT`（2 次）
- `optional_vae:VAE`（2 次）
- `optional_clip:CLIP`（2 次）
- `xyPlot:XYPLOT`（2 次）
- `lora_name:COMBO`（2 次）
- `lora_model_strength:FLOAT`（2 次）

## 输出

- `pipe:PIPE_LINE`（2 次）
- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）
- `vae:VAE`（2 次）
- `clip:CLIP`（2 次）
- `image:IMAGE`（2 次）
- `seed:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["None", 1, 1, "None", 1, "disabled", "Sample", 20, 4, "dpmpp_3m_sde_gpu", "karras", 0.4000000000000001, "Hide", "ComfyU`（1 次）
- `["None", 1, 1, "None", 1, "disabled", "Sample", 20, 4, "dpmpp_3m_sde_gpu", "karras", 0.4000000000000001, "Hide", "ComfyU`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
