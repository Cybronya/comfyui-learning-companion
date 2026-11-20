---
name: unknown_workflow_lora_sampler_vae_26
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.521
common_nodes: [GetNode, ImageResizeKJv2, LoadImage, SetNode, SimpleMath+, VHS_LoadVideo, WanAnimatePlus Bernini, WanAnimatePlus BlockSwap, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SamplerExtraArgs, WanAnimatePlus Samplerv2, WanAnimatePlus Schedulerv2, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Berini视频编辑换背景_2084983032410361857.json, 视频生成/图生视频/快乐老八-Wan2.2 BERNINI视频编辑工作流_2063554868475944962.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_26

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Berini视频编辑换背景_2084983032410361857.json、视频生成/图生视频/快乐老八-Wan2.2 BERNINI视频编辑工作流_2063554868475944962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
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

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
