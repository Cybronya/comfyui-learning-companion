---
name: text_to_image_lora_sampler_clip_450
type: Text To Image
frequency: 4
level: strong
coverage: 0.57525
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetNode, ImageSmartSharpen+, ImpactSwitch, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, SetNode, SubtitleTextProcessor, Text, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy promptLine, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image base 基础文生图_图生图 合一 洗图 lora适配版 -v2_2017843148638130177.json, 图片生成/文生图/z-image turbo 基础文生图_图生图 合一 洗图 lora适配版 -v2_2017843268234514434.json, 图片生成/文生图/🈚️Qwen 2512+z-image 基础+文生图_图生图重绘+反推-洗图_2017843132049657858.json, 图片生成/文生图/🈚️造相 Z-image 文生图+返推 基础_1994015105614544897.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_450

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/z-image base 基础文生图_图生图 合一 洗图 lora适配版 -v2_2017843148638130177.json、图片生成/文生图/z-image turbo 基础文生图_图生图 合一 洗图 lora适配版 -v2_2017843268234514434.json、图片生成/文生图/🈚️Qwen 2512+z-image 基础+文生图_图生图重绘+反推-洗图_2017843132049657858.json、图片生成/文生图/🈚️造相 Z-image 文生图+返推 基础_1994015105614544897.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `ImageSmartSharpen+`
- `ImpactSwitch`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetNode`
- `SubtitleTextProcessor`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy promptLine`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 3/4 个有
- `Float` —— 3/4 个有
- `LatentPixelScale` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `MuterSwitcher` —— 3/4 个有
- `RebatchLatents` —— 3/4 个有
- `RepeatLatentBatch` —— 3/4 个有
- `SeedVarianceEnhancer` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `easy boolean` —— 3/4 个有
- `LayerUtility: TextJoin` —— 2/4 个有
- `BasicScheduler` —— 1/4 个有
- `CFGNorm` —— 1/4 个有
- `DetailDaemonSamplerNode` —— 1/4 个有
- `KSamplerSelect` —— 1/4 个有
- `LatentFrequencyEnhancer_lrzjason` —— 1/4 个有
- `LayerFilter: FilmV2` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SamplerCustom` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 4 | 100% |
| 高度 | 1920 | 1920 - 1920 | 4 | 100% |
| 采样步数 | 6 | 4 - 8 | 4 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | kl_optimal | - | 4 | 50% |
| 重绘幅度 | 0.65 | 0.35 - 1 | 4 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 kl_optimal，4 个样本，一致性 50%
- 重绘幅度 中位数 0.65，观测区间 0.35 - 1，4 个样本
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
