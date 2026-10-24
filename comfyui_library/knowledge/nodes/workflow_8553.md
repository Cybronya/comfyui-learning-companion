# workflow>二次采样

## 节点类型

`workflow>二次采样`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `Flux2KleinConfigPreparer_EditUtils image:IMAGE`（1 次）
- `configs:LIST`（1 次）
- `mask:MASK`（1 次）
- `vae_name:COMBO`（1 次）
- `value:INT`（1 次）
- `Steps value:INT`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `clip_name:COMBO`（1 次）

## 输出

- `config:ANY`（1 次）
- `main_image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `Flux2KleinOutputExtractor_EditUtils main_image:IMAGE`（1 次）
- `vae_images:LIST`（1 次）
- `ref_latents:LIST`（1 次）
- `full_prompt:LIST`（1 次）
- `llama_template:STRING`（1 次）
- `no_refs_cond:STRING`（1 次）
- `Flux2KleinOutputExtractor_EditUtils mask:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux2-vae.safetensors", 232106786800958, "fixed", 4, "fixed", "fluxKleinFP8_flux2KleinBase9bFp8.safetensors", "fp8_e4m`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
