---
name: unknown_workflow_sampler_clip_unet_241
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.925
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/基础flux文生图1009_1976073946242093057.json, 图片生成/文生图/大家电场景图2.0_1943614394796568578.json, 图片生成/文生图/大家电场景图_1948667723191595009.json, 图片生成/文生图/室内建筑景观高质感文生图_2067220940961964033.json, 图片生成/文生图/沙雕动漫专用表情包快速生成_2043984326500556801.json, 图片生成/文生图/生成系列性服装设计_1884234765942538241.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_241

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/基础flux文生图1009_1976073946242093057.json、图片生成/文生图/大家电场景图2.0_1943614394796568578.json、图片生成/文生图/大家电场景图_1948667723191595009.json、图片生成/文生图/室内建筑景观高质感文生图_2067220940961964033.json、图片生成/文生图/沙雕动漫专用表情包快速生成_2043984326500556801.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 4/6 个有
- `LoraLoader` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `LoraLoader|pysssss` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 964 | 720 - 2048 | 6 | 61% |
| 高度 | 1392 | 1024 - 1536 | 6 | 87% |
| LoRA 模型强度 | 0.6 | 0.6 - 1 | 3 | 74% |
| LoRA 文本强度 | 1 | 1 - 1.02 | 3 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 964，观测区间 720 - 2048，6 个样本
- 高度 中位数 1392，观测区间 1024 - 1536，6 个样本，取值集中（一致性 87%）
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1.02，3 个样本，取值集中（一致性 99%）
