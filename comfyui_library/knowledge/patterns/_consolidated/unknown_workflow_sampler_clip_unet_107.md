---
name: unknown_workflow_sampler_clip_unet_107
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2072586147523551233.json, 视频生成/图生视频/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2102351446854426626.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_107

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2072586147523551233.json、视频生成/图生视频/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2102351446854426626.json）

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
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Int` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
