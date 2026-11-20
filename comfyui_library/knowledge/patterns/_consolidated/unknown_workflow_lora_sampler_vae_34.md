---
name: unknown_workflow_lora_sampler_vae_34
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5665
common_nodes: [GetNode, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoInfo, WanAnimatePlus Bernini, WanAnimatePlus BlockSwap, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SamplerExtraArgs, WanAnimatePlus Samplerv2, WanAnimatePlus Schedulerv2, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/视频一键去水印-bernini_2114625596880941058.json, 视频生成/图生视频/Berini视频编辑换背景_2084983032410361857.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_34

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频一键去水印-bernini_2114625596880941058.json、视频生成/图生视频/Berini视频编辑换背景_2084983032410361857.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：57%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `WanAnimatePlus Bernini`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SamplerExtraArgs`
- `WanAnimatePlus Samplerv2`
- `WanAnimatePlus Schedulerv2`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `Text` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
