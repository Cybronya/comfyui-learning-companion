---
name: unknown_workflow_sampler_vae_19
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.743769
common_nodes: [BasicGuider, BasicScheduler, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR Text, CR Text Concatenate, easy cleanGpuUsed, ImageCASharpening+, MathExpression|pysssss, easy textSwitch]
members: [图片生成/文生图/1904904736871469057.json, 图片生成/文生图/1904906707053776898.json, 图片生成/文生图/1904907559919357954.json, 图片生成/文生图/1904908786933633026.json, 图片生成/文生图/1904909104412807170.json, 图片生成/文生图/1905565864324681729.json, 图片生成/文生图/1908181172109586433.json, 图片生成/文生图/1912944528943448065.json, 图片生成/文生图/1930841515361239042.json, 图片生成/文生图/1953735580985249793.json, 图片生成/文生图/1953815039516004354.json, 图片生成/文生图/1957731578933866497.json, 图片生成/文生图/1957999955816460290.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_19

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/1904904736871469057.json、图片生成/文生图/1904906707053776898.json、图片生成/文生图/1904907559919357954.json、图片生成/文生图/1904908786933633026.json、图片生成/文生图/1904909104412807170.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 12/13 个有
- `DualCLIPLoader` —— 12/13 个有
- `Anything Everywhere` —— 8/13 个有
- `LoraLoaderModelOnly` —— 8/13 个有
- `UNETLoader` —— 8/13 个有
- `CR Text` —— 7/13 个有
- `CR Text Concatenate` —— 7/13 个有
- `RH_Prompter` —— 7/13 个有
- `ShowText|pysssss` —— 7/13 个有
- `TextInput_` —— 6/13 个有
- `easy cleanGpuUsed` —— 6/13 个有
- `EG_XZ_QH` —— 5/13 个有
- `Int` —— 5/13 个有
- `NunchakuFluxDiTLoader` —— 5/13 个有
- `RH_Translator` —— 5/13 个有
- `NunchakuFluxLoraLoader` —— 4/13 个有
- `FluxResolutionNode` —— 2/13 个有
- `ImageCASharpening+` —— 2/13 个有
- `MathExpression|pysssss` —— 2/13 个有
- `RHHiddenNodes` —— 2/13 个有
- `CLIPLoader` —— 1/13 个有
- `CLIPTextEncode` —— 1/13 个有
- `Image Comparer (rgthree)` —— 1/13 个有
- `LatentUpscaleBy` —— 1/13 个有
- `ModelSamplingAuraFlow` —— 1/13 个有
- `easy textSwitch` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1536 | 13 | 68% |
| 高度 | 1024 | 768 - 1280 | 13 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1536，13 个样本
- 高度 中位数 1024，观测区间 768 - 1280，13 个样本，取值集中（一致性 83%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、easy cleanGpuUsed、ImageCASharpening+、MathExpression|pysssss
