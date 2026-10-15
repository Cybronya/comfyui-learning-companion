---
key: 视频生成/文生视频/SCAIL-2 Multi-Reference Motion Guide_2072998836324573184.json
name: SCAIL-2 Multi-Reference Motion Guide_2072998836324573184
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Multi-Reference Motion Guide_2072998836324573184.json
hash: 393def4c2dcb9049
coverage: 0.85
learned_at: 2026-10-15 22:46:54
nodes: [WanAnimatePlus BlockSwap, WanAnimatePlus SetLoRAs, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SAM3_VideoTrack, ImageResizeKJv2, ImageResizeKJv2, CheckpointLoaderSimple, SCAIL2ColoredMask, PreviewImage, SAM3_VideoTrack, SAM3_VideoTrack, SCAIL2ColoredMask, ImageResizeKJv2, ImageBatchMulti, PreviewImage, WanAnimatePlus VAELoader, WanAnimatePlus LoraSelectMulti, WanAnimatePlus Sampler, PreviewImage, ImageBatchMulti, ImageResizeKJv2, PreviewImage, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, CLIPTextEncode, WanAnimatePlus SCAIL_2 Embeds, MarkdownNote, WanAnimatePlus ModelLoader, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_LoadVideo, WanAnimatePlus TextEncodeCached, LoadImage, LoadImage, LoadImage, VHS_VideoCombine, LoadImage, ImageResizeKJv2]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
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

覆盖率 **85%**（34/40）

**有卡**：`WanAnimatePlus BlockSwap`、`WanAnimatePlus SetLoRAs`、`SAM3_VideoTrack`、`SCAIL2ColoredMask`、`ImageResizeKJv2`、`CheckpointLoaderSimple`、`ImageBatchMulti`、`WanAnimatePlus VAELoader`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus Sampler`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus Decode`、`CLIPTextEncode`、`WanAnimatePlus SCAIL_2 Embeds`、`WanAnimatePlus ModelLoader`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`VHS_LoadVideo`、`WanAnimatePlus TextEncodeCached`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanAnimatePlus Sampler、WanAnimatePlus Decode、WanAnimatePlus TextEncodeCached、WanAnimatePlus VAELoader、WanAnimatePlus LoraSelectMulti
