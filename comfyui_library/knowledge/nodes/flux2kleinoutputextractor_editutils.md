# Flux2KleinOutputExtractor_EditUtils

## 节点类型

`Flux2KleinOutputExtractor_EditUtils`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `custom_output:ANY`（4 次）

## 输出

- `pad_info:ANY`（4 次）
- `main_image:IMAGE`（4 次）
- `vae_images:LIST`（4 次）
- `ref_latents:LIST`（4 次）
- `full_prompt:STRING`（4 次）
- `llama_template:STRING`（4 次）
- `no_refs_cond:CONDITIONING`（4 次）
- `mask:MASK`（4 次）
- `output_8:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
