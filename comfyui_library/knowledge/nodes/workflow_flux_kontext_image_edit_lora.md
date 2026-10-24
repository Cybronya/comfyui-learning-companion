# workflow>Flux kontext image edit lora

## 节点类型

`workflow>Flux kontext image edit lora`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `LATENT:LATENT`（1 次）
- `vae_name:COMBO`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `clip_name1:COMBO`（1 次）
- `clip_name2:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `lora_name:COMBO`（1 次）
- `strength_model:FLOAT`（1 次）

## 输出

- `LATENT:LATENT`（1 次）
- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ae.safetensors", "flux1-dev-kontext_fp8_scaled.safetensors", "default", "t5xxl_fp8_e4m3fn_scaled.safetensors", "clip_l`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
