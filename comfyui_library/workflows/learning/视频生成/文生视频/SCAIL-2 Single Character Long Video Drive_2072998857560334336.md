---
key: 视频生成/文生视频/SCAIL-2 Single Character Long Video Drive_2072998857560334336.json
name: SCAIL-2 Single Character Long Video Drive_2072998857560334336
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Single Character Long Video Drive_2072998857560334336.json
hash: a2930a87c7acc1f5
coverage: 0.945455
learned_at: 2026-10-15 22:46:54
nodes: [MarkdownNote, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, easy int, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, VAELoader, CLIPLoader, CLIPVisionLoader, CheckpointLoaderSimple, KSamplerSelect, BasicScheduler, CLIPVisionEncode, SAM3_VideoTrack, SAM3_VideoTrack, easy mathInt, easy mathInt, easy mathInt, easy int, easy compare, easy ifElse, SamplerCustom, VAEDecode, easy forLoopStart, WanSCAILToVideo, SamplerCustom, VAEDecode, GetImageRangeFromBatch, GetImageRangeFromBatch, ColorTransfer, BatchImagesNode, easy forLoopEnd, VHS_VideoCombine, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_LoadVideo, LoraLoaderModelOnly, VHS_VideoCombine, WanSCAILToVideo, PrimitiveNode, LoadImage, SCAIL2ColoredMask, Int, ImageResizeKJv2, ImageResizeKJv2, Int, Int]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 视频生成/文生视频/SCAIL-2 Single Character Long Video Drive_2072998857560334336.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Single Character Long Video Drive_2072998857560334336.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
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
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy int`
- `easy compare`
- `easy ifElse`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `easy forLoopStart`
- `WanSCAILToVideo`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `ColorTransfer`
- `BatchImagesNode`
- `easy forLoopEnd`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideo`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `PrimitiveNode`
- `LoadImage`
- `SCAIL2ColoredMask`
- `Int`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Int`
- `Int`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **95%**（52/55）

**有卡**：`CLIPTextEncode`、`easy int`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`KSamplerSelect`、`BasicScheduler`、`CLIPVisionEncode`、`SAM3_VideoTrack`、`easy mathInt`、`easy compare`、`SamplerCustom`、`VAEDecode`、`easy forLoopStart`、`WanSCAILToVideo`、`GetImageRangeFromBatch`、`ColorTransfer`、`BatchImagesNode`、`easy forLoopEnd`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`SCAIL2ColoredMask`、`Int`、`ImageResizeKJv2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
