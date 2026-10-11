# LTXLatentAnchorAware

## 节点类型

`LTXLatentAnchorAware`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `reference_image:IMAGE`（2 次）
- `vae:VAE`（2 次）
- `energy_latent:LATENT`（2 次）
- `sigmas:SIGMAS`（2 次）
- `strength:FLOAT`（2 次）
- `cache_at_step:INT`（2 次）
- `similarity_threshold:FLOAT`（2 次）
- `decay_with_distance:FLOAT`（2 次）
- `energy_threshold:FLOAT`（2 次）

## 输出

- `model:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.11, 5, 0.5, 0.15000000000000002, 0.3, false, false, true, "schedule", 2, 50, 0, "flat", ""]`（1 次）
- `[0.045, 3, 0.25, 0.08, 0.15, false, false, true, "schedule", 2, 50, 0, "flat", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
