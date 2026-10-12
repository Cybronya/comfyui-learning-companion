# workflow>FLUX-K

## 节点类型

`workflow>FLUX-K`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `clip_name1:COMBO`（1 次）
- `clip_name2:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `lora_name:COMBO`（1 次）
- `strength_model:FLOAT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux1-kontext-dev.safetensors", "fp8_e4m3fn", "clip_l.safetensors", "t5xxl_fp8_e4m3fn.safetensors", "flux", "default",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
