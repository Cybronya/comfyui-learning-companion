# workflow>vae

## 节点类型

`workflow>vae`

## 分类

Latent

## 作用

VAE 相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（1 次）
- `model:MODEL`（1 次）
- `FluxKontextMultiReferenceLatentMethod conditioning:CONDITIONING`（1 次）
- `samples:LATENT`（1 次）
- `vae:VAE`（1 次）
- `reference_latents_method:COMBO`（1 次）
- `shift:FLOAT`（1 次）
- `FluxKontextMultiReferenceLatentMethod reference_latents_method:COMBO`（1 次）
- `strength:FLOAT`（1 次）
- `tile_size:INT`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）
- `FluxKontextMultiReferenceLatentMethod CONDITIONING:CONDITIONING`（1 次）
- `patched_model:MODEL`（1 次）
- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["index_timestep_zero", 3.1, "index_timestep_zero", 1, 512, 64, 64, 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
