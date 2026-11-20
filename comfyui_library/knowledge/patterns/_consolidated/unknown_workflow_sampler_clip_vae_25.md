---
name: unknown_workflow_sampler_clip_vae_25
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7634
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux-文生图自动扩写提示词（详细讲解使用）_1908181172109586433.json, 图片生成/文生图/Flux文生图（lora）工作流_1971036023260123138.json, 图片生成/文生图/Flux通过潜空间放大高清修复_1905565864324681729.json, 图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_1912944528943448065.json, 图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_1957731578933866497.json, 图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_1957999955816460290.json, 图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_2061101576210698241.json, 图片生成/文生图/【胶片感】Nun Flux krea文生图（基础流）_1953735580985249793.json, 图片生成/文生图/文生图扩写_1930841515361239042.json, 平台全量/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_2015062908849364994.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_25

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Flux-文生图自动扩写提示词（详细讲解使用）_1908181172109586433.json、图片生成/文生图/Flux文生图（lora）工作流_1971036023260123138.json、图片生成/文生图/Flux通过潜空间放大高清修复_1905565864324681729.json、图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_1912944528943448065.json、图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_1957731578933866497.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 10 个 workflow 都包含：
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
- `Anything Everywhere` —— 9/10 个有
- `CR Text` —— 8/10 个有
- `CR Text Concatenate` —— 8/10 个有
- `RH_Prompter` —— 8/10 个有
- `ShowText|pysssss` —— 8/10 个有
- `EG_XZ_QH` —— 7/10 个有
- `NunchakuFluxDiTLoader` —— 7/10 个有
- `RH_Translator` —— 7/10 个有
- `easy cleanGpuUsed` —— 7/10 个有
- `NunchakuFluxLoraLoader` —— 6/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `UNETLoader` —— 3/10 个有
- `FluxResolutionNode` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `ImageCASharpening+` —— 1/10 个有
- `LatentUpscaleBy` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `TextInput_` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 600 | 512 - 840 | 10 | 85% |
| 高度 | 800 | 512 - 1280 | 10 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 600，观测区间 512 - 840，10 个样本，取值集中（一致性 85%）
- 高度 中位数 800，观测区间 512 - 1280，10 个样本
