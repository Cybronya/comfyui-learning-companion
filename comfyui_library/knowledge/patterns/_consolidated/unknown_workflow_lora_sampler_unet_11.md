---
name: unknown_workflow_lora_sampler_unet_11
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.848875
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [ImageCrop+]
members: [图片生成/文生图/1911275546050002945.json, 图片生成/文生图/1911723649815015426.json, 图片生成/文生图/1911771666933055489.json, 图片生成/文生图/1914936305506287617.json, 图片生成/文生图/1915225224143372289.json, 图片生成/文生图/1915236159570509826.json, 图片生成/文生图/1915288629995048961.json, 图片生成/文生图/1927964492725141505.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_11

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1911275546050002945.json、图片生成/文生图/1911723649815015426.json、图片生成/文生图/1911771666933055489.json、图片生成/文生图/1914936305506287617.json、图片生成/文生图/1915225224143372289.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 6/8 个有
- `FluxGuidance` —— 5/8 个有
- `EmptyLatentImage` —— 4/8 个有
- `EmptySD3LatentImage` —— 4/8 个有
- `ModelSamplingFlux` —— 4/8 个有
- `CLIPTextEncodeFlux` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `ImageCrop+` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `SeargePromptCombiner` —— 1/8 个有
- `TextInput_` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.6 - 1 | 8 | 84% |
| LoRA 文本强度 | 1 | 0 - 1 | 8 | 62% |
| 宽度 | 800 | 768 - 1024 | 4 | 88% |
| 高度 | 1024 | 1024 - 1248 | 4 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.6 - 1，8 个样本，取值集中（一致性 84%）
- LoRA 文本强度 中位数 1，观测区间 0 - 1，8 个样本
- 宽度 中位数 800，观测区间 768 - 1024，4 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 1248，4 个样本，取值集中（一致性 91%）
- 这些节点还没有知识卡，系统对它们的理解有限：ImageCrop+
