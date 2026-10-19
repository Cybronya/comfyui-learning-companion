# LatentFrequencyEnhancer_lrzjason

## 节点类型

`LatentFrequencyEnhancer_lrzjason`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `latent:LATENT`（10 次）
- `high_freq_mult:FLOAT`（10 次）
- `sigma:FLOAT`（10 次）
- `denoise_threshold:FLOAT`（10 次）
- `mask_hardness:FLOAT`（10 次）
- `hf_pre_blur_sigma:FLOAT`（10 次）

## 输出

- `enhanced_latent:LATENT`（10 次）
- `mask_preview:IMAGE`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1.3000000000000003, 2, 0.05, 2, 0.5]`（10 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
