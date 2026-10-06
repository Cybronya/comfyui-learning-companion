# easy MiniMaxH3ReferenceToVideoBridge

## 节点类型

`easy MiniMaxH3ReferenceToVideoBridge`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `clip:CLIP`（8 次）
- `vae:VAE`（8 次）
- `audio_vae:VAE`（8 次）
- `ref_image_0:IMAGE`（8 次）
- `ref_image_1:IMAGE`（8 次）
- `ref_image_2:IMAGE`（8 次）
- `ref_image_3:IMAGE`（8 次）
- `ref_image_4:IMAGE`（8 次）
- `ref_image_5:IMAGE`（8 次）
- `ref_image_6:IMAGE`（8 次）

## 输出

- `positive:CONDITIONING`（8 次）
- `latent:LATENT`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 960, 544, 124, "max"]`（5 次）
- `["", 960, 544, 124, "match"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
