---
name: unknown_workflow_inpaint_lora_sampler_20
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6244
common_nodes: [CLIPTextEncodeFlux, CLIPVisionLoader, CR Latent Batch Size, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, ImageCrop+, ImpactImageBatchToImageList, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LayerMask: LoadFlorence2Model, LayerMask: MaskPreview, LayerUtility: CropByMask V2, LayerUtility: Florence2Image2Prompt, LayerUtility: ImageRemoveAlpha, LayerUtility: PurgeVRAM, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Redux + ACE++：万物迁移，颠覆创作界限！_1948165906064113665.json, 图片生成/图生图/万物迁移FLUX Fill+Redux+ACE++_1955515219034476545.json, 图片生成/图生图/分镜角色一致性迁移替换Flux Fill+Redux+ACE+Pulid+CN+SeedVR2超分_1938862665387139074.json, 图片生成/图生图/分镜角色一致性迁移替换Flux Fill+Redux+ACE+Pulid+CN+SeedVR2超分_1938942475358949377.json, 图片生成/图生图/模特迁移-Pose迁移_1950099234763751425.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Redux + ACE++：万物迁移，颠覆创作界限！_1948165906064113665.json、图片生成/图生图/万物迁移FLUX Fill+Redux+ACE++_1955515219034476545.json、图片生成/图生图/分镜角色一致性迁移替换Flux Fill+Redux+ACE+Pulid+CN+SeedVR2超分_1938862665387139074.json、图片生成/图生图/分镜角色一致性迁移替换Flux Fill+Redux+ACE+Pulid+CN+SeedVR2超分_1938942475358949377.json、图片生成/图生图/模特迁移-Pose迁移_1950099234763751425.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `CR Latent Batch Size`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `ImageCrop+`
- `ImpactImageBatchToImageList`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: MaskPreview`
- `LayerUtility: CropByMask V2`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `InpaintResize` —— 4/5 个有
- `LayerMask: BiRefNetUltraV2` —— 4/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 4/5 个有
- `MaskToImage` —— 4/5 个有
- `Replace Text _O` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `String Literal` —— 4/5 个有
- `easy imageSize` —— 4/5 个有
- `AIO_Preprocessor` —— 3/5 个有
- `Anything Everywhere3` —— 3/5 个有
- `ApplyPulidFlux` —— 3/5 个有
- `ControlNetApplySD3` —— 3/5 个有
- `ControlNetLoader` —— 3/5 个有
- `CropFace` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `PulidFluxEvaClipLoader` —— 3/5 个有
- `PulidFluxInsightFaceLoader` —— 3/5 个有
- `PulidFluxModelLoader` —— 3/5 个有
- `SetUnionControlNetType` —— 3/5 个有
- `ApplyTeaCacheAndSkipBlocks` —— 2/5 个有
- `ColorMatch` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `SeedVR2` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `CLIPTextEncode` —— 1/5 个有
- `FluxGuidance` —— 1/5 个有
- `Get Image Size` —— 1/5 个有
- `Joy_caption` —— 1/5 个有
- `Joy_caption_load` —— 1/5 个有
- `LayerMask: BenUltra` —— 1/5 个有
- `LayerMask: LoadBenModel` —— 1/5 个有
- `LayerMask: MaskStroke` —— 1/5 个有
- `MaskPreview+` —— 1/5 个有
- `ModelSamplingFlux` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 28 | 5 | 51% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 0.9 | 0.9 - 0.9 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 28，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.9，观测区间 0.9 - 0.9，3 个样本，取值集中（一致性 100%）
