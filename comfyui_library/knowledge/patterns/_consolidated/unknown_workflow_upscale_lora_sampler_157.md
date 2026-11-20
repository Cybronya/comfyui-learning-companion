---
name: unknown_workflow_upscale_lora_sampler_157
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.902
common_nodes: [Any Switch (rgthree), CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, Float, FluxGuidance, GetImageSize, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerFilter: AddGrain, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_CoordinateSplitter, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTP_condsetarea_merge, TTP_condtobatch, UnetLoaderGGUF, UpscaleModelLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy bookmark, easy imageBatchToImageList, easy imageInsetCrop, easy int]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/全图肤质增强批量0202_2028727277441257474.json, 平台全量/放大加肤质增强适用低分辨率图像_2027197332344807426.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_157

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/全图肤质增强批量0202_2028727277441257474.json、平台全量/放大加肤质增强适用低分辨率图像_2027197332344807426.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Float`
- `FluxGuidance`
- `GetImageSize`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerFilter: AddGrain`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_CoordinateSplitter`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTP_condsetarea_merge`
- `TTP_condtobatch`
- `UnetLoaderGGUF`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy bookmark`
- `easy imageBatchToImageList`
- `easy imageInsetCrop`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Blur` —— 1/2 个有
- `EG_WXZ_QH` —— 1/2 个有
- `If ANY execute A else B` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageListToImageBatch` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerFilter: GaussianBlur` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `easy convertAnything` —— 1/2 个有
- `easy imageSizeByLongerSide` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.17 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.17，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
