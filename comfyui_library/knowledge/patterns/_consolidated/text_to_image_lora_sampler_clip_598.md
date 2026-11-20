---
name: text_to_image_lora_sampler_clip_598
type: Text To Image
frequency: 3
level: strong
coverage: 0.849
common_nodes: [AddLabel, AddMask, ApplyPulidFlux, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, GetImageSize+, Image Padding, ImageAndMaskPreview, ImageConcanate, JWImageResizeByLongerSide, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, ReferenceLatent, SaveImage, Text Concatenate (JPS), TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/地表最强FLUX超完美换装工作流，一键图片秒换装_1941329998760538114.json, 平台全量/教程身材控制Kontext 换装秀2.0_1943651363303649282.json, 平台全量/教程逐步完善提示词Kontext 换装秀2.0_1943650043541028865.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_598

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/地表最强FLUX超完美换装工作流，一键图片秒换装_1941329998760538114.json、平台全量/教程身材控制Kontext 换装秀2.0_1943651363303649282.json、平台全量/教程逐步完善提示词Kontext 换装秀2.0_1943650043541028865.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `AddMask`
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize+`
- `Image Padding`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `ReferenceLatent`
- `SaveImage`
- `Text Concatenate (JPS)`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Crop Image Square (JPS)` —— 2/3 个有
- `DownloadAndLoadFlorence2Model` —— 2/3 个有
- `Florence2Run` —— 2/3 个有
- `ImageRemoveAlpha+` —— 2/3 个有
- `ImageStitch` —— 2/3 个有
- `LayerMask: BenUltra` —— 2/3 个有
- `LayerMask: LoadBenModel` —— 2/3 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 2/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/3 个有
- `SubtractMask` —— 2/3 个有
- `easy imageSizeByLongerSide` —— 2/3 个有
- `ImpactSwitch` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1024 - 1536 | 3 | 82% |
| 高度 | 1152 | 768 - 1152 | 3 | 82% |
| 采样步数 | 12 | 12 - 12 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，观测区间 1024 - 1536，3 个样本，取值集中（一致性 82%）
- 高度 中位数 1152，观测区间 768 - 1152，3 个样本，取值集中（一致性 82%）
- 采样步数 中位数 12，观测区间 12 - 12，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
