---
name: text_to_image_sampler_clip_unet_214
type: Text To Image
frequency: 3
level: moderate
coverage: 0.908
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, Text Concatenate, UNETLoader, VAEDecode, VAELoader, easy int, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/qwencosplayxzcc1_2024847980452384769.json, 图片生成/文生图/qwencosplayxzcc_2024843582259077122.json, 图片生成/文生图/自用场景设计_2016786512226029569.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_214

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/qwencosplayxzcc1_2024847980452384769.json、图片生成/文生图/qwencosplayxzcc_2024843582259077122.json、图片生成/文生图/自用场景设计_2016786512226029569.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `SaveLatent` —— 2/3 个有
- `ZML_ImageEncryption` —— 2/3 个有
- `ImpactSwitch` —— 1/3 个有
- `Int` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 5 | 2.5 - 5 | 3 | 72% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 512 - 1200 | 3 | 68% |
| 高度 | 1024 | 512 - 1200 | 3 | 68% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 2.5 - 5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1200，3 个样本
- 高度 中位数 1024，观测区间 512 - 1200，3 个样本
