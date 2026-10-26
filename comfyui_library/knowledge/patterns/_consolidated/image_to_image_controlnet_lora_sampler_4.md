---
name: image_to_image_controlnet_lora_sampler_4
type: Image To Image
frequency: 4
level: strong
coverage: 0.918
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ColorAdjust(FaceParsing), ControlNetApplyAdvanced, ControlNetLoader, CropFaces, DetectFaces, Image Comparer (rgthree), ImageListSelect(FaceParsing), ImpactMakeImageBatch, ImpactSEGSToMaskBatch, ImpactSimpleDetectorSEGS, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskGrow, LoadImage, Mask Invert, MaskListSelect(FaceParsing), PreviewImage, SAMLoader, SEGSPreview, SaveImage, UltralyticsDetectorProvider, VAEDecode, VAEEncode, WarpFacesBack, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键多人换脸_1931261565742284802.json, 图片生成/图生图/一键多人换脸_1981903761713045505.json, 图片生成/图生图/多人换脸_2014769681495756802.json, 数字人/数字人/kafengduoren_1974125936012603393.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键多人换脸_1931261565742284802.json、图片生成/图生图/一键多人换脸_1981903761713045505.json、图片生成/图生图/多人换脸_2014769681495756802.json、数字人/数字人/kafengduoren_1974125936012603393.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorAdjust(FaceParsing)`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropFaces`
- `DetectFaces`
- `Image Comparer (rgthree)`
- `ImageListSelect(FaceParsing)`
- `ImpactMakeImageBatch`
- `ImpactSEGSToMaskBatch`
- `ImpactSimpleDetectorSEGS`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskGrow`
- `LoadImage`
- `Mask Invert`
- `MaskListSelect(FaceParsing)`
- `PreviewImage`
- `SAMLoader`
- `SEGSPreview`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `WarpFacesBack`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `BboxDetectorCombined_v2` —— 2/4 个有
- `ImageAndMaskPreview` —— 2/4 个有
- `ImpactImageBatchToImageList` —— 2/4 个有
- `InpaintCropImproved` —— 2/4 个有
- `Int` —— 2/4 个有
- `MaskPreview+` —— 2/4 个有
- `easy imageBatchToImageList` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | 0.5 - 0.5 | 4 | 100% |
| 采样步数 | 7 | 6 - 8 | 4 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | dpmpp_sde | - | 4 | 50% |
| 调度器 | karras | - | 4 | 50% |
| 重绘幅度 | 0.5 | 0.5 - 0.5 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.5，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 7，观测区间 6 - 8，4 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，4 个样本，一致性 50%
- 调度器 最常用 karras，4 个样本，一致性 50%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.5，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
