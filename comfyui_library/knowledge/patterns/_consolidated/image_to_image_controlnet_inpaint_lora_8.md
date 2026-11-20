---
name: image_to_image_controlnet_inpaint_lora_8
type: Image To Image
frequency: 4
level: strong
coverage: 0.8475
common_nodes: [AIO_Preprocessor, ApplyInstantID, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, Crop Face, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FaceAnalysisModels, FaceSegmentation, FluxGuidance, Get Image Size, GrowMaskWithBlur, Image To Mask, ImageConcanate, ImageInvert, ImageResize+, ImageResizeKJv2, ImageScaleToMegapixels, InpaintCrop, InpaintModelConditioning, InpaintResize, InpaintStitch, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, Load RetinaFace, LoadImage, LoraLoaderModelOnly, MaskPreview+, PlaySound|pysssss, PreviewImage, SaveImage, SetUnionControlNetType, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageCropFromMask]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX+Fill+redux+control生图+换脸保持人物和场景一致性_1922083596960727042.json, 图片生成/图生图/这不是玩具！首尾帧生图利器，redux+fill+control生图+姿态编辑（可选）_1921875986818744321.json, 平台全量/人物一致自定义克隆姿态_1921935257149325314.json, 平台全量/龙明首尾帧，redux+fill+control生图+姿态编辑_1928677714235133954.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX+Fill+redux+control生图+换脸保持人物和场景一致性_1922083596960727042.json、图片生成/图生图/这不是玩具！首尾帧生图利器，redux+fill+control生图+姿态编辑（可选）_1921875986818744321.json、平台全量/人物一致自定义克隆姿态_1921935257149325314.json、平台全量/龙明首尾帧，redux+fill+control生图+姿态编辑_1928677714235133954.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyInstantID`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `Crop Face`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FaceAnalysisModels`
- `FaceSegmentation`
- `FluxGuidance`
- `Get Image Size`
- `GrowMaskWithBlur`
- `Image To Mask`
- `ImageConcanate`
- `ImageInvert`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImageScaleToMegapixels`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintResize`
- `InpaintStitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `Load RetinaFace`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PlaySound|pysssss`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageCropFromMask`

**可变部分**（部分 workflow 才有）：
- `Hina.PoseEditor3D` —— 3/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/4 个有
- `AutoCropFaces` —— 1/4 个有
- `CLIPTextEncode (NSP)` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.8 - 0.95 | 4 | 92% |
| 采样步数 | 28 | 28 - 40 | 4 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.95，4 个样本，取值集中（一致性 92%）
- 采样步数 中位数 28，观测区间 28 - 40，4 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
