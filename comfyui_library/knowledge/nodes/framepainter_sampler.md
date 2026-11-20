# FramePainter_Sampler

## 节点类型

`FramePainter_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL_FramePainter`（2 次）
- `clip_vision:CLIP_VISION`（2 次）
- `vae:VAE`（2 次）
- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[958686947, "randomize", 30, 3, 512, 512, 0.8]`（1 次）
- `[1505803624, "randomize", 25, 3, 384, 704, 0.8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
