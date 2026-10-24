---
name: image_to_image_controlnet_upscale_sampler_6
type: Image To Image
frequency: 2
level: weak
coverage: 0.887
common_nodes: [ApplyFBCacheOnModel, ApplyInstantID, CLIPTextEncode, CR Upscale Image, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, CropFace, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, Florence2Run, Florence2toCoordinates, GetImageSize+, GrowMaskWithBlur, Image Comparer (rgthree), ImageComposite+, ImageScale, ImageScaleBy, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LoadImage, MaskPreview+, PreviewImage, Sam2Segmentation, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Florence2 + InstantID：多人同屏精准换脸_修复工作流_1997845376902344706.json, 图片生成/图生图/图像编辑 _ Kontext多图融合+修脸_1946547822981181441.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_sampler_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Florence2 + InstantID：多人同屏精准换脸_修复工作流_1997845376902344706.json、图片生成/图生图/图像编辑 _ Kontext多图融合+修脸_1946547822981181441.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `ApplyInstantID`
- `CLIPTextEncode`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropFace`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `Florence2Run`
- `Florence2toCoordinates`
- `GetImageSize+`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageComposite+`
- `ImageScale`
- `ImageScaleBy`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask`
- `LayerUtility: LayerImageTransform`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `Sam2Segmentation`
- `SaveImage`
- `SetLatentNoiseMask`
- `VAEDecode`
- `VAEEncode`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `IntToText` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `JjkShowText` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `ResizeLongestToNode` —— 1/2 个有
- `Text` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.1 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.5 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
