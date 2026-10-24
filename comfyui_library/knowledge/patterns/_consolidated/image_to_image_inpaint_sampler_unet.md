---
name: image_to_image_inpaint_sampler_unet
type: Image To Image
frequency: 6
level: strong
coverage: 0.765667
common_nodes: [CLIPLoader, ComfySwitchNode, DrawMaskOnImage, Image Comparer (rgthree), ImageScaleToTotalPixels, InpaintCropImproved, InpaintStitchImproved, KSampler, Label (rgthree), LoadImage, PreviewImage, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, Seed (rgthree), SetLatentNoiseMask, SimpleMath+, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image-2.1-遮罩局部重绘-V1_2109819371383250946.json, 图片生成/图生图/Qwen-image21(局部编辑)_2109143172038352897.json, 图片生成/图生图/▶▷Qwen-image21-功能流(高分局部编辑&扩图)_2106723876054061057.json, 图片生成/图生图/▶▷Qwen-image21-功能流(高分局部编辑&扩图)_2107276317925404673.json, 图片生成/图生图/黑鹤 Qwen-image2.1-COS高分局部编辑_2108231665121325057.json, 图片生成/文生图/黑鹤 Qwen-image2.1-全功能流(高分局部编辑_去水印_扩图)_2107329132018364417.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_unet

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-2.1-遮罩局部重绘-V1_2109819371383250946.json、图片生成/图生图/Qwen-image21(局部编辑)_2109143172038352897.json、图片生成/图生图/▶▷Qwen-image21-功能流(高分局部编辑&扩图)_2106723876054061057.json、图片生成/图生图/▶▷Qwen-image21-功能流(高分局部编辑&扩图)_2107276317925404673.json、图片生成/图生图/黑鹤 Qwen-image2.1-COS高分局部编辑_2108231665121325057.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `DrawMaskOnImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `Seed (rgthree)`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `JoinImageWithAlpha` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `SplitImageWithAlpha` —— 5/6 个有
- `easy imageColorMatch` —— 5/6 个有
- `ImagePadForOutpaint` —— 3/6 个有
- `EmptyImage` —— 1/6 个有
- `ImageToMask` —— 1/6 个有
- `Int` —— 1/6 个有
- `easy isNone` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 25 - 35 | 6 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 25 - 35，6 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
