# WanAnimatePlus Sampler

## 节点类型

`WanAnimatePlus Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:WANVIDEOMODEL`（1 次）
- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）
- `text_embeds:WANVIDEOTEXTEMBEDS`（1 次）
- `samples:LATENT`（1 次）
- `feta_args:FETAARGS`（1 次）
- `context_options:WANVIDCONTEXT`（1 次）
- `cache_args:CACHEARGS`（1 次）
- `flowedit_args:FLOWEDITARGS`（1 次）
- `slg_args:SLGARGS`（1 次）
- `loop_args:LOOPARGS`（1 次）

## 输出

- `samples:LATENT`（1 次）
- `denoised_samples:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[6, 1.0000000000000002, 5.000000000000001, 386611676435197, "randomize", true, "dpm++_sde", 0, 1, false, "comfy", 0, -1,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
