---
key: 视频生成/图生视频/SCAIL2动作迁移+角色替换动作迁移话音同步 长视频 工作流V1.0_2066527706170351617.json
name: SCAIL2动作迁移+角色替换动作迁移话音同步 长视频 工作流V1.0_2066527706170351617.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SCAIL2动作迁移+角色替换动作迁移话音同步 长视频 工作流V1.0_2066527706170351617.json
hash: 265c860a2d79f45e
coverage: 0.6
learned_at: 2026-10-15 22:39:50
nodes: [SAM3_VideoTrack, SetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, CLIPVisionLoader, WanAnimatePlus ClipVisionEncode, WanAnimatePlus Sampler, WanAnimatePlus Decode, INTConstant, SetNode, GetNode, GetNode, INTConstant, WanAnimatePlus ModelLoader, WanAnimatePlus LoraSelect, CheckpointLoaderSimple, WanAnimatePlus VAELoader, WanAnimatePlus ContextOptions, SAM3_VideoTrack, CLIPTextEncode, SetNode, SetNode, SCAIL2ColoredMask, easy imageRemBg, Switch any [Crystools], WanAnimatePlus SCAIL_2 Embeds, GetNode, SetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, WanAnimatePlus TextEncodeCached, VHS_VideoInfoLoaded, easy boolean, WanAnimatePlus BlockSwap, VHS_LoadVideo, LoadImage, INTConstant, PreviewImage, ImageConcanate, VHS_VideoCombine, VHS_VideoCombine, ImageConcanate, GetNode, GetImageRangeFromBatch]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 视频生成/图生视频/SCAIL2动作迁移+角色替换动作迁移话音同步 长视频 工作流V1.0_2066527706170351617.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066527706170351617.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（55 个）：
- `SAM3_VideoTrack`
- `SetNode`
- `GetNode`
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
- `WanAnimatePlus Sampler` ★核心
- `WanAnimatePlus Decode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus LoraSelect`
- `CheckpointLoaderSimple` ★核心
- `WanAnimatePlus VAELoader`
- `WanAnimatePlus ContextOptions`
- `SAM3_VideoTrack`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SCAIL2ColoredMask`
- `easy imageRemBg`
- `Switch any [Crystools]`
- `WanAnimatePlus SCAIL_2 Embeds`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `WanAnimatePlus TextEncodeCached`
- `VHS_VideoInfoLoaded`
- `easy boolean`
- `WanAnimatePlus BlockSwap`
- `VHS_LoadVideo`
- `LoadImage`
- `INTConstant`
- `PreviewImage`
- `ImageConcanate`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcanate`
- `GetNode`
- `GetImageRangeFromBatch`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **60%**（33/55）

**有卡**：`SAM3_VideoTrack`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`CLIPVisionLoader`、`WanAnimatePlus ClipVisionEncode`、`WanAnimatePlus Sampler`、`WanAnimatePlus Decode`、`INTConstant`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus LoraSelect`、`CheckpointLoaderSimple`、`WanAnimatePlus VAELoader`、`WanAnimatePlus ContextOptions`、`CLIPTextEncode`、`SCAIL2ColoredMask`、`easy imageRemBg`、`Switch any [Crystools]`、`WanAnimatePlus SCAIL_2 Embeds`、`WanAnimatePlus TextEncodeCached`、`VHS_VideoInfoLoaded`、`easy boolean`、`WanAnimatePlus BlockSwap`、`VHS_LoadVideo`、`LoadImage`、`ImageConcanate`、`GetImageRangeFromBatch`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanAnimatePlus Sampler、WanAnimatePlus ClipVisionEncode、WanAnimatePlus Decode、WanAnimatePlus TextEncodeCached、WanAnimatePlus VAELoader
