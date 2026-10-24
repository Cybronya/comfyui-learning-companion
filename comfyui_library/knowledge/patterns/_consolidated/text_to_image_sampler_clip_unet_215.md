---
name: text_to_image_sampler_clip_unet_215
type: Text To Image
frequency: 2
level: weak
coverage: 0.83
common_nodes: [CLIPTextEncode, CR Text, ConditioningZeroOut, DeepTranslatorTextNode, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QT103-文生图（FLUX）基础文生图，一键轻松图_1946954032549769218.json, 图片生成/文生图/宝宝版 文生图_2009166166715011074.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_215

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/QT103-文生图（FLUX）基础文生图，一键轻松图_1946954032549769218.json、图片生成/文生图/宝宝版 文生图_2009166166715011074.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `easy positive` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1264 | - | 2 | 81% |
| 高度 | 764 | - | 2 | 66% |
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1264，样本不足，未给区间，2 个样本，取值集中（一致性 81%）
- 高度 中位数 764，样本不足，未给区间，2 个样本
- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
