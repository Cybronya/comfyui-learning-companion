---
name: unknown_workflow_upscale_lora_sampler_95
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.868667
common_nodes: [CLIPLoader, ConditioningZeroOut, Fast Bypasser (rgthree), Flux2KleinEditTextEncode_EditUtils, Image Comparer (rgthree), ImageFromBatch, KSampler, LayerColor: BrightnessContrastV2, LayerFilter: AddGrain, LayerFilter: GaussianBlurV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: NumberCalculator, LoraLoaderModelOnly, MathExpression|pysssss, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/▶▶瑶光+白玉V2+如梦似幻+肤若凝脂工作流V9（带模型和lora下载链接）_2047478179761229825.json, 图片生成/文生图/美少女文生图_2072994580554932225.json, 平台全量/超分放大（4K）_2081939614541115394.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_95

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/▶▶瑶光+白玉V2+如梦似幻+肤若凝脂工作流V9（带模型和lora下载链接）_2047478179761229825.json、图片生成/文生图/美少女文生图_2072994580554932225.json、平台全量/超分放大（4K）_2081939614541115394.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Bypasser (rgthree)`
- `Flux2KleinEditTextEncode_EditUtils`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `KSampler`
- `LayerColor: BrightnessContrastV2`
- `LayerFilter: AddGrain`
- `LayerFilter: GaussianBlurV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: NumberCalculator`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PreviewImage`
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
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `GetImageSize+` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `SimpleMathDual+` —— 2/3 个有
- `TTResolutionSelector` —— 2/3 个有
- `UltimateSDUpscale` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `LoadImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | 1 - 1 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
