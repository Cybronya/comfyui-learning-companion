---
name: unknown_workflow_inpaint_lora_sampler_4
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.893167
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, ConstrainImage|pysssss, DetailerForEach, DualCLIPLoader, EmptyImage, FaceAnalysisModels, FaceBoundingBox, FluxGuidance, GrowMaskWithBlur, Image Comparer (rgthree), ImageConcanate, ImageCrop, ImageResize+, ImageToMask, ImpactGaussianBlurMask, InpaintModelConditioning, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, MaskToImage, MaskToSEGS, PreviewImage, ReduxAdvanced, ResizeMask, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, preview_mask]
problems: []
missing: []
members: [图片生成/图生图/FLUX Redux+ACE++ 换脸_2001943816934420482.json, 图片生成/图生图/FLUX Redux+ACE++ 换脸工作流_1895719152445751298.json, 图片生成/图生图/FLUX Redux+ACE++ 换脸工作流_2012087167392157697.json, 图片生成/图生图/FLUX Redux+ACE++ 换脸工作流_2020043139452510210.json, 图片生成/图生图/FLUX Redux+ACE++ 换脸工作流_2047506205597241345.json, 图片生成/图生图/FLUX Redux+ACE高清换脸_2066039713353523202.json, 图片生成/图生图/FLUX+Redux+ACE+++换脸工作流_2042518669216976898.json, 图片生成/图生图/FLUX_Redux+ACE++_换脸工作流_2098910351919243265.json, 图片生成/图生图/FLUX_Redux+ACE++_换脸工作流_2098972141172649985.json, 图片生成/图生图/全自动换头换脸  指定换脸真实自然 写实换脸换装_2091707597454925826.json, 图片生成/图生图/无痕换脸-FLUX+Redux+ACE_2089616148764643330.json, 图片生成/图生图/角色一致性换脸工作流_2044033278356754433.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/FLUX Redux+ACE++ 换脸_2001943816934420482.json、图片生成/图生图/FLUX Redux+ACE++ 换脸工作流_1895719152445751298.json、图片生成/图生图/FLUX Redux+ACE++ 换脸工作流_2012087167392157697.json、图片生成/图生图/FLUX Redux+ACE++ 换脸工作流_2020043139452510210.json、图片生成/图生图/FLUX Redux+ACE++ 换脸工作流_2047506205597241345.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DetailerForEach`
- `DualCLIPLoader`
- `EmptyImage`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageCrop`
- `ImageResize+`
- `ImageToMask`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `MaskToSEGS`
- `PreviewImage`
- `ReduxAdvanced`
- `ResizeMask`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `preview_mask`

**可变部分**（部分 workflow 才有）：
- `TeaCache` —— 11/12 个有
- `GetImageSize+` —— 1/12 个有
- `GetNode` —— 1/12 个有
- `If ANY execute A else B` —— 1/12 个有
- `Image Tiled` —— 1/12 个有
- `ImageConcanateOfUtils` —— 1/12 个有
- `ImageFromBatch` —— 1/12 个有
- `ImageListToBatch+` —— 1/12 个有
- `ImagePass` —— 1/12 个有
- `ImageUpscaleWithModel` —— 1/12 个有
- `Images to RGB` —— 1/12 个有
- `ImpactCompare` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `SeedVR2LoadDiTModel` —— 1/12 个有
- `SeedVR2LoadVAEModel` —— 1/12 个有
- `SeedVR2VideoUpscaler` —— 1/12 个有
- `SetNode` —— 1/12 个有
- `TTP_Image_Assy` —— 1/12 个有
- `TTP_Image_Tile_Batch` —— 1/12 个有
- `TTP_Tile_image_size` —— 1/12 个有
- `UpscaleModelLoader` —— 1/12 个有
- `easy imageBatchToImageList` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 15 - 15 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | normal | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，观测区间 15 - 15，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 normal，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
