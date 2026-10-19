# LatentNoised

## 节点类型

`LatentNoised`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `latent_image:LATENT`（2 次）
- `latent_noise:LATENT`（2 次）
- `mask:MASK`（2 次）
- `add_noise:BOOLEAN`（2 次）
- `noise_is_latent:BOOLEAN`（2 次）
- `noise_type:COMBO`（2 次）
- `alpha:FLOAT`（2 次）
- `k:FLOAT`（2 次）
- `noise_seed:INT`（2 次）
- `noise_strength:FLOAT`（2 次）

## 输出

- `latent_noised:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, false, "perlin", 1, 1, 786422380791499, "fixed", 2.2, "false"]`（1 次）
- `[true, false, "perlin", 1, 1, 786422380791499, "fixed", 2.66, "false"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
