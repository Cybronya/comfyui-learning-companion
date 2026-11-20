---
name: unknown_workflow_sampler_clip_unet_459
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5855
common_nodes: [AIO_Preprocessor, Anything Everywhere, CLIPLoader, CLIPTextEncode, DrawMaskOnImage, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), FastCanvas, FastCanvasTool, Flux2Scheduler, GetNode, JoinImageWithAlpha, KSamplerSelect, LoadImage, PreviewAny, PreviewImage, Qwen3_VQA, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageRemBg, easy seed, 孤海-图像与遮罩描边]
problems: []
missing: []
members: [图片生成/文生图/Flux.2 klein 单图_多图编辑 文生图 二合一 基础_2012476273980874753.json, 图片生成/文生图/Flux.2 基础 文生图 +多图编辑 _ 图像参考 二合一_1993632576155877378.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_459

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux.2 klein 单图_多图编辑 文生图 二合一 基础_2012476273980874753.json、图片生成/文生图/Flux.2 基础 文生图 +多图编辑 _ 图像参考 二合一_1993632576155877378.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `DrawMaskOnImage`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FastCanvas`
- `FastCanvasTool`
- `Flux2Scheduler`
- `GetNode`
- `JoinImageWithAlpha`
- `KSamplerSelect`
- `LoadImage`
- `PreviewAny`
- `PreviewImage`
- `Qwen3_VQA`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageRemBg`
- `easy seed`
- `孤海-图像与遮罩描边`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `CFGGuider` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `EasyCache` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RebatchLatents` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `Text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
