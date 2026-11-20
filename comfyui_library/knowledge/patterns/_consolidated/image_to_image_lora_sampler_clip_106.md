---
name: image_to_image_lora_sampler_clip_106
type: Image To Image
frequency: 3
level: strong
coverage: 0.922333
common_nodes: [CFGGuider, CFGNorm, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/分镜 自动分镜  短剧分镜 漫剧分镜_2095774817839575042.json, 图片生成/图生图/无遮挡电商产品图_2038156576611115010.json, 图片生成/图生图/有遮挡电商产品图_2038159479967059970.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_106

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/分镜 自动分镜  短剧分镜 漫剧分镜_2095774817839575042.json、图片生成/图生图/无遮挡电商产品图_2038156576611115010.json、图片生成/图生图/有遮挡电商产品图_2038159479967059970.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorPickerMW` —— 2/3 个有
- `DF_Get_image_size` —— 2/3 个有
- `FillMaskWithColor` —— 2/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `InvertMask` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/3 个有
- `LayerUtility: CropByMask V3` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `LayerUtility: RestoreCropBox` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `BiRefNetRMBG` —— 1/3 个有
- `Int` —— 1/3 个有
- `JDCN_StringToList` —— 1/3 个有
- `LayerUtility: ImageBlendAdvance V3` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `ProcessString` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `Switch` —— 1/3 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 3 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta57 | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，3 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta57，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
