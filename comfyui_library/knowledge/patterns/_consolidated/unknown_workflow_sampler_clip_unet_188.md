---
name: unknown_workflow_sampler_clip_unet_188
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.610667
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetNode, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageRemBg, easy seed]
problems: []
missing: []
members: [图片生成/文生图/Flux.2 klein 单图_多图编辑 文生图 二合一 基础_2012476273980874753.json, 图片生成/文生图/Flux.2 基础 文生图 +多图编辑 _ 图像参考 二合一_1993632576155877378.json, 图片生成/文生图/加速优化！Flux.2 基础文生图+多图编辑_图像参考多合一工作流_2058209151062462465.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_188

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flux.2 klein 单图_多图编辑 文生图 二合一 基础_2012476273980874753.json、图片生成/文生图/Flux.2 基础 文生图 +多图编辑 _ 图像参考 二合一_1993632576155877378.json、图片生成/文生图/加速优化！Flux.2 基础文生图+多图编辑_图像参考多合一工作流_2058209151062462465.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
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

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `BasicGuider` —— 2/3 个有
- `DrawMaskOnImage` —— 2/3 个有
- `EasyCache` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `FastCanvas` —— 2/3 个有
- `FastCanvasTool` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `Int` —— 2/3 个有
- `JoinImageWithAlpha` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelPatchTorchSettings` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `Qwen3_VQA` —— 2/3 个有
- `Text` —— 2/3 个有
- `孤海-图像与遮罩描边` —— 2/3 个有
- `1hew_AnySwitchSelect` —— 1/3 个有
- `CFGGuider` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `RebatchLatents` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
