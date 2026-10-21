---
name: unknown_workflow_sampler_clip_unet_110
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.785667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [MathExpression|pysssss, ImageResize+, LayerMask: BenUltra, LayerMask: LoadBenModel, LayerUtility: ImageScaleRestore]
members: [图片生成/文生图/1938559858222551041.json, 图片生成/文生图/1939140747582955521.json, 图片生成/文生图/1942411562571214849.json, 图片生成/文生图/1942739895523979266.json, 图片生成/文生图/1942746478307946498.json, 图片生成/文生图/1952011457573629953.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_110

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1938559858222551041.json、图片生成/文生图/1939140747582955521.json、图片生成/文生图/1942411562571214849.json、图片生成/文生图/1942739895523979266.json、图片生成/文生图/1942746478307946498.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 5/6 个有
- `FluxResolutionNode` —— 5/6 个有
- `MathExpression|pysssss` —— 5/6 个有
- `RH_Translator` —— 5/6 个有
- `ImageResize+` —— 4/6 个有
- `FluxKontextImageScale` —— 2/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `LayerMask: BenUltra` —— 1/6 个有
- `LayerMask: LoadBenModel` —— 1/6 个有
- `LayerUtility: ImageScaleRestore` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RBGImageStitchPlus` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1280 | 1280 - 1280 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、ImageResize+、LayerMask: BenUltra、LayerMask: LoadBenModel、LayerUtility: ImageScaleRestore
