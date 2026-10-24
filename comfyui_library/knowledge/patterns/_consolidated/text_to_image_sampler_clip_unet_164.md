---
name: text_to_image_sampler_clip_unet_164
type: Text To Image
frequency: 4
level: moderate
coverage: 0.931
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/qwencosplayxzcc1_2024847980452384769.json, 图片生成/文生图/qwencosplayxzcc_2024843582259077122.json, 图片生成/文生图/z-image-turbo flow dpo版文生图 自用_2050564898463207426.json, 图片生成/文生图/自用场景设计_2016786512226029569.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_164

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/qwencosplayxzcc1_2024847980452384769.json、图片生成/文生图/qwencosplayxzcc_2024843582259077122.json、图片生成/文生图/z-image-turbo flow dpo版文生图 自用_2050564898463207426.json、图片生成/文生图/自用场景设计_2016786512226029569.json）

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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `ZML_ImageEncryption` —— 3/4 个有
- `easy int` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `SaveLatent` —— 2/4 个有
- `HAIGC_SaveImagesToZip` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `Int` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 10 - 30 | 4 | 63% |
| Prompt 约束强度(CFG) | 3.75 | 1 - 5 | 4 | 49% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | sgm_uniform | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 896 | 512 - 1200 | 4 | 70% |
| 高度 | 1024 | 512 - 1200 | 4 | 73% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 10 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 3.75，观测区间 1 - 5，4 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 512 - 1200，4 个样本
- 高度 中位数 1024，观测区间 512 - 1200，4 个样本
