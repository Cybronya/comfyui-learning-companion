# QwenEditOutputExtractor_EditUtils

## 节点类型

`QwenEditOutputExtractor_EditUtils`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `custom_output:ANY`（1 次）

## 输出

- `pad_info:ANY`（1 次）
- `full_refs_cond:CONDITIONING`（1 次）
- `main_ref_cond:CONDITIONING`（1 次）
- `main_image:IMAGE`（1 次）
- `vae_images:LIST`（1 次）
- `ref_latents:LIST`（1 次）
- `vl_images:LIST`（1 次）
- `full_prompt:STRING`（1 次）
- `llama_template:STRING`（1 次）
- `no_refs_cond:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
