---
key: 视频生成/文生视频/SCAIL-2 Triple Character Motion Drive_2072998837192794112.json
name: SCAIL-2 Triple Character Motion Drive_2072998837192794112
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Triple Character Motion Drive_2072998837192794112.json
hash: cd60172e2655e52e
coverage: 0.8
learned_at: 2026-10-11 20:21:29
nodes: [MarkdownNote, CLIPTextEncode, CLIPTextEncode, PrimitiveNode, easy int, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, VAELoader, CLIPLoader, CLIPVisionLoader, CheckpointLoaderSimple, KSamplerSelect, BasicScheduler, CLIPVisionEncode, SAM3_VideoTrack, SAM3_VideoTrack, SCAIL2ColoredMask, easy mathInt, easy mathInt, easy mathInt, easy int, easy compare, easy ifElse, WanSCAILToVideo, SamplerCustom, VAEDecode, easy forLoopStart, WanSCAILToVideo, SamplerCustom, VAEDecode, GetImageRangeFromBatch, GetImageRangeFromBatch, ColorTransfer, BatchImagesNode, easy forLoopEnd, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, ImageResizeKJv2, Int, ImageResizeKJv2, Int, LoraLoaderModelOnly, Int, VHS_LoadVideo, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: [easy compare, easy forLoopEnd, easy forLoopStart, easy int, easy int, easy mathInt, easy mathInt, easy mathInt]
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
discoveries: [次要节点 `easy compare` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/SCAIL-2 Triple Character Motion Drive_2072998837192794112.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Triple Character Motion Drive_2072998837192794112.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
- `MarkdownNote`
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
- `BatchImagesNode`
- `easy forLoopEnd`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `Int`
- `ImageResizeKJv2`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `Int`
- `VHS_LoadVideo`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **80%**（44/55）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`KSamplerSelect`、`BasicScheduler`、`CLIPVisionEncode`、`SAM3_VideoTrack`、`SCAIL2ColoredMask`、`WanSCAILToVideo`、`SamplerCustom`、`VAEDecode`、`GetImageRangeFromBatch`、`ColorTransfer`、`BatchImagesNode`、`VHS_VideoCombine`、`ImageResizeKJv2`、`Int`、`VHS_LoadVideo`、`LoadImage`

**缺卡**（8）：`easy compare`、`easy forLoopEnd`、`easy forLoopStart`、`easy int`、`easy int`、`easy mathInt`、`easy mathInt`、`easy mathInt`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 学习发现

- 次要节点 `easy compare` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
