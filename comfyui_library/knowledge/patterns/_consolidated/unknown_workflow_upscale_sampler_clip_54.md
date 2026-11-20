---
name: unknown_workflow_upscale_sampler_clip_54
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.917333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux文生图+SD放大_1910653440345997314.json, 图片生成/文生图/Flux简易文生图+放大_1902293777606975490.json, 平台全量/nunchaku-flux.1-dev人物高清放大_1940795667176648705.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flux文生图+SD放大_1910653440345997314.json、图片生成/文生图/Flux简易文生图+放大_1902293777606975490.json、平台全量/nunchaku-flux.1-dev人物高清放大_1940795667176648705.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `FluxResolutionNode` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `JjkShowText` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1280 | 768 - 1280 | 3 | 78% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 768 - 1280，3 个样本
