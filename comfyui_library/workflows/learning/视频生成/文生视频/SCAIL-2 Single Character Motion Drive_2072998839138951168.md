---
key: 视频生成/文生视频/SCAIL-2 Single Character Motion Drive_2072998839138951168.json
name: SCAIL-2 Single Character Motion Drive_2072998839138951168
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Single Character Motion Drive_2072998839138951168.json
hash: f6dca2dea5b61153
coverage: 0.948276
learned_at: 2026-10-15 22:46:54
nodes: [MarkdownNote, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, PrimitiveNode, easy int, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, VAELoader, CLIPLoader, CLIPVisionLoader, CheckpointLoaderSimple, KSamplerSelect, BasicScheduler, CLIPVisionEncode, SAM3_VideoTrack, SAM3_VideoTrack, SCAIL2ColoredMask, easy mathInt, easy mathInt, easy mathInt, easy int, easy compare, easy ifElse, WanSCAILToVideo, SamplerCustom, VAEDecode, easy forLoopStart, WanSCAILToVideo, SamplerCustom, VAEDecode, GetImageRangeFromBatch, GetImageRangeFromBatch, ColorTransfer, easy forLoopEnd, EmptyImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, BatchImagesNode, Int, VHS_LoadVideo, ImageResizeKJv2, Int, Int, ImageResizeKJv2, LoraLoaderModelOnly, LoadImage, ImageCompositeMasked, SAM3_TrackToMask, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 视频生成/文生视频/SCAIL-2 Single Character Motion Drive_2072998839138951168.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Single Character Motion Drive_2072998839138951168.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（58 个）：
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `easy int`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CLIPVisionEncode`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy int`
- `easy compare`
- `easy ifElse`
- `WanSCAILToVideo`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `easy forLoopStart`
- `WanSCAILToVideo`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `ColorTransfer`
- `easy forLoopEnd`
- `EmptyImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BatchImagesNode`
- `Int`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ImageCompositeMasked`
- `SAM3_TrackToMask`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **95%**（55/58）

**有卡**：`CLIPTextEncode`、`easy int`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`KSamplerSelect`、`BasicScheduler`、`CLIPVisionEncode`、`SAM3_VideoTrack`、`SCAIL2ColoredMask`、`easy mathInt`、`easy compare`、`WanSCAILToVideo`、`SamplerCustom`、`VAEDecode`、`easy forLoopStart`、`GetImageRangeFromBatch`、`ColorTransfer`、`easy forLoopEnd`、`EmptyImage`、`BatchImagesNode`、`Int`、`VHS_LoadVideo`、`ImageResizeKJv2`、`LoadImage`、`ImageCompositeMasked`、`SAM3_TrackToMask`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
