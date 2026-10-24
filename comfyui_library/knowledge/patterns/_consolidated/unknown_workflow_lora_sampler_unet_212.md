---
name: unknown_workflow_lora_sampler_unet_212
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.663333
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyLatentImage, GetNode, KSampler, LoadImage, LoraLoaderModelOnly, QwenMultiangleCameraNode, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen多角度单角度批量图片生成工作流分镜制作或素材库_2018253621518929922.json, 图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2011298197339115521.json, 图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2040760101212000257.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_212

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen多角度单角度批量图片生成工作流分镜制作或素材库_2018253621518929922.json、图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2011298197339115521.json、图片生成/图生图/qwen-image-edit-2511-multiple-angles-lora_2040760101212000257.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JoinStringMulti` —— 2/3 个有
- `KepStringLiteral` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `easy imageSize` —— 1/3 个有
- `easy promptLine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 3 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1280 | 720 - 1408 | 3 | 74% |
| 高度 | 768 | 720 - 1280 | 3 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，3 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 720 - 1408，3 个样本
- 高度 中位数 768，观测区间 720 - 1280，3 个样本
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
