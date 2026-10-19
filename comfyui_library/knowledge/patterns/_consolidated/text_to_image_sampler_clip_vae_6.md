---
name: text_to_image_sampler_clip_vae_6
type: Text To Image
frequency: 3
level: strong
coverage: 0.660333
common_nodes: [CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImpactSwitch, Int, KSampler, LoadImage, RH_Captioner, RH_Translator, RepeatLatentBatch, SaveImage, VAEDecode, VAELoader, easy imageSize, easy showAnything]
problems: []
missing: [CR SDXL Aspect Ratio, easy imageSize]
members: [图片生成/文生图/1951091937367498754.json, 图片生成/文生图/1951212723730325505.json, 图片生成/文生图/1956161644252549122.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1951091937367498754.json、图片生成/文生图/1951212723730325505.json、图片生成/文生图/1956161644252549122.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LoadImage`
- `RH_Captioner`
- `RH_Translator`
- `RepeatLatentBatch`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `easy ifElse` —— 2/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `NunchakuFluxLoraLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR SDXL Aspect Ratio、easy imageSize
