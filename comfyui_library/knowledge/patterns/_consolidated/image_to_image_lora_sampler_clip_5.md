---
name: image_to_image_lora_sampler_clip_5
type: Image To Image
frequency: 3
level: moderate
coverage: 0.805667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, Image Comparer (rgthree), ImageBatchToList+, ImageListToBatch+, KSampler, LayerColor: ColorAdapter, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculatorV2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LayerUtility: Seed, LoadImage, LoraLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveInt, ReferenceLatent, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TeaCache, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [ImageBatchToList+, ImageListToBatch+, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculatorV2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LayerColor: ColorAdapter, LayerUtility: Seed, image resize]
members: [图片生成/文生图/(贞贞皮衣版)白转Qwen-古风差异采样文生图加速多重放大去油版V1_1975202358164631553.json, 图片生成/文生图/1+QwenImage_V2_20251022OTT_1983932162795831298.json, 图片生成/文生图/1968297890005299202.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/(贞贞皮衣版)白转Qwen-古风差异采样文生图加速多重放大去油版V1_1975202358164631553.json、图片生成/文生图/1+QwenImage_V2_20251022OTT_1983932162795831298.json、图片生成/文生图/1968297890005299202.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageBatchToList+`
- `ImageListToBatch+`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NumberCalculatorV2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: Seed`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TeaCache`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `CameraWatermarkNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GridLoras` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `JC` —— 1/3 个有
- `JC_ExtraOptions` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SaveImagePlus` —— 1/3 个有
- `Textbox` —— 1/3 个有
- `image resize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 3 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | 0.5 - 1 | 3 | 72% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，3 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.5 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ImageBatchToList+、ImageListToBatch+、LayerUtility: ImageMaskScaleAsV2、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: NumberCalculatorV2
