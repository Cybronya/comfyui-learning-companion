---
name: unknown_workflow_video_lora_sampler_794
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6615
common_nodes: [CLIPTextEncode, CR Text, CheckpointLoaderSimple, ImageBatchMulti, ImageResizeKJv2, LoadImage, RIFE VFI, SAM3_VideoTrack, SCAIL2ColoredMask, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/2072321050989383682.json, 视频生成/图生视频/2072172131533803521.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_794

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2072321050989383682.json、视频生成/图生视频/2072172131533803521.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `RIFE VFI`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
