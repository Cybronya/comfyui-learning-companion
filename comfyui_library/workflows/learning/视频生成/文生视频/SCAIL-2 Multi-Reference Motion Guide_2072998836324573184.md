---
key: 视频生成/文生视频/SCAIL-2 Multi-Reference Motion Guide_2072998836324573184.json
name: SCAIL-2 Multi-Reference Motion Guide_2072998836324573184
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Multi-Reference Motion Guide_2072998836324573184.json
hash: 393def4c2dcb9049
coverage: 0.6
learned_at: 2026-10-11 20:21:29
nodes: [WanAnimatePlus BlockSwap, WanAnimatePlus SetLoRAs, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SAM3_VideoTrack, ImageResizeKJv2, ImageResizeKJv2, CheckpointLoaderSimple, SCAIL2ColoredMask, PreviewImage, SAM3_VideoTrack, SAM3_VideoTrack, SCAIL2ColoredMask, ImageResizeKJv2, ImageBatchMulti, PreviewImage, WanAnimatePlus VAELoader, WanAnimatePlus LoraSelectMulti, WanAnimatePlus Sampler, PreviewImage, ImageBatchMulti, ImageResizeKJv2, PreviewImage, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, CLIPTextEncode, WanAnimatePlus SCAIL_2 Embeds, MarkdownNote, WanAnimatePlus ModelLoader, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_LoadVideo, WanAnimatePlus TextEncodeCached, LoadImage, LoadImage, LoadImage, VHS_VideoCombine, LoadImage, ImageResizeKJv2]
patterns: []
missing: [WanAnimatePlus BlockSwap, WanAnimatePlus ContextOptions, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader]
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
discoveries: [次要节点 `WanAnimatePlus BlockSwap` 知识库中没有该节点类型的任何知识, 次要节点 `WanAnimatePlus ContextOptions` 知识库中没有该节点类型的任何知识, 次要节点 `WanAnimatePlus ModelLoader` 知识库中没有该节点类型的任何知识, 次要节点 `WanAnimatePlus SCAIL_2 Embeds` 知识库中没有该节点类型的任何知识, 核心节点 `WanAnimatePlus Sampler` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `WanAnimatePlus Decode` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `WanAnimatePlus LoraSelectMulti` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `WanAnimatePlus SetLoRAs` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `WanAnimatePlus TextEncodeCached` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `WanAnimatePlus VAELoader` 仅有 VAE 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/SCAIL-2 Multi-Reference Motion Guide_2072998836324573184.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Multi-Reference Motion Guide_2072998836324573184.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（40 个）：
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus SetLoRAs`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SAM3_VideoTrack`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CheckpointLoaderSimple` ★核心
- `SCAIL2ColoredMask`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `ImageResizeKJv2`
- `ImageBatchMulti`
- `PreviewImage`
- `WanAnimatePlus VAELoader`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus Sampler` ★核心
- `PreviewImage`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus Decode`
- `CLIPTextEncode` ★核心
- `WanAnimatePlus SCAIL_2 Embeds`
- `MarkdownNote`
- `WanAnimatePlus ModelLoader`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `VHS_LoadVideo`
- `WanAnimatePlus TextEncodeCached`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJv2`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **60%**（24/40）

**有卡**：`SAM3_VideoTrack`、`SCAIL2ColoredMask`、`ImageResizeKJv2`、`CheckpointLoaderSimple`、`ImageBatchMulti`、`CLIPTextEncode`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoCombine`

**缺卡**（10）：`WanAnimatePlus BlockSwap`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus SCAIL_2 Embeds`、`WanAnimatePlus Sampler`、`WanAnimatePlus Decode`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus TextEncodeCached`、`WanAnimatePlus VAELoader`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ImageResizeKJv2、ImageBatchMulti、VHS_LoadVideo、VHS_VideoCombine、SAM3_VideoTrack

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
