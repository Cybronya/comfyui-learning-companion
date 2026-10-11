# HunyuanImageToVideo

## 节点类型

`HunyuanImageToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `positive:CONDITIONING`（3 次）
- `vae:VAE`（3 次）
- `start_image:IMAGE`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `length:INT`（1 次）
- `batch_size:INT`（1 次）
- `guidance_type:COMBO`（1 次）

## 输出

- `positive:CONDITIONING`（3 次）
- `latent:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[848, 480, 65, 1, "v2 (replace)"]`（2 次）
- `[848, 480, 53, 1, "v1 (concat)"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
