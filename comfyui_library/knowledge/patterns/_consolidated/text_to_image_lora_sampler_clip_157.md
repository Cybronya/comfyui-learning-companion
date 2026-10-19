---
name: text_to_image_lora_sampler_clip_157
type: Text To Image
frequency: 6
level: weak
coverage: 0.882333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108431762991964161.json, 数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108886341202300929.json, 数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108891627866640386.json, 数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109018096492175361.json, 数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109414860994994177.json, 视频生成/图生视频/Flux2Klein多图编辑9B加速版｜换脸换装都顺手｜图生视频前处理首选_2102632847407407106.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_157

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108431762991964161.json、数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108886341202300929.json、数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108891627866640386.json、数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109018096492175361.json、数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109414860994994177.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSampler`
- `KSamplerSelect`
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

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 5/6 个有
- `ConditioningZeroOut` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `ImageSharpen` —— 5/6 个有
- `PreviewAny` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `QwenImagePromptOptimizer` —— 5/6 个有
- `QwenImagePromptStyler` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `JjkText` —— 3/6 个有
- `solarL_SaveImagesToZip` —— 3/6 个有
- `孤海注释` —— 3/6 个有
- `CR Text` —— 1/6 个有
- `Int` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1064 | 80 - 2048 | 6 | 8% |
| 高度 | 1064 | 80 - 2048 | 6 | 8% |
| 采样步数 | 17 | 4 - 30 | 6 | 24% |
| Prompt 约束强度(CFG) | 3.25 | 2 - 4.5 | 6 | 62% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1064，观测区间 80 - 2048，6 个样本，取值分散，一致性仅 8%
- 高度 中位数 1064，观测区间 80 - 2048，6 个样本，取值分散，一致性仅 8%
- 采样步数 中位数 17，观测区间 4 - 30，6 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 3.25，观测区间 2 - 4.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
