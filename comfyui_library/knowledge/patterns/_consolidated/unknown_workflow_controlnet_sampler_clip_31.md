---
name: unknown_workflow_controlnet_sampler_clip_31
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.771
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ControlNetLoader, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen参考控制文生图：打破限制，掌控你的视觉构图！文生图_参考姿势、深度、线稿_1965617902089027586.json, 图片生成/文生图/Qwen文生图控制(姿势、线稿、深度)InstantX-Union-ControlNet工作流_1966590309864026114.json, 平台全量/Qwen-Image最强姿态控制inatanlX，美女lora_1985019732329992193.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen参考控制文生图：打破限制，掌控你的视觉构图！文生图_参考姿势、深度、线稿_1965617902089027586.json、图片生成/文生图/Qwen文生图控制(姿势、线稿、深度)InstantX-Union-ControlNet工作流_1966590309864026114.json、平台全量/Qwen-Image最强姿态控制inatanlX，美女lora_1985019732329992193.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplySD3` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 3 | 65% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.75 | 0.75 - 1 | 3 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.75，观测区间 0.75 - 1，3 个样本，取值集中（一致性 86%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
