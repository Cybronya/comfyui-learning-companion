---
name: text_to_image_sampler_clip_unet_170
type: Text To Image
frequency: 4
level: moderate
coverage: 0.931
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/qwencosplayxzcc1_2024847980452384769.json, 图片生成/文生图/qwencosplayxzcc_2024843582259077122.json, 图片生成/文生图/墨沫深空krea2-RAW 工作流_2077060951261671426.json, 图片生成/文生图/自用场景设计_2016786512226029569.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_170

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/qwencosplayxzcc1_2024847980452384769.json、图片生成/文生图/qwencosplayxzcc_2024843582259077122.json、图片生成/文生图/墨沫深空krea2-RAW 工作流_2077060951261671426.json、图片生成/文生图/自用场景设计_2016786512226029569.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `easy int` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `SaveLatent` —— 2/4 个有
- `ZML_ImageEncryption` —— 2/4 个有
- `ImpactSwitch` —— 1/4 个有
- `Int` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `TTResolutionSelector` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 4 | 84% |
| Prompt 约束强度(CFG) | 3.75 | 1 - 5 | 4 | 49% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | sgm_uniform | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 768 | 512 - 1200 | 4 | 62% |
| 高度 | 768 | 512 - 1200 | 4 | 62% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 3.75，观测区间 1 - 5，4 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 1200，4 个样本
- 高度 中位数 768，观测区间 512 - 1200，4 个样本
