---
name: text_to_image_controlnet_upscale_lora_9
type: Text To Image
frequency: 3
level: moderate
coverage: 0.485667
common_nodes: [BasicGuider, BasicScheduler, BboxDetectorSEGS, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetLoader, DetailerForEach, DualCLIPLoader, EmptyLatentImage, Float, GetNode, Image Comparer (rgthree), ImageResizeKJ, ImpactSegsAndMask, ImpactSwitch, Int, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MaskPreview+, PlaySound|pysssss, PortraitMaster, PreviewImage, RandomNoise, SAMDetectorCombined, SAMLoader, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, TextInput_, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物模特三维视角多角度一致性生成_1909078931130228738.json, 平台全量/FLUX多角度一致性写实人物Pro_ 穿上真实的衣服_1843491534351335425.json, 平台全量/FLUX多角度一致性写实人物__极致写实_1844700718925254658.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人物模特三维视角多角度一致性生成_1909078931130228738.json、平台全量/FLUX多角度一致性写实人物Pro_ 穿上真实的衣服_1843491534351335425.json、平台全量/FLUX多角度一致性写实人物__极致写实_1844700718925254658.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BboxDetectorSEGS`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `DetailerForEach`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Float`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `ImpactSegsAndMask`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PlaySound|pysssss`
- `PortraitMaster`
- `PreviewImage`
- `RandomNoise`
- `SAMDetectorCombined`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `OpenposePreprocessor` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `ApplyPulidFlux` —— 1/3 个有
- `CLIPTextEncodeHunyuanDiT` —— 1/3 个有
- `CR Upscale Image` —— 1/3 个有
- `ControlNetApplySD3` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `DownloadAndLoadFlorence2Model` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `PulidFluxEvaClipLoader` —— 1/3 个有
- `PulidFluxInsightFaceLoader` —— 1/3 个有
- `PulidFluxModelLoader` —— 1/3 个有
- `ReActorFaceBoost` —— 1/3 个有
- `ReActorFaceSwap` —— 1/3 个有
- `TTP_Image_Assy` —— 1/3 个有
- `TTP_Image_Tile_Batch` —— 1/3 个有
- `TTP_Tile_image_size` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有
- `easy imageBatchToImageList` —— 1/3 个有
- `easy imageChooser` —— 1/3 个有
- `easy imageListToImageBatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 0.8 - 1 | 3 | 90% |
| 采样步数 | 4 | 4 - 50 | 3 | 0% |
| Prompt 约束强度(CFG) | 2 | 2 - 6 | 3 | 43% |
| 采样算法 | dpmpp_sde | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 904 | 3 | 71% |
| 高度 | 512 | 512 - 1200 | 3 | 56% |
| LoRA 模型强度 | 0.9 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- 采样步数 中位数 4，观测区间 4 - 50，3 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 6，3 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 904，3 个样本
- 高度 中位数 512，观测区间 512 - 1200，3 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
