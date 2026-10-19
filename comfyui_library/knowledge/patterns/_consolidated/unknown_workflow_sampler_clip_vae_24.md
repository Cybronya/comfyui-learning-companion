---
name: unknown_workflow_sampler_clip_vae_24
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.536667
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPTextEncode, ConditioningZeroOut, DeepTranslatorTextNode, KSampler (Efficient), LayerFilter: HDREffects, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuTextEncoderLoaderV2, SaveImage, ShowText|pysssss, StringFunction|pysssss, VAELoader]
problems: []
missing: [LayerFilter: HDREffects, LayerUtility: PurgeVRAM V2, StringFunction|pysssss, KSampler (Efficient), GetImageSize+, Seed Everywhere]
members: [图片生成/文生图/1936638938712821762.json, 图片生成/文生图/1952287898248884225.json, 图片生成/文生图/1952289860134621185.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1936638938712821762.json、图片生成/文生图/1952287898248884225.json、图片生成/文生图/1952289860134621185.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoaderV2`
- `SaveImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `NunchakuFluxLoraLoader` —— 2/3 个有
- `Seed Everywhere` —— 2/3 个有
- `GetImageSize+` —— 1/3 个有
- `JJC_JoyCaption` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 0.7 - 1 | 3 | 84% |
| 宽度 | 912 | - | 2 | 88% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，3 个样本，取值集中（一致性 84%）
- 宽度 中位数 912，样本不足，未给区间，2 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerFilter: HDREffects、LayerUtility: PurgeVRAM V2、StringFunction|pysssss、KSampler (Efficient)、GetImageSize+
