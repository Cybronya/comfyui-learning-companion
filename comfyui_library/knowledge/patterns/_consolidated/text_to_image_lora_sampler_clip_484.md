---
name: text_to_image_lora_sampler_clip_484
type: Text To Image
frequency: 4
level: moderate
coverage: 0.895
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/首饰产品精修2k版直出首饰产品精修2k直出2.0 (2)_2094363399160418305.json, 图片生成/文生图/Flux2 klein9b集合_2025390753387651074.json, 平台全量/V3.1首饰产品精修2k版直出_2117911489398001665.json, 平台全量/V3首饰产品精修2k版直出_2117900429366480898.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_484

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/首饰产品精修2k版直出首饰产品精修2k直出2.0 (2)_2094363399160418305.json、图片生成/文生图/Flux2 klein9b集合_2025390753387651074.json、平台全量/V3.1首饰产品精修2k版直出_2117911489398001665.json、平台全量/V3首饰产品精修2k版直出_2117900429366480898.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
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
- `Float` —— 3/4 个有
- `FluxGuidance` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `SeargeIntegerConstant` —— 3/4 个有
- `easy promptConcat` —— 3/4 个有
- `EmptyFlux2LatentImage` —— 1/4 个有
- `GetImageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 4 | 65% |
| 高度 | 512 | 512 - 1024 | 4 | 65% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 4 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，4 个样本
- 高度 中位数 512，观测区间 512 - 1024，4 个样本
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，4 个样本
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
