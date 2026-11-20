---
name: unknown_workflow_sampler_clip_unet_75
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.95575
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/PS专用 klein 9b 扩图_2071036709902569474.json, 图片生成/图生图/Q版色稿转成品_2092805656247099393.json, 图片生成/图生图/flux 2 klein edit single image 单图编辑_2044446355933896705.json, 图片生成/图生图/flux klein单图编辑_2085594588139581442.json, 图片生成/图生图/flux klein双图编辑工作流_2085595709289623554.json, 图片生成/图生图/flux klein双图编辑工作流_2105577595982143490.json, 图片生成/图生图/flux klein双图编辑工作流_2105650140253089794.json, 图片生成/图生图/flux-2-klein-4b单图编辑_2033454491990761473.json, 图片生成/图生图/flux-2-klein-9b模型图像编辑_2094963430150201346.json, 图片生成/图生图/flux2 klein 9B 4视图_2050825970894028801.json, 图片生成/图生图/flux2 klein扩图工作流_2016349875780194305.json, 图片生成/图生图/kelin精修V2_2061361375989035010.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_75

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/PS专用 klein 9b 扩图_2071036709902569474.json、图片生成/图生图/Q版色稿转成品_2092805656247099393.json、图片生成/图生图/flux 2 klein edit single image 单图编辑_2044446355933896705.json、图片生成/图生图/flux klein单图编辑_2085594588139581442.json、图片生成/图生图/flux klein双图编辑工作流_2085595709289623554.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 11/12 个有
- `ConditioningZeroOut` —— 9/12 个有
- `Image Comparer (rgthree)` —— 5/12 个有
- `LoraLoaderModelOnly` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `String Literal` —— 3/12 个有
- `ColorMatch` —— 2/12 个有
- `ImageScale` —— 2/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `CheckpointLoaderSimple` —— 1/12 个有
- `DrawMaskOnImage` —— 1/12 个有
- `FlexLoraLoaderModelOnly` —— 1/12 个有
- `ImageColorMatch+` —— 1/12 个有
- `ImagePadForOutpaint` —— 1/12 个有
- `ImpactGaussianBlurMask` —— 1/12 个有
- `MaskPreview+` —— 1/12 个有
- `PixelSnapping` —— 1/12 个有
- `TextBoxMira` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
