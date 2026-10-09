# WanVideoSamplerv2

## 节点类型

`WanVideoSamplerv2`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:WANVIDEOMODEL`（5 次）
- `image_embeds:WANVIDIMAGE_EMBEDS`（5 次）
- `scheduler:WANVIDEOSCHEDULER`（5 次）
- `text_embeds:WANVIDEOTEXTEMBEDS`（5 次）
- `samples:LATENT`（5 次）
- `extra_args:WANVIDSAMPLEREXTRAARGS`（5 次）
- `cfg:FLOAT`（5 次）
- `seed:INT`（5 次）
- `force_offload:BOOLEAN`（5 次）
- `add_noise_to_samples:BOOLEAN`（5 次）

## 输出

- `samples:LATENT`（5 次）
- `denoised_samples:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 3, "fixed", true, false]`（1 次）
- `[1, 1, "fixed", true, false]`（1 次）
- `[1, 4, "fixed", true, false]`（1 次）
- `[1, 5, "fixed", true, false]`（1 次）
- `[1, 2, "fixed", true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
