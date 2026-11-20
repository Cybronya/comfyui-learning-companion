---
name: image_to_image_controlnet_lora_sampler_15
type: Image To Image
frequency: 2
level: weak
coverage: 0.783
common_nodes: [Anything Everywhere3, BrushNet, BrushNetLoader, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DetailTransfer, EmptyImage, GetImageSize+, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), ICLightConditioning, Image Comparer (rgthree), ImageCompositeMasked, ImageResize+, ImageResizeKJ, KSampler, LayerMask: MaskInvert, LoadAndApplyICLightUnet, LoadImage, LoraLoaderModelOnly, MaskComposite, MaskToImage, PreviewImage, ResizeMask, SAMLoader, SaveImage, VAEDecode, VAEEncode, Zoe_DepthAnythingPreprocessor]
problems: []
missing: []
members: [图片生成/图生图/【人像摄影】模特换背景_1921202873483345921.json, 图片生成/图生图/模特换背景_1921173381259935745.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【人像摄影】模特换背景_1921202873483345921.json、图片生成/图生图/模特换背景_1921173381259935745.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DetailTransfer`
- `EmptyImage`
- `GetImageSize+`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `ICLightConditioning`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageResize+`
- `ImageResizeKJ`
- `KSampler`
- `LayerMask: MaskInvert`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskComposite`
- `MaskToImage`
- `PreviewImage`
- `ResizeMask`
- `SAMLoader`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `Zoe_DepthAnythingPreprocessor`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.35 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
