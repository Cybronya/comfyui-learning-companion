# TurboDiffusionI2VSampler

## 节点类型

`TurboDiffusionI2VSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `high_noise_model:MODEL`（2 次）
- `low_noise_model:MODEL`（2 次）
- `conditioning:CONDITIONING`（2 次）
- `vae:VAE`（2 次）
- `image:IMAGE`（2 次）
- `num_frames:INT`（2 次）
- `num_steps:COMBO`（2 次）
- `resolution:COMBO`（2 次）
- `aspect_ratio:COMBO`（2 次）
- `boundary:FLOAT`（2 次）

## 输出

- `frames:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[81, 4, "720p", "9:16", 0.9, 200, 469892505616336, "randomize", false]`（1 次）
- `[49, 4, "720p", "9:16", 0.9, 180, 397352072816238, "randomize", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
