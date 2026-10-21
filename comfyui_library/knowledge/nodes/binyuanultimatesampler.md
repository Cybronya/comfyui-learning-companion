# BinyuanUltimateSampler

## 节点类型

`BinyuanUltimateSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `外部模型:MODEL`（1 次）
- `外部CLIP:CLIP`（1 次）
- `外部VAE:VAE`（1 次）
- `外部Latent:LATENT`（1 次）
- `外部正面条件:CONDITIONING`（1 次）
- `外部负面条件:CONDITIONING`（1 次）
- `上游图像_1:IMAGE`（1 次）
- `上游图像_2:IMAGE`（1 次）
- `上游图像_3:IMAGE`（1 次）
- `加载模式:COMBO`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `模型:MODEL`（1 次）
- `CLIP:CLIP`（1 次）
- `VAE:VAE`（1 次）
- `Latent:LATENT`（1 次）
- `正面条件:CONDITIONING`（1 次）
- `负面条件:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["分离式(Flux/SD3/扩散)", "None", "binyuan_krea2_edit_v1.0_bf16.safetensors", "qwen3vl_4b_fp8_scaled.safetensors", "None", "k`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
