---
name: text_to_image_sampler_clip_unet_47
type: Text To Image
frequency: 9
level: weak
coverage: 0.838556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, Power Lora Loader (rgthree)]
members: [图片生成/文生图/1955085568910790658.json, 图片生成/文生图/1955863541137985538.json, 图片生成/文生图/1985898941021659137.json, 图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json, 图片生成/文生图/Krea2 Turbo文生图 工作流+全节点注释_2077756477330247682.json, 图片生成/文生图/Krea2 Turbo文生图 工作流+全节点注释_2096069355342749697.json, 图片生成/文生图/Krea2 Turbo文生图（人像增强_低清晰快速版）_2077588064620343297.json, 图片生成/文生图/Krea2+Text-to-Image+(场景增强_低清晰快速版）_2079889659416637442.json, 图片生成/文生图/krea2+klein+zimage高质量生图_2083406223365468162.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_47

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1955085568910790658.json、图片生成/文生图/1955863541137985538.json、图片生成/文生图/1985898941021659137.json、图片生成/文生图/Anima-Base1.0 +Lora 芙莉莲（提示词指南）_2058148244718444546.json、图片生成/文生图/Krea2 Turbo文生图 工作流+全节点注释_2077756477330247682.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 8/9 个有
- `CFGNorm` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `Int` —— 6/9 个有
- `CR Text` —— 5/9 个有
- `ConditioningZeroOut` —— 5/9 个有
- `KSamplerAdvanced` —— 5/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `SeedNode` —— 5/9 个有
- `VAEEncode` —— 5/9 个有
- `QZ_ResolutionPreset` —— 4/9 个有
- `LoadImage` —— 3/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `PreviewAny` —— 2/9 个有
- `RHLLMChatNode` —— 2/9 个有
- `EmptySD3LatentImage` —— 1/9 个有
- `FluxResolutionNode` —— 1/9 个有
- `Power Lora Loader (rgthree)` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1024 | 9 | 88% |
| 高度 | 1024 | 1024 - 1368 | 9 | 88% |
| 采样步数 | 10 | 4 - 30 | 6 | 25% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 10 | 9 | 14% |
| 采样算法 | euler | - | 9 | 44% |
| 调度器 | simple | - | 9 | 44% |
| 重绘幅度 | 1 | 0.25 - 1 | 6 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1024，9 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 1368，9 个样本，取值集中（一致性 88%）
- 采样步数 中位数 10，观测区间 4 - 30，6 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 10，9 个样本，取值分散，一致性仅 14%
- 采样算法 最常用 euler，9 个样本，一致性 44%
- 调度器 最常用 simple，9 个样本，一致性 44%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，6 个样本
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Power Lora Loader (rgthree)
