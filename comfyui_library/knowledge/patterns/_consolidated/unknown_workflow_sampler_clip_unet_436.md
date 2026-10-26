---
name: unknown_workflow_sampler_clip_unet_436
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9485
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein图像风格互转_真人转动漫风格_动漫风格转真人_2054440839576866818.json, 图片生成/图生图/一致性换脸工作流_2043924693551423490.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_436

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/klein图像风格互转_真人转动漫风格_动漫风格转真人_2054440839576866818.json、图片生成/图生图/一致性换脸工作流_2043924693551423490.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `HAIGC_LoadImagesFromZip` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Model Input Switch` —— 1/2 个有
- `ModelPatchLoader` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `QwenImageDiffsynthControlnet` —— 1/2 个有
- `RH_BatchImages` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
