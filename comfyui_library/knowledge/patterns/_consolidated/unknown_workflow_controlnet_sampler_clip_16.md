---
name: unknown_workflow_controlnet_sampler_clip_16
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.697
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize, GetNode, ImageScaleToMaxDimension, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingAuraFlow, Qwen3_VQA, QwenImageDiffsynthControlnet, RHHiddenNodes, SaveImage, SetNode, Text Concatenate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image Controlnet 自动提示词洗图_1996978241003012098.json, 图片生成/图生图/Z-image 完美Controlnet 洗图【2.0】自动提示词补足_1996958116019388417.json, 图片生成/文生图/Z-image 完美Controlnet 洗图【3.0】自动提示词补足_2002733726566105090.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-image Controlnet 自动提示词洗图_1996978241003012098.json、图片生成/图生图/Z-image 完美Controlnet 洗图【2.0】自动提示词补足_1996958116019388417.json、图片生成/文生图/Z-image 完美Controlnet 洗图【3.0】自动提示词补足_2002733726566105090.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `GetImageSize`
- `GetNode`
- `ImageScaleToMaxDimension`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `Qwen3_VQA`
- `QwenImageDiffsynthControlnet`
- `RHHiddenNodes`
- `SaveImage`
- `SetNode`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelPatchLoader` —— 2/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `Primitive integer [Crystools]` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 9 | 3 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | ddim_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 0.45 - 1 | 3 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 9，3 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 ddim_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.45 - 1，3 个样本
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
