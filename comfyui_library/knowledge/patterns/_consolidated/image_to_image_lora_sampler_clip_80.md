---
name: image_to_image_lora_sampler_clip_80
type: Image To Image
frequency: 4
level: strong
coverage: 0.8695
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, FluxGuidance, Image Comparer (rgthree), ImpactInt, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/首饰_珠宝_2056753455921975297.json, 图片生成/图生图/首饰草图转换首饰草图转换V1.0_2094360265574928385.json, 图片生成/文生图/空白工作流_2088539683264483329.json, 数字人/数字人/空白工作流_2088544556475305986.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_80

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/首饰_珠宝_2056753455921975297.json、图片生成/图生图/首饰草图转换首饰草图转换V1.0_2094360265574928385.json、图片生成/文生图/空白工作流_2088539683264483329.json、数字人/数字人/空白工作流_2088544556475305986.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `JjkText`
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
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `Float` —— 3/4 个有
- `GrowMask` —— 1/4 个有
- `InvertMask` —— 1/4 个有
- `JoinImageWithAlpha` —— 1/4 个有
- `LayerMask: BiRefNetUltraV2` —— 1/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
