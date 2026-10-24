# workflow>运算

## 节点类型

`workflow>运算`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `reuse_threshold:FLOAT`（1 次）
- `start_percent:FLOAT`（1 次）
- `end_percent:FLOAT`（1 次）

## 输出

- `文本:STRING`（1 次）
- `图像:IMAGE`（1 次）
- `*:*`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux2_dev_fp8mixed.safetensors", "default", "mistral_3_small_flux2_fp8.safetensors", "flux2", "default", "flux2-vae.sa`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
