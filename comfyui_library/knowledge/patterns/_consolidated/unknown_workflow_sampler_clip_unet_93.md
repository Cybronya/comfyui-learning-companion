---
name: unknown_workflow_sampler_clip_unet_93
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.812
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, INTConstant, JWStringConcat, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Qwen3_VQA, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline, CR Latent Input Switch, CR Prompt Text, easy imageSize, easy promptLine]
members: [图片生成/图生图/2015961543439028226.json, 图片生成/图生图/2043916659529883649.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_93

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2015961543439028226.json、图片生成/图生图/2043916659529883649.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `INTConstant`
- `JWStringConcat`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Qwen3_VQA`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Latent Input Switch` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Text Multiline、CR Latent Input Switch、CR Prompt Text、easy imageSize
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
