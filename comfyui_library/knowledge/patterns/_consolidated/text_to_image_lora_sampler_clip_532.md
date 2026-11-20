---
name: text_to_image_lora_sampler_clip_532
type: Text To Image
frequency: 3
level: strong
coverage: 0.901667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/灯光优化图生图工作流，改善人像与产品光影效果_2102874032126382081.json, 图片生成/图生图/超强一致性全能编辑｜Flux2+Klein9b换装换背景_2092943005975146497.json, 视频生成/图生视频/灯光优化图生图工作流，改善人像与产品光影效果_2105124719635812353.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_532

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/灯光优化图生图工作流，改善人像与产品光影效果_2102874032126382081.json、图片生成/图生图/超强一致性全能编辑｜Flux2+Klein9b换装换背景_2092943005975146497.json、视频生成/图生视频/灯光优化图生图工作流，改善人像与产品光影效果_2105124719635812353.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PainterFluxImageEdit` —— 2/3 个有
- `RH_LLMAPI_Pro_Node` —— 2/3 个有
- `RH_RhartImageG25SunburstImageToImage` —— 2/3 个有
- `SphereLightNode` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `Int` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（7/3 个样本）：Steps较低可能导致细节不足
