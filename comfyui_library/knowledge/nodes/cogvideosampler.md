# CogVideoSampler

## 节点类型

`CogVideoSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:COGVIDEOMODEL`（4 次）
- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `samples:LATENT`（4 次）
- `image_cond_latents:LATENT`（4 次）
- `context_options:COGCONTEXT`（4 次）
- `controlnet:COGVIDECONTROLNET`（4 次）
- `tora_trajectory:TORAFEATURES`（4 次）
- `fastercache:FASTERCACHEARGS`（4 次）
- `feta_args:FETAARGS`（4 次）

## 输出

- `samples:LATENT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[49, 25, 6, 0, "fixed", "CogVideoXDDIM", 0.8]`（2 次）
- `[55, 25, 6, 123, "fixed", "DPM++", 1]`（1 次）
- `[49, 20, 5.000000000000001, 0, "fixed", "DPM++", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
