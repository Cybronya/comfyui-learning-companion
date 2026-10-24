---
name: unknown_workflow_inpaint_lora_sampler_28
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8015
common_nodes: [Anything Everywhere3, BiRefNetRMBG, CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GetImageSize, GetImageSize+, Image Comparer (rgthree), ImageCrop+, ImageToMask, InpaintCropImproved, InpaintModelConditioning, InpaintStitchImproved, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MaskPreview+, MaskToImage, PreviewImage, RH_Translator, ReduxAdvanced, SaveImage, ShowText, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键换脸_1974123248587771905.json, 图片生成/图生图/一键迁移，万物迁移，人物迁移，首饰，换装，加速版（Redux Ace++ OneReward）_1967070558049406977.json, 图片生成/图生图/无痕换脸，自动调整面部角度_1974024583470780417.json, 图片生成/图生图/电商换装，换脸，万物迁移。可以框选产品_1969985819773726721.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键换脸_1974123248587771905.json、图片生成/图生图/一键迁移，万物迁移，人物迁移，首饰，换装，加速版（Redux Ace++ OneReward）_1967070558049406977.json、图片生成/图生图/无痕换脸，自动调整面部角度_1974024583470780417.json、图片生成/图生图/电商换装，换脸，万物迁移。可以框选产品_1969985819773726721.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `BiRefNetRMBG`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GetImageSize`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageCrop+`
- `ImageToMask`
- `InpaintCropImproved`
- `InpaintModelConditioning`
- `InpaintStitchImproved`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `RH_Translator`
- `ReduxAdvanced`
- `SaveImage`
- `ShowText`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `LayerUtility: CropByMask V2` —— 3/4 个有
- `Switch conditioning [Crystools]` —— 3/4 个有
- `easy ifElse` —— 3/4 个有
- `easy isMaskEmpty` —— 3/4 个有
- `FaceAlign` —— 2/4 个有
- `FaceAnalysisModels` —— 2/4 个有
- `ApplyPulidFlux` —— 1/4 个有
- `AutoCropFaces` —— 1/4 个有
- `ColorMatch` —— 1/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `InstantIDFaceAnalysis` —— 1/4 个有
- `MirroredImage` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PulidFluxEvaClipLoader` —— 1/4 个有
- `PulidFluxModelLoader` —— 1/4 个有
- `ReActorFaceSwap` —— 1/4 个有
- `easy sleep` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 0.3 - 1 | 4 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，4 个样本
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
