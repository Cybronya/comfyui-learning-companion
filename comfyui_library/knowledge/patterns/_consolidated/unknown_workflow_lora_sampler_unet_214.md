---
name: unknown_workflow_lora_sampler_unet_214
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.79
common_nodes: [Anything Everywhere3, CFGNorm, CLIPLoader, CR Seed, EmptySD3LatentImage, ImageResizeKJ, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RHHiddenNodes, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit2509 （人像多视角九宫格【写真】）_1979492942681378817.json, 图片生成/图生图/Qwen-Image-Edit2509 （深度图控制版本）_1979386348991844354.json, 图片生成/图生图/电商模特无限特裂变-姿势裂变-视角裂变_2032817915128455169.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_214

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit2509 （人像多视角九宫格【写真】）_1979492942681378817.json、图片生成/图生图/Qwen-Image-Edit2509 （深度图控制版本）_1979386348991844354.json、图片生成/图生图/电商模特无限特裂变-姿势裂变-视角裂变_2032817915128455169.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `CFGNorm`
- `CLIPLoader`
- `CR Seed`
- `EmptySD3LatentImage`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `easy batchAnything` —— 2/3 个有
- `easy forLoopEnd` —— 2/3 个有
- `easy forLoopStart` —— 2/3 个有
- `CR Text Replace` —— 1/3 个有
- `CannyEdgePreprocessor` —— 1/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `JoinStrings` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
