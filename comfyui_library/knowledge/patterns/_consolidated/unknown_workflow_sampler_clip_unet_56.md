---
name: unknown_workflow_sampler_clip_unet_56
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.931
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-rebalance文生图_1999689524483682305.json, 图片生成/文生图/QwenImage 8步 蒸馏加速工作流_1954589330377469954.json, 图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2084844216345251842.json, 图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2084906463855726594.json, 图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2087826566675001345.json, 图片生成/文生图/QwenImage Comfyui官方工作流_1952820714467487746.json, 图片生成/文生图/QwenImage Comfyui官方工作流_1952877428207194113.json, 图片生成/文生图/QwenImage+8步+蒸馏加速工作流_2015669597445300226.json, 图片生成/文生图/QwenImage千问文生图4步加速放大工作流_1955919657263923201.json, 图片生成/文生图/Z-image Base Distilled蒸馏加速版_2019063606171668481.json, 图片生成/文生图/Z-image Tubro文生图工作流，没有AI味的模型！_2061058146243801090.json, 图片生成/文生图/Z-image 文生图_2017213414262710273.json, 图片生成/文生图/Zimage图片加速生成（Zimage Quick Text-to-Image Generatio）_2029019962836258817.json, 图片生成/文生图/工作流基础系列4-z image turbo文生图工作流-基础向讲解此工作流_2044389426284990466.json, 图片生成/文生图/组件系列6-Z-image-turbo文生图_2058749993380569090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_56

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Qwen-rebalance文生图_1999689524483682305.json、图片生成/文生图/QwenImage 8步 蒸馏加速工作流_1954589330377469954.json、图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2084844216345251842.json、图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2084906463855726594.json、图片生成/文生图/QwenImage 8步 蒸馏加速工作流_2087826566675001345.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 14/15 个有
- `LoraLoaderModelOnly` —— 13/15 个有
- `ConditioningZeroOut` —— 12/15 个有
- `PreviewImage` —— 6/15 个有
- `CR Prompt Text` —— 4/15 个有
- `easy promptList` —— 3/15 个有
- `Seed (rgthree)` —— 2/15 个有
- `CR Upscale Image` —— 1/15 个有
- `EmptyZImageLatentImage //ZImagePowerNodes` —— 1/15 个有
- `ImpactInt` —— 1/15 个有
- `PrimitiveFloat` —— 1/15 个有
- `StringFunction|pysssss` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 15 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 15 | 58% |
| 采样算法 | euler | - | 15 | 73% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，15 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 73%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（11/15 个样本）：Steps较低可能导致细节不足
