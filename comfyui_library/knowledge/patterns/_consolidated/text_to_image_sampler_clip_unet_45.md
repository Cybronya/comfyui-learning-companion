---
name: text_to_image_sampler_clip_unet_45
type: Text To Image
frequency: 9
level: moderate
coverage: 0.879889
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [PortraitMaster_中文版, Text Multiline, LayerUtility: PurgeVRAM V2]
members: [图片生成/文生图/1924680451447771137.json, 图片生成/文生图/1930451421953691649.json, 图片生成/文生图/1934106744388018178.json, 图片生成/文生图/1935524742722158593.json, 图片生成/文生图/1946760909358555137.json, 图片生成/文生图/1951065960218304513.json, 图片生成/文生图/1951153128769040386.json, 图片生成/文生图/1951218791621570562.json, 图片生成/文生图/1953481264051441666.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_45

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1924680451447771137.json、图片生成/文生图/1930451421953691649.json、图片生成/文生图/1934106744388018178.json、图片生成/文生图/1935524742722158593.json、图片生成/文生图/1946760909358555137.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `RH_Translator` —— 5/9 个有
- `Text Multiline` —— 5/9 个有
- `FluxGuidance` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `ApplyFBCacheAndSkipBlocks` —— 1/9 个有
- `DeepTranslatorTextNode` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `PMRF` —— 1/9 个有
- `PortraitMaster_中文版` —— 1/9 个有
- `TeaCache` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 9 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 9 | 39% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 0.8 - 1 | 9 | 94% |
| 宽度 | 1024 | 512 - 1280 | 9 | 71% |
| 高度 | 1280 | 512 - 1920 | 9 | 61% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，9 个样本，取值集中（一致性 94%）
- 宽度 中位数 1024，观测区间 512 - 1280，9 个样本
- 高度 中位数 1280，观测区间 512 - 1920，9 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：PortraitMaster_中文版、Text Multiline、LayerUtility: PurgeVRAM V2
