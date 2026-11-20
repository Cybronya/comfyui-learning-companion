---
name: unknown_workflow_sampler_clip_vae_20
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.769778
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux-文生图自动扩写提示词（详细讲解使用）_1908181172109586433.json, 图片生成/文生图/Flux文生图（lora）工作流_1971036023260123138.json, 图片生成/文生图/Flux通过潜空间放大高清修复_1905565864324681729.json, 图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_1912944528943448065.json, 图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_1957731578933866497.json, 图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_1957999955816460290.json, 图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_2061101576210698241.json, 图片生成/文生图/【胶片感】Nun Flux krea文生图（基础流）_1953735580985249793.json, 图片生成/文生图/文生图扩写_1930841515361239042.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_20

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Flux-文生图自动扩写提示词（详细讲解使用）_1908181172109586433.json、图片生成/文生图/Flux文生图（lora）工作流_1971036023260123138.json、图片生成/文生图/Flux通过潜空间放大高清修复_1905565864324681729.json、图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_1912944528943448065.json、图片生成/文生图/【10秒出图】Nun Flux-文生图扩写提示词（中文输入）_1957731578933866497.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 9 个 workflow 都包含：
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
- `Anything Everywhere` —— 8/9 个有
- `CR Text` —— 7/9 个有
- `CR Text Concatenate` —— 7/9 个有
- `RH_Prompter` —— 7/9 个有
- `ShowText|pysssss` —— 7/9 个有
- `EG_XZ_QH` —— 6/9 个有
- `NunchakuFluxDiTLoader` —— 6/9 个有
- `RH_Translator` —— 6/9 个有
- `easy cleanGpuUsed` —— 6/9 个有
- `NunchakuFluxLoraLoader` —— 5/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `UNETLoader` —— 3/9 个有
- `FluxResolutionNode` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `ImageCASharpening+` —— 1/9 个有
- `LatentUpscaleBy` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `TextInput_` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 600 | 512 - 840 | 9 | 85% |
| 高度 | 800 | 512 - 1280 | 9 | 74% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 600，观测区间 512 - 840，9 个样本，取值集中（一致性 85%）
- 高度 中位数 800，观测区间 512 - 1280，9 个样本
