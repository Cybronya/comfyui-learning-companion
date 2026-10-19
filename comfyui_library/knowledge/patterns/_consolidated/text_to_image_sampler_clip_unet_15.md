---
name: text_to_image_sampler_clip_unet_15
type: Text To Image
frequency: 5
level: strong
coverage: 0.8884
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, ImpactSwitch, Int, KSampler, ModelSamplingAuraFlow, PrimitiveString, RHHiddenNodes, SaveImage, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy int]
problems: []
missing: []
members: [图片生成/文生图/人物模特生成-智能提示词版_1982988891378581505.json, 图片生成/文生图/人物模特生成-智能提示词版_2103298288773591042.json, 图片生成/文生图/人物模特生成-智能提示词版_2103666446302797825.json, 图片生成/文生图/人物模特生成-智能提示词版_2104489691142774785.json, 图片生成/文生图/人物模特生成-智能提示词版_2104848974585876481.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_15

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/人物模特生成-智能提示词版_1982988891378581505.json、图片生成/文生图/人物模特生成-智能提示词版_2103298288773591042.json、图片生成/文生图/人物模特生成-智能提示词版_2103666446302797825.json、图片生成/文生图/人物模特生成-智能提示词版_2104489691142774785.json、图片生成/文生图/人物模特生成-智能提示词版_2104848974585876481.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PrimitiveString`
- `RHHiddenNodes`
- `SaveImage`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 5 | 100% |
| 高度 | 512 | 512 - 512 | 5 | 100% |
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 5 | 100% |
| 采样算法 | res_2m | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
