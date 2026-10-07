# StoryDiffusion_Apply

## 节点类型

`StoryDiffusion_Apply`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `vae:VAE`（3 次）
- `CLIP_VISION:CLIP_VISION`（3 次）

## 输出

- `model:MODEL`（3 次）
- `switch:DIFFCONDI`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["dreamo", "none", "FLUX.1-Turbo-Alpha.safetensors", "nf4", 1, ""]`（2 次）
- `["dreamo", "none", "FLUX.1-Turbo-Alpha.safetensors", "nf4", 0.8, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
