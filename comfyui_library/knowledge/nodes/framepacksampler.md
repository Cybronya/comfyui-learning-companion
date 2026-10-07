# FramePackSampler

## 节点类型

`FramePackSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:FramePackMODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `start_latent:LATENT`（1 次）
- `image_embeds:CLIP_VISION_OUTPUT`（1 次）
- `end_latent:LATENT`（1 次）
- `end_image_embeds:CLIP_VISION_OUTPUT`（1 次）
- `initial_samples:LATENT`（1 次）

## 输出

- `samples:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20, true, 0.15, 1, 10, 0, 71, "fixed", 9, 1, 3, "unipc_bh1", 1, 1, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
