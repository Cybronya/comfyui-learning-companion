# workflow>11

## 节点类型

`workflow>11`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `easy imageSizeByLongerSide image:IMAGE`（1 次）
- `输入任何:*`（1 次）
- `遮罩:MASK`（1 次）
- `GrowMaskWithBlur mask:MASK`（1 次）
- `image:IMAGE`（1 次）
- `InpaintCropImproved image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `optional_context_mask:MASK`（1 次）
- `PreviewImage images:IMAGE`（1 次）

## 输出

- `遮罩:MASK`（1 次）
- `反转遮罩:MASK`（1 次）
- `GrowMaskWithBlur 反转遮罩:MASK`（1 次）
- `stitcher:STITCHER`（1 次）
- `模型:MODEL`（1 次）
- `*:*`（1 次）
- `image_urls:STRING`（1 次）
- `PreviewImage image_urls:STRING`（1 次）
- `PreviewImage 41 image_urls:STRING`（1 次）
- `PreviewImage 47 image_urls:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1600, "4x-UltraSharp.pth", "4x-UltraSharp.pth", 1600, "4x-ClearRealityV1.pth", 1600, "flux1-redux-dev.safetensors", "cl`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
