---
name: image_to_image_lora_sampler_clip_76
type: Image To Image
frequency: 4
level: weak
coverage: 0.9055
common_nodes: [Anything Everywhere, CLIPTextEncode, ConditioningZeroOut, DF_Integer, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageBatchToList+, ImageListToBatch+, KSampler, LayerColor: ColorAdapter, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculatorV2, LoadImage, LoraLoaderModelOnly, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千府AI一次修复放大工作流_1972855797787086850.json, 图片生成/图生图/千府AI三次高清放大工作流_1965644758238547970.json, 图片生成/图生图/建筑立面迁移工作流公司_1980190105518379009.json, 图片生成/图生图/高清修复放大三合一工作流【Flux+Wan2.2+seedvr2-约7分钟】_2013279668945821697.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_76

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/千府AI一次修复放大工作流_1972855797787086850.json、图片生成/图生图/千府AI三次高清放大工作流_1965644758238547970.json、图片生成/图生图/建筑立面迁移工作流公司_1980190105518379009.json、图片生成/图生图/高清修复放大三合一工作流【Flux+Wan2.2+seedvr2-约7分钟】_2013279668945821697.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DF_Integer`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageBatchToList+`
- `ImageListToBatch+`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NumberCalculatorV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `ControlNetApplyAdvanced` —— 3/4 个有
- `ControlNetLoader` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `CLIPLoader` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `ApplyFBCacheOnModel` —— 1/4 个有
- `CFGNorm` —— 1/4 个有
- `ImageListToImageBatch` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `NunchakuQwenImageDiTLoader` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有
- `SetUnionControlNetType` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有
- `VAEDecodeTiled` —— 1/4 个有
- `easy imageBatchToImageList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.2 - 0.6 | 3 | 60% |
| 采样步数 | 8 | 4 - 20 | 4 | 40% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 4 | 69% |
| 采样算法 | res_2s | - | 4 | 50% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 0.6 | 0.2 - 1 | 4 | 33% |
| LoRA 模型强度 | 0.4 | - | 1 | 100% |
| LoRA 文本强度 | 0.4 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.2 - 0.6，3 个样本
- 采样步数 中位数 8，观测区间 4 - 20，4 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 res_2s，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 0.6，观测区间 0.2 - 1，4 个样本，取值分散，一致性仅 33%
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
