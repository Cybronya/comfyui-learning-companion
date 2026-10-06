# MiniMaxH3LatentUpscaleBy32T8

## 节点类型

`MiniMaxH3LatentUpscaleBy32T8`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `latent:LATENT`（2 次）
- `upscale_method:COMBO`（2 次）
- `scale_by:FLOAT`（2 次）
- `pixels_per_latent:COMBO`（2 次）
- `alignment_policy:COMBO`（2 次）

## 输出

- `latent:LATENT`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `report_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["bicubic", 2.0000000000000004, "16 - MiniMax H3", "best_aspect"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
