# WanVideoDiffusionForcingSampler

## 节点类型

`WanVideoDiffusionForcingSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:WANVIDEOMODEL`（3 次）
- `text_embeds:WANVIDEOTEXTEMBEDS`（3 次）
- `image_embeds:WANVIDIMAGE_EMBEDS`（3 次）
- `samples:LATENT`（3 次）
- `prefix_samples:LATENT`（3 次）
- `cache_args:CACHEARGS`（3 次）
- `slg_args:SLGARGS`（3 次）
- `experimental_args:EXPERIMENTALARGS`（3 次）
- `unianimate_poses:UNIANIMATE_POSE`（3 次）

## 输出

- `samples:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[10, 24.000000000000004, 30, 4.000000000000001, 5.000000000000001, 0, "fixed", true, "unipc", 1, "comfy"]`（2 次）
- `[24, 24.000000000000004, 30, 4.000000000000001, 5.000000000000001, 0, "fixed", true, "unipc", 1, "comfy"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
