---
name: text_to_image_sampler_clip_unet_114
type: Text To Image
frequency: 6
level: moderate
coverage: 0.8615
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LatentColorMatchSimple, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2文生图+高清修复_2072870114332078081.json, 图片生成/文生图/Krea2 高清放大修复_2070642369757798402.json, 图片生成/文生图/Krea2-文生图-高清2K【30秒】出图_2074665064451366914.json, 图片生成/文生图/Krea2 写实人像_2071577267242885122.json, 图片生成/文生图/krea2文生图+高清修复_2072118286560612353.json, 图片生成/文生图/krea2文生图+高清修复_2072866898324316162.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_114

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/krea2文生图+高清修复_2072870114332078081.json、图片生成/文生图/Krea2 高清放大修复_2070642369757798402.json、图片生成/文生图/Krea2-文生图-高清2K【30秒】出图_2074665064451366914.json、图片生成/文生图/Krea2 写实人像_2071577267242885122.json、图片生成/文生图/krea2文生图+高清修复_2072118286560612353.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LatentColorMatchSimple`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `Text Concatenate` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `CR Text` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `CLIPLoaderGGUF` —— 1/6 个有
- `ConditioningKrea2Rebalance` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `ttN concat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1280 | 6 | 55% |
| 高度 | 768 | 720 - 768 | 6 | 98% |
| 采样步数 | 6 | 5 - 6 | 6 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 1 | 6 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1280，6 个样本
- 高度 中位数 768，观测区间 720 - 768，6 个样本，取值集中（一致性 98%）
- 采样步数 中位数 6，观测区间 5 - 6，6 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 1，6 个样本
- 高发问题（13/6 个样本）：Steps较低可能导致细节不足
