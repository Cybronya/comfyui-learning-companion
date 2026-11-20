---
key: 平台全量/SCAIL2动作迁移+角色替换合集 支持长视频（8.01更新）_2065318799263490050.json
name: SCAIL2动作迁移+角色替换合集 支持长视频（8.01更新）_2065318799263490050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SCAIL2动作迁移+角色替换合集 支持长视频（8.01更新）_2065318799263490050.json
hash: 753d071e9b323a64
coverage: 0.542373
learned_at: 2026-11-14 00:55:34
nodes: [SAM3_VideoTrack, GetNode, GetImageRangeFromBatch, SetNode, GetNode, ImageConcanate, ImageConcanate, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, CLIPVisionLoader, WanAnimatePlus ClipVisionEncode, WanAnimatePlus Decode, INTConstant, SetNode, GetNode, VHS_VideoCombine, GetNode, INTConstant, WanAnimatePlus LoraSelect, CheckpointLoaderSimple, WanAnimatePlus VAELoader, SAM3_VideoTrack, CLIPTextEncode, VHS_VideoCombine, SetNode, SetNode, PreviewImage, SCAIL2ColoredMask, easy imageRemBg, Switch any [Crystools], GetNode, MarkdownNote, MarkdownNote, SetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, VHS_VideoInfoLoaded, easy boolean, MarkdownNote, VHS_LoadVideo, LoadImage, INTConstant, MarkdownNote, WanAnimatePlus Sampler, WanAnimatePlus TextEncodeCached, WanAnimatePlus ModelLoader, WanAnimatePlus BlockSwap, MarkdownNote, WanAnimatePlus SCAIL_2 Embeds]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/SCAIL2动作迁移+角色替换合集 支持长视频（8.01更新）_2065318799263490050.json

> 来源文件 `comfyui_library/workflows/平台全量/SCAIL2动作迁移+角色替换合集 支持长视频（8.01更新）_2065318799263490050.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（59 个）：
- `SAM3_VideoTrack`
- `GetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `ImageConcanate`
- `ImageConcanate`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus Decode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `INTConstant`
- `WanAnimatePlus LoraSelect`
- `CheckpointLoaderSimple` ★核心
- `WanAnimatePlus VAELoader`
- `SAM3_VideoTrack`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `SCAIL2ColoredMask`
- `easy imageRemBg`
- `Switch any [Crystools]`
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `VHS_VideoInfoLoaded`
- `easy boolean`
- `MarkdownNote`
- `VHS_LoadVideo`
- `LoadImage`
- `INTConstant`
- `MarkdownNote`
- `WanAnimatePlus Sampler` ★核心
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus BlockSwap`
- `MarkdownNote`
- `WanAnimatePlus SCAIL_2 Embeds`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **54%**（32/59）

**有卡**：`SAM3_VideoTrack`、`GetImageRangeFromBatch`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`CLIPVisionLoader`、`WanAnimatePlus ClipVisionEncode`、`WanAnimatePlus Decode`、`INTConstant`、`WanAnimatePlus LoraSelect`、`CheckpointLoaderSimple`、`WanAnimatePlus VAELoader`、`CLIPTextEncode`、`SCAIL2ColoredMask`、`easy imageRemBg`、`Switch any [Crystools]`、`VHS_VideoInfoLoaded`、`easy boolean`、`VHS_LoadVideo`、`LoadImage`、`WanAnimatePlus Sampler`、`WanAnimatePlus TextEncodeCached`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus BlockSwap`、`WanAnimatePlus SCAIL_2 Embeds`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanAnimatePlus Sampler、WanAnimatePlus ClipVisionEncode、WanAnimatePlus Decode、WanAnimatePlus TextEncodeCached、WanAnimatePlus VAELoader
