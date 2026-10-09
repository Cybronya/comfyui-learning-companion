# workflow>klein高清

## 节点类型

`workflow>klein高清`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 mask:MASK`（1 次）
- `mask:MASK`（1 次）
- `c:*`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `Flux2KleinEditTextEncode_EditUtils mask:MASK`（1 次）
- `LayerUtility: ImageScaleRestore V2 mask:MASK`（1 次）
- `clip_name:COMBO`（1 次）

## 输出

- `遮罩:MASK`（1 次）
- `原始大小:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `image_urls:STRING`（1 次）
- `images:IMAGE`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 遮罩:MASK`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 width:INT`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 height:INT`（1 次）
- `batch_size:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_3_8b.safetensors", "flux2", "default", "flux2-vae.safetensors", "Flux2-Klein-9B-True-v2-bf16.safetensors", "fp8_e`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
