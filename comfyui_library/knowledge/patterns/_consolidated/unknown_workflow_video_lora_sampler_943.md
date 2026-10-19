---
name: unknown_workflow_video_lora_sampler_943
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8385
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageBatchMulti, ImageResizeKJv2, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, VHS_LoadVideo, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/SCAIL-2 Multi-Reference Character Swap_2072998835137585152.json, 视频生成/文生视频/SCAIL-2 Multi-Reference Motion Guide_2072998836324573184.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_943

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/SCAIL-2 Multi-Reference Character Swap_2072998835137585152.json、视频生成/文生视频/SCAIL-2 Multi-Reference Motion Guide_2072998836324573184.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `SAM3_TrackToMask` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
