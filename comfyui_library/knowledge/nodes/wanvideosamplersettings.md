# WanVideoSamplerSettings

## 节点类型

`WanVideoSamplerSettings`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:WANVIDEOMODEL`（5 次）
- `image_embeds:WANVIDIMAGE_EMBEDS`（5 次）
- `text_embeds:WANVIDEOTEXTEMBEDS`（5 次）
- `samples:LATENT`（5 次）
- `feta_args:FETAARGS`（5 次）
- `context_options:WANVIDCONTEXT`（5 次）
- `cache_args:CACHEARGS`（5 次）
- `flowedit_args:FLOWEDITARGS`（5 次）
- `slg_args:SLGARGS`（5 次）
- `loop_args:LOOPARGS`（5 次）

## 输出

- `sampler_inputs:SAMPLER_ARGS`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[10, 1, 12, 2, "fixed", true, "longcat_distill_euler", 0, 1, false, "comfy", 0, -1, false]`（1 次）
- `[10, 1, 12, 3, "fixed", true, "longcat_distill_euler", 0, 1, false, "comfy", 0, -1, false]`（1 次）
- `[10, 1, 12, 4, "fixed", true, "longcat_distill_euler", 0, 1, false, "comfy", 0, -1, false]`（1 次）
- `[10, 1, 12, 1, "fixed", true, "longcat_distill_euler", 0, 1, false, "comfy", 0, -1, false]`（1 次）
- `[10, 1, 12, 0, "fixed", true, "longcat_distill_euler", 0, 1, false, "comfy", 0, -1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
