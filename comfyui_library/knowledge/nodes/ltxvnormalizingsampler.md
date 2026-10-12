# LTXVNormalizingSampler

## 节点类型

`LTXVNormalizingSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 12 个 workflow 中。

## 输入

- `noise:NOISE`（13 次）
- `guider:GUIDER`（13 次）
- `sampler:SAMPLER`（13 次）
- `sigmas:SIGMAS`（13 次）
- `latent_image:LATENT`（13 次）
- `video_normalization_factors:STRING`（13 次）
- `audio_normalization_factors:STRING`（13 次）

## 输出

- `denoised_output:LATENT`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1,1,1,1,1,1,1,1", "1,1,0.25,1,1,0.25,1,1"]`（13 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
