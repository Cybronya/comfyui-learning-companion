# WanAnimatePlus Samplerv2

## 节点类型

`WanAnimatePlus Samplerv2`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:WANVIDEOMODEL`（4 次）
- `image_embeds:WANVIDIMAGE_EMBEDS`（4 次）
- `scheduler:WANVIDEOSCHEDULER`（4 次）
- `text_embeds:WANVIDEOTEXTEMBEDS`（4 次）
- `samples:LATENT`（4 次）
- `extra_args:WANVIDSAMPLEREXTRAARGS`（4 次）
- `cfg:FLOAT`（4 次）
- `seed:INT`（4 次）
- `force_offload:BOOLEAN`（4 次）
- `add_noise_to_samples:BOOLEAN`（4 次）

## 输出

- `samples:LATENT`（4 次）
- `denoised_samples:LATENT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 666, "fixed", true, true, "cfg", 0.5, 0, 50, 4, 4.5, 4, 1.25, 4.5, 4]`（2 次）
- `[1, 666, "fixed", true, false, "cfg", 0.5, 0, 50, 4, 4.5, 4, 1.25, 4.5, 4]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
