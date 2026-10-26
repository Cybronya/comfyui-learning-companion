---
name: image_to_image_lora_sampler_clip_50
type: Image To Image
frequency: 6
level: moderate
coverage: 0.939167
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, FluxGuidance, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键毛坯房装修 + Flux Kontext_1966186173439930370.json, 图片生成/图生图/一键毛坯房装修 + Flux Kontext_1966332345303412738.json, 图片生成/图生图/一键毛坯房装修 flux kontext_1955862682740117506.json, 图片生成/图生图/一键毛坯房装修+flux+kontext_1955905403399929858.json, 图片生成/图生图/去ai感-人像精修_2102231252593102849.json, 图片生成/图生图/家装2_1960273426332200961.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/一键毛坯房装修 + Flux Kontext_1966186173439930370.json、图片生成/图生图/一键毛坯房装修 + Flux Kontext_1966332345303412738.json、图片生成/图生图/一键毛坯房装修 flux kontext_1955862682740117506.json、图片生成/图生图/一键毛坯房装修+flux+kontext_1955905403399929858.json、图片生成/图生图/去ai感-人像精修_2102231252593102849.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `easy imageConcat` —— 5/6 个有
- `CR Simple Text Watermark` —— 2/6 个有
- `EmptyFlux2LatentImage` —— 1/6 个有
- `SeedVR2` —— 1/6 个有
- `SeedVR2BlockSwap` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 6 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | uni_pc | - | 6 | 83% |
| 调度器 | beta | - | 6 | 83% |
| 重绘幅度 | 0.2 | 0.2 - 1 | 6 | 11% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 83%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 1，6 个样本，取值分散，一致性仅 11%
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
