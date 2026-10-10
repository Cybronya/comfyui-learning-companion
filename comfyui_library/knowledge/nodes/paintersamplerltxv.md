# PainterSamplerLTXV

## 节点类型

`PainterSamplerLTXV`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:MODEL`（5 次）
- `positive:CONDITIONING`（5 次）
- `negative:CONDITIONING`（5 次）
- `latent_image:LATENT`（5 次）
- `sigmas:SIGMAS`（5 次）
- `add_noise:COMBO`（5 次）
- `noise_seed:INT`（5 次）
- `steps:INT`（5 次）
- `cfg:FLOAT`（5 次）
- `sampler_name:COMBO`（5 次）

## 输出

- `latent:LATENT`（5 次）
- `video_latent:LATENT`（5 次）
- `audio_latent:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["enable", 136258299600624, "randomize", 8, 1, "euler", "simple", 0, 10000, "disable"]`（1 次）
- `["enable", 993381929174265, "randomize", 8, 1, "euler", "simple", 0, 10000, "disable"]`（1 次）
- `["enable", 893185183670771, "randomize", 8, 1, "euler", "simple", 0, 10000, "disable"]`（1 次）
- `["enable", 558607353850160, "randomize", 8, 1, "euler", "simple", 0, 10000, "disable"]`（1 次）
- `["enable", 186991909688540, "randomize", 8, 1, "euler", "simple", 0, 10000, "disable"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
