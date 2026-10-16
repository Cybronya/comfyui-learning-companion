# MiniMaxH3ImageToVideoTail

## 节点类型

`MiniMaxH3ImageToVideoTail`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）
- `first_frame:IMAGE`（1 次）
- `last_frame:IMAGE`（1 次）
- `video_latent:LATENT`（1 次）
- `prompt:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `length:INT`（1 次）
- `apply_keyframes:COMBO`（1 次）

## 输出

- `positive:CONDITIONING`（1 次）
- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 1344, 768, 124, "enable"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
