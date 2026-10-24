---
name: unknown_workflow_sampler_clip_vae_47
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7156
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPTextEncode, ConditioningZeroOut, DeepTranslatorTextNode, KSampler (Efficient), LayerFilter: HDREffects, ModelSamplingFlux, SaveImage, ShowText|pysssss, StringFunction|pysssss, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux.1 Krea Dev Nunchaku 文生图新人必备_1952287898248884225.json, 图片生成/文生图/Flux.1 Krea Dev Nunchaku图生图  新人必备_1952289860134621185.json, 图片生成/文生图/Flux.1 Krea Dev 普通版图生图  新人必备_1952283213253259265.json, 图片生成/文生图/Flux.1 Krea Dev 普通版文生图 新人必备_1952280309612097537.json, 图片生成/文生图/Nunchaku  极速文生图 反推_1936638938712821762.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_47

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Flux.1 Krea Dev Nunchaku 文生图新人必备_1952287898248884225.json、图片生成/文生图/Flux.1 Krea Dev Nunchaku图生图  新人必备_1952289860134621185.json、图片生成/文生图/Flux.1 Krea Dev 普通版图生图  新人必备_1952283213253259265.json、图片生成/文生图/Flux.1 Krea Dev 普通版文生图 新人必备_1952280309612097537.json、图片生成/文生图/Nunchaku  极速文生图 反推_1936638938712821762.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `ModelSamplingFlux`
- `SaveImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Seed Everywhere` —— 4/5 个有
- `EmptyLatentImage` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `NunchakuFluxDiTLoader` —— 3/5 个有
- `NunchakuTextEncoderLoaderV2` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `DualCLIPLoader` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `NunchakuFluxLoraLoader` —— 2/5 个有
- `UNETLoader` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `GetImageSize+` —— 1/5 个有
- `JJC_JoyCaption` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 800 | 800 - 1024 | 3 | 88% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 30 | 20 - 30 | 5 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 60% |
| 重绘幅度 | 1 | 0.7 - 1 | 5 | 87% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 800，观测区间 800 - 1024，3 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 20 - 30，5 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，5 个样本，取值集中（一致性 87%）
