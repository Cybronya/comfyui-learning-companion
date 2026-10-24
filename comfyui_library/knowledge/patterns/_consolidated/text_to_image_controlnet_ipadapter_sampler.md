---
name: text_to_image_controlnet_ipadapter_sampler
type: Text To Image
frequency: 3
level: strong
coverage: 0.863
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, Get Image Size, IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageScaleBy, ImpactSwitch, Int, JjkText, KSampler, LoadImage, RH_Translator, SaveImage, ShowText|pysssss, Text Multiline, VAEDecode, easy float, easy int, easy promptConcat, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/方案演变XL_1926992697335173122.json, 图片生成/图生图/模拟风格进行线条上色V2_2045037824377884674.json, 图片生成/图生图/线稿上色_草绘上色_2036798855878021121.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_sampler

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/方案演变XL_1926992697335173122.json、图片生成/图生图/模拟风格进行线条上色V2_2045037824377884674.json、图片生成/图生图/线稿上色_草绘上色_2036798855878021121.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `Get Image Size`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageScaleBy`
- `ImpactSwitch`
- `Int`
- `JjkText`
- `KSampler`
- `LoadImage`
- `RH_Translator`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `VAEDecode`
- `easy float`
- `easy int`
- `easy promptConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Filter Adjustments` —— 2/3 个有
- `ImageInvert` —— 2/3 个有
- `easy imageIndexSwitch` —— 2/3 个有
- `CannyEdgePreprocessor` —— 1/3 个有
- `IPAdapterStyleComposition` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 1344 | 1344 - 1344 | 3 | 100% |
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 2 | 2 - 2 | 3 | 100% |
| 采样算法 | dpmpp_sde | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | 0.7 - 1 | 3 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1344，观测区间 1344 - 1344，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 0.7 - 1，3 个样本，取值集中（一致性 84%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
