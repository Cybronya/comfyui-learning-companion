# FramePackSingleFrameSampler

## 节点类型

`FramePackSingleFrameSampler`

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
- `initial_samples:LATENT`（1 次）
- `reference_latent:LATENT`（1 次）
- `reference_image_embeds:CLIP_VISION_OUTPUT`（1 次）
- `input_mask:MASK`（1 次）
- `reference_mask:MASK`（1 次）

## 输出

- `samples:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[15, true, 0.15, 1, 10, 0, 52738648138893, "randomize", 9, 25, "unipc_bh1", false, 1, 5, 10]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
