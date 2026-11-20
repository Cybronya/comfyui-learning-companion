# workflow>nunchaku内补

## 节点类型

`workflow>nunchaku内补`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 image:IMAGE`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 mask:MASK`（1 次）
- `缩放到长度:INT`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 scale_to_length:INT`（1 次）

## 输出

- `VAE:VAE`（1 次）
- `遮罩:MASK`（1 次）
- `原始大小:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `图像:IMAGE`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 原始大小:BOX`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 width:INT`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 height:INT`（1 次）
- `Latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux.1", "clip_l.safetensors", "awq-int4-flux.1-t5xxl.safetensors", 512, "ae.sft", "svdq-int4-flux.1-fill-dev", 0.1000`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
