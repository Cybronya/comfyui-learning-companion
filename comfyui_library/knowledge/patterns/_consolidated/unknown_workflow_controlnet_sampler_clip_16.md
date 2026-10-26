---
name: unknown_workflow_controlnet_sampler_clip_16
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.88025
common_nodes: [CLIPLoader, CLIPTextEncode, Canny, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize, ImageScaleToMaxDimension, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image 对比测试 Z-Image-Turbo_2016590069972344833.json, 图片生成/文生图/Z-Image 对比测试 Z-Image-Turbo_2017454945296982018.json, 图片生成/文生图/Z-image Controlnet Union 1.0 Vs 2.0对比工作流_2000525274498428929.json, 图片生成/文生图/文生图姿态迁移Zimage标准版Cn控制(多姿态控制）图生图（加速版）_1996442210822397953.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-Image 对比测试 Z-Image-Turbo_2016590069972344833.json、图片生成/文生图/Z-Image 对比测试 Z-Image-Turbo_2017454945296982018.json、图片生成/文生图/Z-image Controlnet Union 1.0 Vs 2.0对比工作流_2000525274498428929.json、图片生成/文生图/文生图姿态迁移Zimage标准版Cn控制(多姿态控制）图生图（加速版）_1996442210822397953.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Canny`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `GetImageSize`
- `ImageScaleToMaxDimension`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `AddLabel` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `DepthAnythingPreprocessor` —— 1/4 个有
- `LineArtPreprocessor` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 10 | 4 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 10，4 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
