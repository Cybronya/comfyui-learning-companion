---
name: image_to_image_lora_sampler_clip_91
type: Image To Image
frequency: 3
level: moderate
coverage: 0.905
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageConcanate, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux_Krea真人洗图_1958462222928343041.json, 图片生成/图生图/Flux_Krea真人洗图_2072206265215971330.json, 图片生成/图生图/喜怒哀乐表情包_1949755739474714626.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_91

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux_Krea真人洗图_1958462222928343041.json、图片生成/图生图/Flux_Krea真人洗图_2072206265215971330.json、图片生成/图生图/喜怒哀乐表情包_1949755739474714626.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DisplayText` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `Qwen2.5VL` —— 2/3 个有
- `RepeatLatentBatch` —— 2/3 个有
- `WD14Tagger|pysssss` —— 2/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 30 | 3 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.7 | 0.7 - 1 | 3 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.7 - 1，3 个样本，取值集中（一致性 82%）
