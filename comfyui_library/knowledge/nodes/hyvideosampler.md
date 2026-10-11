# HyVideoSampler

## 节点类型

`HyVideoSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:HYVIDEOMODEL`（1 次）
- `hyvid_embeds:HYVIDEMBEDS`（1 次）
- `samples:LATENT`（1 次）
- `image_cond_latents:LATENT`（1 次）
- `stg_args:STGARGS`（1 次）
- `context_options:HYVIDCONTEXT`（1 次）
- `feta_args:FETAARGS`（1 次）
- `teacache_args:TEACACHEARGS`（1 次）
- `loop_args:LOOPARGS`（1 次）
- `fresca_args:FRESCA_ARGS`（1 次）

## 输出

- `samples:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, 65, 30, 6.000000000000001, 7.000000000000002, 135, "fixed", true, 1, "FlowMatchDiscreteScheduler", 0, "dynami`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
