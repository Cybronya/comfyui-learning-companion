---
name: unknown_workflow_sampler_clip_unet_450
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.988
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/爆分游戏的三个爆分状态_2086696888518135810.json, 视频生成/图生视频/Flux2单图+双图编辑工作流_2014254176355753986.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_450

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/爆分游戏的三个爆分状态_2086696888518135810.json、视频生成/图生视频/Flux2单图+双图编辑工作流_2014254176355753986.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
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
- `AILab_ImageCombiner` —— 1/2 个有
- `BiRefNetRMBG` —— 1/2 个有
- `EmptyFlux2LatentImage` —— 1/2 个有
- `ImageBlur` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `LayerColor: AutoAdjustV2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
