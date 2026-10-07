# Wan22FunControlToVideo

## 节点类型

`Wan22FunControlToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `vae:VAE`（3 次）
- `ref_image:IMAGE`（3 次）
- `control_video:IMAGE`（3 次）

## 输出

- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `latent:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[640, 640, 81, 1]`（2 次）
- `[704, 704, 121, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
