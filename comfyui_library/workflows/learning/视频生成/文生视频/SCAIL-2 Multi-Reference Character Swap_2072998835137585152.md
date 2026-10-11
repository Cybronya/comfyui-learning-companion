---
key: 视频生成/文生视频/SCAIL-2 Multi-Reference Character Swap_2072998835137585152.json
name: SCAIL-2 Multi-Reference Character Swap_2072998835137585152
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Multi-Reference Character Swap_2072998835137585152.json
hash: 5ccca6a383f38499
coverage: 0.634615
learned_at: 2026-10-11 20:21:29
nodes: [WanAnimatePlus SetLoRAs, PreviewImage, SAM3_VideoTrack, SAM3_VideoTrack, ImageResizeKJv2, ImageResizeKJv2, CheckpointLoaderSimple, PreviewImage, SAM3_VideoTrack, SAM3_VideoTrack, ImageResizeKJv2, PreviewImage, WanAnimatePlus VAELoader, WanAnimatePlus LoraSelectMulti, WanAnimatePlus Sampler, PreviewImage, ImageBatchMulti, ImageResizeKJv2, PreviewImage, WanAnimatePlus Decode, CLIPTextEncode, MarkdownNote, WanAnimatePlus ModelLoader, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, WanAnimatePlus ContextOptions, SCAIL2ColoredMask, SCAIL2ColoredMask, WanAnimatePlus BlockSwap, SAM3_TrackToMask, ImageCompositeMasked, PreviewImage, SAM3_TrackToMask, EmptyImage, ImageCompositeMasked, PreviewImage, SAM3_TrackToMask, EmptyImage, ImageCompositeMasked, PreviewImage, EmptyImage, VHS_LoadVideo, WanAnimatePlus TextEncodeCached, ImageResizeKJv2, SCAIL2ColoredMask, WanAnimatePlus SCAIL_2 Embeds, ImageBatchMulti]
patterns: []
missing: [WanAnimatePlus BlockSwap, WanAnimatePlus ContextOptions, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader]
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
discoveries: [次要节点 `WanAnimatePlus BlockSwap` 知识库中没有该节点类型的任何知识, 次要节点 `WanAnimatePlus ContextOptions` 知识库中没有该节点类型的任何知识, 次要节点 `WanAnimatePlus ModelLoader` 知识库中没有该节点类型的任何知识, 次要节点 `WanAnimatePlus SCAIL_2 Embeds` 知识库中没有该节点类型的任何知识, 核心节点 `WanAnimatePlus Sampler` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `WanAnimatePlus Decode` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `WanAnimatePlus LoraSelectMulti` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `WanAnimatePlus SetLoRAs` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `WanAnimatePlus TextEncodeCached` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `WanAnimatePlus VAELoader` 仅有 VAE 的通用知识，没有该节点自己的说明]
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

覆盖率 **63%**（33/52）

**有卡**：`SAM3_VideoTrack`、`ImageResizeKJv2`、`CheckpointLoaderSimple`、`ImageBatchMulti`、`CLIPTextEncode`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`LoadImage`、`SCAIL2ColoredMask`、`SAM3_TrackToMask`、`ImageCompositeMasked`、`EmptyImage`、`VHS_LoadVideo`

**缺卡**（10）：`WanAnimatePlus BlockSwap`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus SCAIL_2 Embeds`、`WanAnimatePlus Sampler`、`WanAnimatePlus Decode`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus TextEncodeCached`、`WanAnimatePlus VAELoader`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ImageResizeKJv2、EmptyImage、ImageBatchMulti、VHS_LoadVideo、VHS_VideoCombine

## 学习发现

- 次要节点 `WanAnimatePlus BlockSwap` 知识库中没有该节点类型的任何知识
- 次要节点 `WanAnimatePlus ContextOptions` 知识库中没有该节点类型的任何知识
- 次要节点 `WanAnimatePlus ModelLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `WanAnimatePlus SCAIL_2 Embeds` 知识库中没有该节点类型的任何知识
- 核心节点 `WanAnimatePlus Sampler` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `WanAnimatePlus Decode` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `WanAnimatePlus LoraSelectMulti` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `WanAnimatePlus SetLoRAs` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `WanAnimatePlus TextEncodeCached` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `WanAnimatePlus VAELoader` 仅有 VAE 的通用知识，没有该节点自己的说明
