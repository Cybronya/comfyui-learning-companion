---
name: unknown_workflow_controlnet_lora_sampler_2
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.811
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetLoader, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree)]
members: [图片生成/文生图/1960971357423112194.json, 图片生成/文生图/1962405096208338945.json, 图片生成/文生图/1964686002021351425.json, 图片生成/文生图/1966590309864026114.json, 图片生成/文生图/1974331826225459201.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1960971357423112194.json、图片生成/文生图/1962405096208338945.json、图片生成/文生图/1964686002021351425.json、图片生成/文生图/1966590309864026114.json、图片生成/文生图/1974331826225459201.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 4/5 个有
- `ControlNetApplySD3` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `ControlNetApplyAdvanced` —— 2/5 个有
- `CannyEdgePreprocessor` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `DWPreprocessor` —— 1/5 个有
- `DepthAnythingV2Preprocessor` —— 1/5 个有
- `Fast Bypasser (rgthree)` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 2.5 | 5 | 63% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 0.75 | 0.75 - 1 | 5 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.75，观测区间 0.75 - 1，5 个样本，取值集中（一致性 86%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Fast Bypasser (rgthree)、Mute / Bypass Repeater (rgthree)
