---
name: image_to_image_lora_sampler_clip_33
type: Image To Image
frequency: 8
level: moderate
coverage: 0.818375
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageListToBatch+, KSampler, LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculatorV2, LoadImage, LoraLoaderModelOnly, PrimitiveInt, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TeaCache, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/三种放大_1968936654675271681.json, 图片生成/图生图/三种放大对比_2073054547806871554.json, 图片生成/图生图/全能图片V1 Kontext 无损高清放大 最强人物一致性多参考图像编辑工作流 -Star_1965863881858002945.json, 图片生成/图生图/全能图片V1 Kontext 无损高清放大 最强人物一致性多参考图像编辑工作流 -Star_1969621426330345474.json, 图片生成/图生图/图生图Kontext高清放大_2026534566969741313.json, 图片生成/图生图/最强VR2+kt分块放大工作流_1987840205463990274.json, 图片生成/文生图/(贞贞皮衣版)白转Qwen-古风差异采样文生图加速多重放大去油版V1_1975202358164631553.json, 图片生成/文生图/1+QwenImage_V2_20251022OTT_1983932162795831298.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/三种放大_1968936654675271681.json、图片生成/图生图/三种放大对比_2073054547806871554.json、图片生成/图生图/全能图片V1 Kontext 无损高清放大 最强人物一致性多参考图像编辑工作流 -Star_1965863881858002945.json、图片生成/图生图/全能图片V1 Kontext 无损高清放大 最强人物一致性多参考图像编辑工作流 -Star_1969621426330345474.json、图片生成/图生图/图生图Kontext高清放大_2026534566969741313.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToBatch+`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NumberCalculatorV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TeaCache`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: Seed` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `ImpactImageBatchToImageList` —— 5/8 个有
- `LayerUtility: ImageMaskScaleAs` —— 5/8 个有
- `LayerUtility: PurgeVRAM` —— 5/8 个有
- `SeedVR2BlockSwap` —— 5/8 个有
- `CLIPLoader` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `ImageBatchToList+` —— 3/8 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 3/8 个有
- `LayerUtility: PurgeVRAM V2` —— 3/8 个有
- `SeedVR2ExtraArgs` —— 3/8 个有
- `SeedVR2GGUF` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `EmptySD3LatentImage` —— 2/8 个有
- `GetNode` —— 2/8 个有
- `ImageListToImageBatch` —— 2/8 个有
- `LoraLoader` —— 2/8 个有
- `ModelSamplingAuraFlow` —— 2/8 个有
- `ModelSamplingSD3` —— 2/8 个有
- `RH_Nano_Banana_Image2Image` —— 2/8 个有
- `SeedVR2` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `Text Concatenate` —— 2/8 个有
- `easy anythingIndexSwitch` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `easy imageConcat` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `CameraWatermarkNode` —— 1/8 个有
- `GridLoras` —— 1/8 个有
- `JC` —— 1/8 个有
- `JC_ExtraOptions` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/8 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/8 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有
- `SaveImagePlus` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 8 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 58% |
| 采样算法 | euler | - | 8 | 62% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 0.1 - 1 | 8 | 50% |
| LoRA 模型强度 | 0.75 | - | 2 | 67% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，8 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，8 个样本，取值分散，一致性仅 50%
- LoRA 模型强度 中位数 0.75，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
