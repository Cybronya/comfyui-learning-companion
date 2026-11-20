# WanAnimatePlus Easy SamplerSettings

## 节点类型

`WanAnimatePlus Easy SamplerSettings`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:WANVIDEOMODEL`（3 次）
- `image_embeds:WANVIDIMAGE_EMBEDS`（3 次）
- `text_embeds:WANVIDEOTEXTEMBEDS`（3 次）
- `samples:LATENT`（3 次）
- `context_options:WANVIDCONTEXT`（3 次）
- `uni3c_embeds:UNI3C_EMBEDS`（3 次）
- `steps:INT`（3 次）
- `cfg:FLOAT`（3 次）
- `shift:FLOAT`（3 次）
- `seed:INT`（3 次）

## 输出

- `sampler_inputs:SAMPLER_ARGS`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[6, 1.0000000000000002, 5, 0, "randomize", true, "dpm++_sde"]`（1 次）
- `[6, 1.0000000000000002, 5, 392399237461083, "randomize", true, "dpm++_sde"]`（1 次）
- `[6, 1, 5, 0, "randomize", true, "dpm++_sde"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
