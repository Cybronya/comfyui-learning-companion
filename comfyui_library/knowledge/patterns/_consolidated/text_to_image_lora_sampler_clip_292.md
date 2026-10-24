---
name: text_to_image_lora_sampler_clip_292
type: Text To Image
frequency: 6
level: strong
coverage: 0.896333
common_nodes: [CFGGuider, CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein 9B图像编辑+Lora-单图 浮云2.9_2020706923749842945.json, 图片生成/图生图/Flux2 Klein 9B图像编辑对比-单图 浮云2.7_2017520141579325442.json, 图片生成/图生图/Flux2 Klein 图像编辑对比-单图_2012134645369933826.json, 图片生成/图生图/Flux2 Klein 图像编辑对比-多图_2012149655513075714.json, 图片生成/图生图/千问2511 图像编辑对比-单图 浮云2.7_2020065708322856962.json, 图片生成/文生图/Flux2-Klein文生图_单图编辑_多图融合工作流合集_2014665385068466178.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_292

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 9B图像编辑+Lora-单图 浮云2.9_2020706923749842945.json、图片生成/图生图/Flux2 Klein 9B图像编辑对比-单图 浮云2.7_2017520141579325442.json、图片生成/图生图/Flux2 Klein 图像编辑对比-单图_2012134645369933826.json、图片生成/图生图/Flux2 Klein 图像编辑对比-多图_2012149655513075714.json、图片生成/图生图/千问2511 图像编辑对比-单图 浮云2.7_2020065708322856962.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 5/6 个有
- `FluxResolutionNode` —— 5/6 个有
- `ImpactInt` —— 5/6 个有
- `ImpactSwitch` —— 5/6 个有
- `KOOK_ImageCompression` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `TextEncodeQwenImageEditPlus` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `LayerUtility: PurgeVRAM` —— 3/6 个有
- `ImageConcanate` —— 2/6 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 616 | 512 - 720 | 6 | 83% |
| 高度 | 896 | 512 - 1280 | 6 | 57% |
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 616，观测区间 512 - 720，6 个样本，取值集中（一致性 83%）
- 高度 中位数 896，观测区间 512 - 1280，6 个样本
- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
