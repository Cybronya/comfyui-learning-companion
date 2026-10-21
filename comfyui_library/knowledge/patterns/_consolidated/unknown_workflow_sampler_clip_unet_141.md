---
name: unknown_workflow_sampler_clip_unet_141
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.857
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline, CR Latent Input Switch, CR Prompt Text, easy imageSize, easy promptLine]
members: [图片生成/图生图/2015961543439028226.json, 图片生成/图生图/2043916659529883649.json, 图片生成/文生图/Flux2-Klein一自动分镜 一键生成_2014679299307085826.json, 图片生成/文生图/Flux2_klein4B&9B文生图_图生图_图像编辑合集_2012078185009127425.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_141

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2015961543439028226.json、图片生成/图生图/2043916659529883649.json、图片生成/文生图/Flux2-Klein一自动分镜 一键生成_2014679299307085826.json、图片生成/文生图/Flux2_klein4B&9B文生图_图生图_图像编辑合集_2012078185009127425.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `JWStringConcat` —— 3/4 个有
- `Qwen3_VQA` —— 3/4 个有
- `easy promptLine` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `CR Latent Input Switch` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Text Multiline、CR Latent Input Switch、CR Prompt Text、easy imageSize
