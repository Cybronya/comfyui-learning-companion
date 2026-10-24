---
name: unknown_workflow_sampler_clip_unet_142
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.871875
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI试戴美甲-穿戴甲换甲工作流_2094418586373804033.json, 图片生成/图生图/Flux 3_Image_Klein开源版-多图参考生图_2111065019705286658.json, 图片生成/图生图/MOSS图生图2K极速版!_2112529861960101890.json, 图片生成/图生图/MOSS图生图2K极速版_2112543696460804097.json, 图片生成/图生图/MOSS图生图2K极速版_2112855505784893441.json, 图片生成/图生图/Moss-image-文生图（8步加速）_2112146425906814977.json, 图片生成/图生图/Moss-image-文生图（提示词增强）_2112140949404082178.json, 图片生成/文生图/kera-2 文生图 _ 图生图 + gemma4 自动提示词工作流_2072549485133262849.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_142

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/AI试戴美甲-穿戴甲换甲工作流_2094418586373804033.json、图片生成/图生图/Flux 3_Image_Klein开源版-多图参考生图_2111065019705286658.json、图片生成/图生图/MOSS图生图2K极速版!_2112529861960101890.json、图片生成/图生图/MOSS图生图2K极速版_2112543696460804097.json、图片生成/图生图/MOSS图生图2K极速版_2112855505784893441.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `EmptyFlux2LatentImage` —— 6/8 个有
- `LoadImage` —— 6/8 个有
- `TextGenerate` —— 6/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `ImageConcatMulti` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `EmptySD3LatentImage` —— 2/8 个有
- `ReferenceMultiLatent` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `TextEncodeQwenImageEditPlus` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 50 | 7 | 14% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 2.5 | 7 | 65% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 0.15 - 1 | 7 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 50，7 个样本，取值分散，一致性仅 14%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，7 个样本
