# BerniniSampler

## 节点类型

`BerniniSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:WANVIDEOMODEL`（2 次）
- `image_embeds:WANVIDIMAGE_EMBEDS`（2 次）
- `scheduler:WANVIDEOSCHEDULER`（2 次）
- `text_embeds:WANVIDEOTEXTEMBEDS`（2 次）
- `samples:LATENT`（2 次）
- `extra_args:WANVIDSAMPLEREXTRAARGS`（2 次）
- `cfg:FLOAT`（2 次）
- `seed:INT`（2 次）
- `force_offload:BOOLEAN`（2 次）
- `add_noise_to_samples:BOOLEAN`（2 次）

## 输出

- `samples:LATENT`（2 次）
- `denoised_samples:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 666, "fixed", true, true]`（1 次）
- `[1, 666, "fixed", true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
