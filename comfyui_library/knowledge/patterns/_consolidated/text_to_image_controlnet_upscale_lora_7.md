---
name: text_to_image_controlnet_upscale_lora_7
type: Text To Image
frequency: 3
level: moderate
coverage: 0.894333
common_nodes: [CFGGuider, CFGNorm, CLIPLoader, CLIPTextEncode, CR Conditioning Input Switch, CR Latent Input Switch, CR Model Input Switch, CR SDXL Aspect Ratio, CR Text, CR Text Concatenate, CannyEdgePreprocessor, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetApplySD3, ControlNetLoader, DWPreprocessor, DepthAnythingV2Preprocessor, DrawMaskOnImage, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, FluxKontextMultiReferenceLatentMethod, HFEPostProcessor (lrzjason), Image Comparer (rgthree), ImageColorMatchAdobe+, ImageListToImageBatch, ImagePadForOutpaint, ImagePadKJ, ImageResizeKJv2, ImageScaleBy, ImageUpscaleWithModel, ImpactInt, KSampler, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, ModelMemoryUsageFactorOverride, ModelPatchLoader, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, QwenImageDiffsynthControlnet, RHHiddenNodes, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, ShowText|pysssss, SimpleMath+, TTP_Image_Assy, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, Upscale Model Loader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, VRAM_Debug, easy anythingIndexSwitch, easy cleanGpuUsed, easy imageBatchToImageList, easy imageSize, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 生图 改图 局部重绘 动作迁移电影肖像换装洗图扩图 工作流合集_2064037868850475010.json, 图片生成/图生图/Qwen Edit 生图 改图 局部重绘 动作迁移电影肖像换装洗图扩图 工作流合集_2076957850185850882.json, 图片生成/图生图/Qwen_Edit_生图_改图_局部重绘_动作迁移电影肖像换装洗图扩图_工作流合集_2072125997440397314.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 生图 改图 局部重绘 动作迁移电影肖像换装洗图扩图 工作流合集_2064037868850475010.json、图片生成/图生图/Qwen Edit 生图 改图 局部重绘 动作迁移电影肖像换装洗图扩图 工作流合集_2076957850185850882.json、图片生成/图生图/Qwen_Edit_生图_改图_局部重绘_动作迁移电影肖像换装洗图扩图_工作流合集_2072125997440397314.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Conditioning Input Switch`
- `CR Latent Input Switch`
- `CR Model Input Switch`
- `CR SDXL Aspect Ratio`
- `CR Text`
- `CR Text Concatenate`
- `CannyEdgePreprocessor`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DWPreprocessor`
- `DepthAnythingV2Preprocessor`
- `DrawMaskOnImage`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `FluxKontextMultiReferenceLatentMethod`
- `HFEPostProcessor (lrzjason)`
- `Image Comparer (rgthree)`
- `ImageColorMatchAdobe+`
- `ImageListToImageBatch`
- `ImagePadForOutpaint`
- `ImagePadKJ`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelMemoryUsageFactorOverride`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `RHHiddenNodes`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `VRAM_Debug`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: NumberCalculatorV2` —— 1/3 个有
- `TTP_Image_Tile_Batch` —— 1/3 个有
- `TTP_Tile_image_size` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 3 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1536 | 1536 - 1536 | 3 | 100% |
| 高度 | 2048 | 2048 - 2048 | 3 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 33/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，3 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，观测区间 2048 - 2048，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（33/3 个样本）：Steps较低可能导致细节不足
