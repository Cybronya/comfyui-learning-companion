---
key: 视频生成/文生视频/SCAIL-2 Multi-Reference Character Swap_2072998835137585152.json
name: SCAIL-2 Multi-Reference Character Swap_2072998835137585152
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Multi-Reference Character Swap_2072998835137585152.json
hash: 5ccca6a383f38499
coverage: 0.826923
learned_at: 2026-10-15 22:46:54
nodes: [WanAnimatePlus SetLoRAs, PreviewImage, SAM3_VideoTrack, SAM3_VideoTrack, ImageResizeKJv2, ImageResizeKJv2, CheckpointLoaderSimple, PreviewImage, SAM3_VideoTrack, SAM3_VideoTrack, ImageResizeKJv2, PreviewImage, WanAnimatePlus VAELoader, WanAnimatePlus LoraSelectMulti, WanAnimatePlus Sampler, PreviewImage, ImageBatchMulti, ImageResizeKJv2, PreviewImage, WanAnimatePlus Decode, CLIPTextEncode, MarkdownNote, WanAnimatePlus ModelLoader, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, WanAnimatePlus ContextOptions, SCAIL2ColoredMask, SCAIL2ColoredMask, WanAnimatePlus BlockSwap, SAM3_TrackToMask, ImageCompositeMasked, PreviewImage, SAM3_TrackToMask, EmptyImage, ImageCompositeMasked, PreviewImage, SAM3_TrackToMask, EmptyImage, ImageCompositeMasked, PreviewImage, EmptyImage, VHS_LoadVideo, WanAnimatePlus TextEncodeCached, ImageResizeKJv2, SCAIL2ColoredMask, WanAnimatePlus SCAIL_2 Embeds, ImageBatchMulti]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 视频生成/文生视频/SCAIL-2 Multi-Reference Character Swap_2072998835137585152.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Multi-Reference Character Swap_2072998835137585152.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（52 个）：
- `WanAnimatePlus SetLoRAs`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanAnimatePlus VAELoader`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus Sampler` ★核心
- `PreviewImage`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanAnimatePlus Decode`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `WanAnimatePlus ModelLoader`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanAnimatePlus ContextOptions`
- `SCAIL2ColoredMask`
- `SCAIL2ColoredMask`
- `WanAnimatePlus BlockSwap`
- `SAM3_TrackToMask`
- `ImageCompositeMasked`
- `PreviewImage`
- `SAM3_TrackToMask`
- `EmptyImage`
- `ImageCompositeMasked`
- `PreviewImage`
- `SAM3_TrackToMask`
- `EmptyImage`
- `ImageCompositeMasked`
- `PreviewImage`
- `EmptyImage`
- `VHS_LoadVideo`
- `WanAnimatePlus TextEncodeCached`
- `ImageResizeKJv2`
- `SCAIL2ColoredMask`
- `WanAnimatePlus SCAIL_2 Embeds`
- `ImageBatchMulti`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **83%**（43/52）

**有卡**：`WanAnimatePlus SetLoRAs`、`SAM3_VideoTrack`、`ImageResizeKJv2`、`CheckpointLoaderSimple`、`WanAnimatePlus VAELoader`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus Sampler`、`ImageBatchMulti`、`WanAnimatePlus Decode`、`CLIPTextEncode`、`WanAnimatePlus ModelLoader`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`LoadImage`、`WanAnimatePlus ContextOptions`、`SCAIL2ColoredMask`、`WanAnimatePlus BlockSwap`、`SAM3_TrackToMask`、`ImageCompositeMasked`、`EmptyImage`、`VHS_LoadVideo`、`WanAnimatePlus TextEncodeCached`、`WanAnimatePlus SCAIL_2 Embeds`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanAnimatePlus Sampler、WanAnimatePlus Decode、WanAnimatePlus TextEncodeCached、WanAnimatePlus VAELoader、WanAnimatePlus LoraSelectMulti
