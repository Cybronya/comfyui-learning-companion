---
name: unknown_workflow_sampler_clip_unet_29
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.83925
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [MathExpression|pysssss, ImageResize+, LayerMask: BenUltra, LayerMask: LoadBenModel, LayerUtility: ImageScaleRestore]
members: [图片生成/文生图/1937568663094628354.json, 图片生成/文生图/1937783580867084290.json, 图片生成/文生图/1938559858222551041.json, 图片生成/文生图/1939140747582955521.json, 图片生成/文生图/1942411562571214849.json, 图片生成/文生图/1942739895523979266.json, 图片生成/文生图/1942746478307946498.json, 图片生成/文生图/1952011457573629953.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_29

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1937568663094628354.json、图片生成/文生图/1937783580867084290.json、图片生成/文生图/1938559858222551041.json、图片生成/文生图/1939140747582955521.json、图片生成/文生图/1942411562571214849.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 7/8 个有
- `FluxGuidance` —— 7/8 个有
- `LoadImage` —— 6/8 个有
- `ModelSamplingFlux` —— 6/8 个有
- `RH_Translator` —— 6/8 个有
- `ReferenceLatent` —— 6/8 个有
- `VAEEncode` —— 6/8 个有
- `FluxResolutionNode` —— 5/8 个有
- `MathExpression|pysssss` —— 5/8 个有
- `ImageResize+` —— 4/8 个有
- `FluxKontextImageScale` —— 2/8 个有
- `Bjornulf_ShowStringText` —— 1/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `ImageScaleBy` —— 1/8 个有
- `ImageStitch` —— 1/8 个有
- `LayerMask: BenUltra` —— 1/8 个有
- `LayerMask: LoadBenModel` —— 1/8 个有
- `LayerUtility: ImageScaleRestore` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RBGImageStitchPlus` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 7 | 98% |
| 高度 | 1280 | 1024 - 1280 | 7 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，7 个样本，取值集中（一致性 98%）
- 高度 中位数 1280，观测区间 1024 - 1280，7 个样本，取值集中（一致性 91%）
- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、ImageResize+、LayerMask: BenUltra、LayerMask: LoadBenModel、LayerUtility: ImageScaleRestore
