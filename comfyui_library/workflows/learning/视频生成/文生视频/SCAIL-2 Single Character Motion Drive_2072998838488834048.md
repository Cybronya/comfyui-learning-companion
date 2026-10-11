---
key: 视频生成/文生视频/SCAIL-2 Single Character Motion Drive_2072998838488834048.json
name: SCAIL-2 Single Character Motion Drive_2072998838488834048
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Single Character Motion Drive_2072998838488834048.json
hash: 45d0e9fe96abec42
coverage: 0.807018
learned_at: 2026-10-11 20:21:29
nodes: [MarkdownNote, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, VAELoader, CLIPVisionLoader, CheckpointLoaderSimple, KSamplerSelect, BasicScheduler, CLIPVisionEncode, SAM3_VideoTrack, SAM3_VideoTrack, easy mathInt, easy mathInt, easy mathInt, easy int, easy compare, easy ifElse, SamplerCustom, VAEDecode, easy forLoopStart, WanSCAILToVideo, SamplerCustom, VAEDecode, GetImageRangeFromBatch, GetImageRangeFromBatch, ColorTransfer, BatchImagesNode, easy forLoopEnd, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, PrimitiveNode, SCAIL2ColoredMask, Int, ImageResizeKJv2, ImageResizeKJv2, Int, Int, LoraLoaderModelOnly, LoadImage, UnetLoaderGGUF, CLIPLoaderGGUF, CLIPLoader, easy int, VHS_VideoCombine]
patterns: []
missing: [easy compare, easy forLoopEnd, easy forLoopStart, easy int, easy int, easy mathInt, easy mathInt, easy mathInt]
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
discoveries: [次要节点 `easy compare` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/SCAIL-2 Single Character Motion Drive_2072998838488834048.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SCAIL-2 Single Character Motion Drive_2072998838488834048.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（57 个）：
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAELoader`
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `PrimitiveNode`
- `SCAIL2ColoredMask`
- `Int`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Int`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `CLIPLoaderGGUF`
- `CLIPLoader`
- `easy int`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **81%**（46/57）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`KSamplerSelect`、`BasicScheduler`、`CLIPVisionEncode`、`SAM3_VideoTrack`、`SamplerCustom`、`VAEDecode`、`WanSCAILToVideo`、`GetImageRangeFromBatch`、`ColorTransfer`、`BatchImagesNode`、`VHS_VideoCombine`、`VHS_LoadVideo`、`SCAIL2ColoredMask`、`Int`、`ImageResizeKJv2`、`LoadImage`、`UnetLoaderGGUF`、`CLIPLoaderGGUF`、`CLIPLoader`

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
