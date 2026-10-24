---
name: unknown_workflow_controlnet_sampler_clip_9
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.87275
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetLoader, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 深度 Controlnet_1967681155103428610.json, 图片生成/图生图/Qwen Image 线稿 Controlnet_1967681950809034754.json, 图片生成/图生图/Qwen-Image-10步蒸馏-Controlnet_1961780586719416322.json, 图片生成/文生图/Qwen image ControlNet控制模型 （线条、深度、姿态）8不出图_1962405096208338945.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 深度 Controlnet_1967681155103428610.json、图片生成/图生图/Qwen Image 线稿 Controlnet_1967681950809034754.json、图片生成/图生图/Qwen-Image-10步蒸馏-Controlnet_1961780586719416322.json、图片生成/文生图/Qwen image ControlNet控制模型 （线条、深度、姿态）8不出图_1962405096208338945.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplySD3` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `CFGNorm` —— 2/4 个有
- `CannyEdgePreprocessor` —— 2/4 个有
- `DWPreprocessor` —— 2/4 个有
- `DepthAnythingV2Preprocessor` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `ControlNetApplyAdvanced` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 20 | 4 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 1 | 0.7 - 1 | 4 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 0.7 - 1，4 个样本，取值集中（一致性 86%）
