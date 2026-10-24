# easy preSampling

## 节点类型

`easy preSampling`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `pipe:PIPE_LINE`（6 次）
- `image_to_latent:IMAGE`（6 次）
- `latent:LATENT`（6 次）
- `steps:INT`（2 次）
- `cfg:FLOAT`（2 次）
- `sampler_name:COMBO`（2 次）
- `scheduler:COMBO`（2 次）
- `denoise:FLOAT`（2 次）
- `seed:INT`（2 次）

## 输出

- `pipe:PIPE_LINE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[25, 7.5, "ddpm", "sgm_uniform", 1, 759578274101406, "fixed"]`（1 次）
- `[20, 5, "dpmpp_3m_sde", "karras", 1, 296864414041636, "fixed"]`（1 次）
- `[20, 8, "dpmpp_2m", "karras", 1, 739208055117764, "fixed"]`（1 次）
- `[30, 6.8, "dpmpp_2m_sde", "karras", 1, 422529055879874, "randomize"]`（1 次）
- `[14, 5.5, "dpmpp_2m_sde_gpu", "align_your_steps", 1, 1051325639706525, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
