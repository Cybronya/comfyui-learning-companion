---
name: text_to_image_lora_sampler_clip_402
type: Text To Image
frequency: 5
level: moderate
coverage: 0.7666
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveStringMultiline, SaveImage, SeedNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 Turbo文生图 工作流+全节点注释_2077756477330247682.json, 图片生成/文生图/Krea2 Turbo文生图 工作流+全节点注释_2096069355342749697.json, 图片生成/文生图/Krea2 Turbo文生图（人像增强_低清晰快速版）_2077588064620343297.json, 图片生成/文生图/Krea2+Text-to-Image+(场景增强_低清晰快速版）_2079889659416637442.json, 图片生成/文生图/krea2+klein+zimage高质量生图_2083406223365468162.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_402

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Krea2 Turbo文生图 工作流+全节点注释_2077756477330247682.json、图片生成/文生图/Krea2 Turbo文生图 工作流+全节点注释_2096069355342749697.json、图片生成/文生图/Krea2 Turbo文生图（人像增强_低清晰快速版）_2077588064620343297.json、图片生成/文生图/Krea2+Text-to-Image+(场景增强_低清晰快速版）_2079889659416637442.json、图片生成/文生图/krea2+klein+zimage高质量生图_2083406223365468162.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SeedNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/5 个有
- `QZ_ResolutionPreset` —— 4/5 个有
- `CR Text` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `RHLLMChatNode` —— 2/5 个有
- `LoadImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 10 | 1 - 10 | 5 | 31% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 60% |
| 宽度 | 1024 | 720 - 1024 | 5 | 87% |
| 高度 | 1024 | 1024 - 1280 | 5 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 10，观测区间 1 - 10，5 个样本，取值分散，一致性仅 31%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 60%
- 宽度 中位数 1024，观测区间 720 - 1024，5 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1280，5 个样本，取值集中（一致性 90%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
