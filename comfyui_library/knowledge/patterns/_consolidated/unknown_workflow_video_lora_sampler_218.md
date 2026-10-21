---
name: unknown_workflow_video_lora_sampler_218
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.839778
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageBatchMulti, ImageConcatMulti, ImageResizeKJv2, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, VHS_LoadVideo, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2066386680499761154.json, 视频生成/图生视频/2066423753369808897.json, 视频生成/图生视频/2066016584279347201.json, 视频生成/图生视频/2066001113731649537.json, 视频生成/图生视频/2066378010617540610.json, 视频生成/图生视频/2073343102223470594.json, 视频生成/图生视频/2065965062183018498.json, 视频生成/图生视频/2066889873231015938.json, 视频生成/图生视频/2065963015316525057.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_218

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2066386680499761154.json、视频生成/图生视频/2066423753369808897.json、视频生成/图生视频/2066016584279347201.json、视频生成/图生视频/2066001113731649537.json、视频生成/图生视频/2066378010617540610.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
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

**可变部分**（部分 workflow 才有）：
- `WanAnimatePlus ContextOptions` —— 8/9 个有
- `Int` —— 3/9 个有
- `JjkText` —— 2/9 个有
- `Text` —— 2/9 个有
- `CLIPVisionLoader` —— 1/9 个有
- `If ANY execute A else B` —— 1/9 个有
- `ImpactNeg` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `WanAnimatePlus ClipVisionEncode` —— 1/9 个有
- `easy boolean` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
