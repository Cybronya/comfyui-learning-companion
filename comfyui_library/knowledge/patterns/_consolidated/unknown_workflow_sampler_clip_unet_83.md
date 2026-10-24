---
name: unknown_workflow_sampler_clip_unet_83
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.900636
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image-controlnet 2.1 图生图_2009424173604544514.json, 图片生成/图生图/Z-image图生图-canny控制_1998928195103641601.json, 图片生成/图生图/Z-image图生图-depth深度控制_1998934414765776897.json, 图片生成/图生图/Z-image图生图-dw姿态控制_1998936679278895105.json, 图片生成/图生图/Z-image图生图-深度控制-真人转美漫_1998939406658588673.json, 图片生成/图生图/Z-image图生图精准控制版_2064281103275483138.json, 图片生成/图生图/Z-image标准版Cn控制V1图生图_1996307091344211970.json, 图片生成/文生图/Z-image Controlnet Union 1.0 Vs 2.0对比工作流_2000525274498428929.json, 图片生成/文生图/【阡陌】Z-Image+controlnet 2.1 自动反推提示词洗图工作流_2003449912257880066.json, 图片生成/文生图/【阡陌】Z-Image+controlnet自动反推提示词洗图工作流_1999304671166689282.json, 图片生成/文生图/文生图姿态迁移Zimage标准版Cn控制(多姿态控制）图生图（加速版）_1996442210822397953.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_83

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Z-image-controlnet 2.1 图生图_2009424173604544514.json、图片生成/图生图/Z-image图生图-canny控制_1998928195103641601.json、图片生成/图生图/Z-image图生图-depth深度控制_1998934414765776897.json、图片生成/图生图/Z-image图生图-dw姿态控制_1998936679278895105.json、图片生成/图生图/Z-image图生图-深度控制-真人转美漫_1998939406658588673.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImageDiffsynthControlnet` —— 9/11 个有
- `ImageScaleToMaxDimension` —— 8/11 个有
- `AIO_Preprocessor` —— 7/11 个有
- `Canny` —— 5/11 个有
- `CR Prompt Text` —— 3/11 个有
- `ImageConcatMulti` —— 3/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `QwenVisionNode` —— 3/11 个有
- `easy conditioningIndexSwitch` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `ZImageFunControlnet` —— 2/11 个有
- `AddLabel` —— 1/11 个有
- `DWPreprocessor` —— 1/11 个有
- `DepthAnythingPreprocessor` —— 1/11 个有
- `LineArtPreprocessor` —— 1/11 个有
- `easy anythingIndexSwitch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 10 | 11 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | res_multistep | - | 11 | 82% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 10，11 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，11 个样本，一致性 82%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（8/11 个样本）：Steps较低可能导致细节不足
