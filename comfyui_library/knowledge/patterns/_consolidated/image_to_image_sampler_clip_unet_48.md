---
name: image_to_image_sampler_clip_unet_48
type: Image To Image
frequency: 8
level: strong
coverage: 0.986375
common_nodes: [CLIPTextEncode, CR Text, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, Int, KSampler, LoadImage, PlaySound|pysssss, RH_LLMAPI_NODE, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy convertAnything, easy positive, easy promptLine, ttN concat]
problems: []
missing: []
members: [图片生成/图生图/QY5-千姿引擎，一张图秒变多姿态，千姿百态，电商、模特、服装_1951936959017111554.json, 图片生成/图生图/QY5-千姿引擎，一张图秒变多姿态，千姿百态，电商、模特、服装_1971033497114710017.json, 图片生成/图生图/QY5-千姿引擎，一张图秒变多姿态，千姿百态，电商、模特、服装_1993199712522223618.json, 图片生成/图生图/QY5-千姿引擎，多姿态，千姿百态，电商、模特、服装（适合人物）_1983459384355397634.json, 图片生成/图生图/电商、模特、服装_1图千姿百态_1993244079171502081.json, 图片生成/图生图/西洲 QY5-千姿引擎，一张图秒变多姿态，千姿百态，电商、模特、服装_1975052976186372097.json, 图片生成/文生图/QY5-千姿引擎，一张图秒变多姿态，千姿百态，电商、模特、服装_1961972929053528066.json, 数字人/数字人/一张图秒变多姿态 人物一致多角度  美女模特人物服装不同视角展示 IP角色创建 电商、模特_1969590303055355905.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_48

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/QY5-千姿引擎，一张图秒变多姿态，千姿百态，电商、模特、服装_1951936959017111554.json、图片生成/图生图/QY5-千姿引擎，一张图秒变多姿态，千姿百态，电商、模特、服装_1971033497114710017.json、图片生成/图生图/QY5-千姿引擎，一张图秒变多姿态，千姿百态，电商、模特、服装_1993199712522223618.json、图片生成/图生图/QY5-千姿引擎，多姿态，千姿百态，电商、模特、服装（适合人物）_1983459384355397634.json、图片生成/图生图/电商、模特、服装_1图千姿百态_1993244079171502081.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Int`
- `KSampler`
- `LoadImage`
- `PlaySound|pysssss`
- `RH_LLMAPI_NODE`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy convertAnything`
- `easy positive`
- `easy promptLine`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `easy bookmark` —— 5/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 28 - 28 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 28 - 28，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
