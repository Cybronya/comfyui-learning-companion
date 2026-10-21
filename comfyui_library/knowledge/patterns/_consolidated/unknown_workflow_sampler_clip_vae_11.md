---
name: unknown_workflow_sampler_clip_vae_11
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.6075
common_nodes: [Anything Everywhere, BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR Text, CR Text Concatenate, easy cleanGpuUsed, ImageCASharpening+, MathExpression|pysssss]
members: [图片生成/文生图/1905565864324681729.json, 图片生成/文生图/1908181172109586433.json, 图片生成/文生图/1912944528943448065.json, 图片生成/文生图/1930841515361239042.json, 图片生成/文生图/1953735580985249793.json, 图片生成/文生图/1957731578933866497.json, 图片生成/文生图/1957999955816460290.json, 图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_2061101576210698241.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_11

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1905565864324681729.json、图片生成/文生图/1908181172109586433.json、图片生成/文生图/1912944528943448065.json、图片生成/文生图/1930841515361239042.json、图片生成/文生图/1953735580985249793.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 8 个 workflow 都包含：
- `Anything Everywhere`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 7/8 个有
- `CR Text Concatenate` —— 7/8 个有
- `RH_Prompter` —— 7/8 个有
- `ShowText|pysssss` —— 7/8 个有
- `EG_XZ_QH` —— 6/8 个有
- `NunchakuFluxDiTLoader` —— 6/8 个有
- `RH_Translator` —— 6/8 个有
- `easy cleanGpuUsed` —— 6/8 个有
- `NunchakuFluxLoraLoader` —— 5/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `UNETLoader` —— 2/8 个有
- `FluxResolutionNode` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `ImageCASharpening+` —— 1/8 个有
- `LatentUpscaleBy` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `TextInput_` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 600 | 512 - 840 | 8 | 85% |
| 高度 | 800 | 768 - 1280 | 8 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 600，观测区间 512 - 840，8 个样本，取值集中（一致性 85%）
- 高度 中位数 800，观测区间 768 - 1280，8 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、easy cleanGpuUsed、ImageCASharpening+、MathExpression|pysssss
