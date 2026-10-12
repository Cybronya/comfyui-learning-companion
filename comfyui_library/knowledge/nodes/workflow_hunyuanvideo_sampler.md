# workflow/HunyuanVideo Sampler

## 节点类型

`workflow/HunyuanVideo Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `参考图像大小:IMAGE`（1 次）
- `vae:VAE`（1 次）
- `model:HYVIDEOMODEL`（1 次）
- `hyvid_embeds:HYVIDEMBEDS`（1 次）
- `samples:LATENT`（1 次）
- `stg_args:STGARGS`（1 次）
- `context_options:HYVIDCONTEXT`（1 次）
- `feta_args:FETAARGS`（1 次）
- `teacache_args:TEACACHEARGS`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `ColorMatch 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[544, 960, "lanczos", false, 2, "center", true, 64, 256, true, 0, 1, 49, 30, 1, 7, 15, "fixed", true, 1, "FlowMatchDiscr`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
