---
name: unknown_workflow_controlnet_sampler_clip_8
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.6835
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize, GetNode, ImageScaleToMaxDimension, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingAuraFlow, Qwen3_VQA, QwenImageDiffsynthControlnet, RHHiddenNodes, SaveImage, SetNode, Text Concatenate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Z-image 完美Controlnet 洗图——自动提示词_2002907703670370305.json, 图片生成/图生图/Z-image Controlnet 自动提示词洗图_1996978241003012098.json, 图片生成/图生图/Z-image 完美Controlnet 洗图【2.0】自动提示词补足_1996958116019388417.json, 图片生成/文生图/Z-image 完美Controlnet 洗图【3.0】自动提示词补足_2002733726566105090.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/Z-image 完美Controlnet 洗图——自动提示词_2002907703670370305.json、图片生成/图生图/Z-image Controlnet 自动提示词洗图_1996978241003012098.json、图片生成/图生图/Z-image 完美Controlnet 洗图【2.0】自动提示词补足_1996958116019388417.json、图片生成/文生图/Z-image 完美Controlnet 洗图【3.0】自动提示词补足_2002733726566105090.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
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
- `ImageConcatMulti` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `ModelPatchLoader` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Primitive integer [Crystools]` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy showAnything` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 9 | 4 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | ddim_uniform | - | 4 | 100% |
| 重绘幅度 | 0.725 | 0.45 - 1 | 4 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 9，4 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 ddim_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 0.725，观测区间 0.45 - 1，4 个样本
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
