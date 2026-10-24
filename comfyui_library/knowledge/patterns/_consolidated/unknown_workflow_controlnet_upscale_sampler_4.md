---
name: unknown_workflow_controlnet_upscale_sampler_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.864
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSize+, Image Comparer (rgthree), KSamplerAdvanced, LoadImage, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-lmage-Turbo 一键老建筑换新居所_2030933528707338242.json, 图片生成/文生图/Z-Image-Turbo ControlNet_2057628633455484929.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_sampler_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-lmage-Turbo 一键老建筑换新居所_2030933528707338242.json、图片生成/文生图/Z-Image-Turbo ControlNet_2057628633455484929.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageListToImageBatch` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImpactImageBatchToImageList` —— 1/2 个有
- `LayerUtility: If ` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SimpleComparison+` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 50% |
| 高度 | 1280 | - | 2 | 40% |
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
