# WanVideoSampler

## 节点类型

`WanVideoSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:WANVIDEOMODEL`（4 次）
- `text_embeds:WANVIDEOTEXTEMBEDS`（4 次）
- `image_embeds:WANVIDIMAGE_EMBEDS`（4 次）
- `samples:LATENT`（4 次）
- `feta_args:FETAARGS`（3 次）
- `context_options:WANVIDCONTEXT`（3 次）
- `cache_args:CACHEARGS`（1 次）
- `flowedit_args:FLOWEDITARGS`（1 次）
- `slg_args:SLGARGS`（1 次）
- `loop_args:LOOPARGS`（1 次）

## 输出

- `samples:LATENT`（4 次）
- `denoised_samples:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[15, 6, 5, 1057359483639287, "fixed", true, "dpm++", 0, 1]`（1 次）
- `[10, 6, 5, 1057359483639286, "fixed", true, "dpm++", 0, 1]`（1 次）
- `[4, 1.0000000000000002, 11.000000000000002, 123867144405498, "randomize", true, "unipc", 0, 1, false, "comfy", 0, -1, tr`（1 次）
- `[20, 6, 5, 1041359483639289, "fixed", true, "dpm++", 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
