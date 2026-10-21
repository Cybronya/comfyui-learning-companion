---
name: unknown_workflow_upscale_lora_sampler_53
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8325
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptySD3LatentImage, Fast Bypasser (rgthree), Flux2KleinEditTextEncode_EditUtils, GetImageSize+, Image Comparer (rgthree), ImageFromBatch, ImageScaleToTotalPixels, KSampler, LayerColor: BrightnessContrastV2, LayerFilter: AddGrain, LayerFilter: GaussianBlurV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: NumberCalculator, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, PrimitiveFloat, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMathDual+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTResolutionSelector, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/▶▶瑶光+白玉V2+如梦似幻+肤若凝脂工作流V9（带模型和lora下载链接）_2047478179761229825.json, 图片生成/文生图/美少女文生图_2072994580554932225.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_53

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/▶▶瑶光+白玉V2+如梦似幻+肤若凝脂工作流V9（带模型和lora下载链接）_2047478179761229825.json、图片生成/文生图/美少女文生图_2072994580554932225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Fast Bypasser (rgthree)`
- `Flux2KleinEditTextEncode_EditUtils`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerColor: BrightnessContrastV2`
- `LayerFilter: AddGrain`
- `LayerFilter: GaussianBlurV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: NumberCalculator`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMathDual+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTResolutionSelector`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
