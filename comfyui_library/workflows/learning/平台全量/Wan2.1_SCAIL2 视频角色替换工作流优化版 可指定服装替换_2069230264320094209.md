---
key: 平台全量/Wan2.1_SCAIL2 视频角色替换工作流优化版 可指定服装替换_2069230264320094209.json
name: Wan2.1_SCAIL2 视频角色替换工作流优化版 可指定服装替换_2069230264320094209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1_SCAIL2 视频角色替换工作流优化版 可指定服装替换_2069230264320094209.json
hash: c2bec4a2bb6d6b51
coverage: 0.44697
learned_at: 2026-11-14 01:04:42
nodes: [GetNode, VAELoader, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, SetNode, BasicScheduler, GetNode, VAEDecode, SetNode, GetNode, SetNode, CLIPTextEncode, easy forLoopStart, easy forLoopEnd, GetNode, GetNode, easy batchAnything, GetNode, GetNode, GetNode, GetImageRangeFromBatch, SetNode, GetNode, VAEDecode, GetImageRangeFromBatch, SamplerCustom, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ModelSamplingSD3, SetNode, SetNode, CLIPLoader, GetNode, SetNode, CLIPVisionEncode, GetNode, GetNode, SetNode, SetNode, GetNode, ImageConcatMulti, GetNode, VHS_VideoCombine, GetNode, MathExpression|pysssss, SetNode, easy showAnything, SetNode, SetNode, SetNode, SetNode, SetNode, Int, Int, SetNode, SetNode, GetNode, VHS_VideoCombine, SetNode, Note, CLIPTextEncode, GetNode, SamplerCustom, SetNode, SetNode, GetNode, easy imageRemBg, DiffusionModelLoaderKJ, GetNode, VHS_VideoCombine, SetNode, LoraLoaderModelOnly, CR Text, SetNode, WanSCAILToVideo, LoadImage, GetNode, Int, SAM3_VideoTrack, HAIGC_VideoFrameRelay, PreviewImage, GetNode, GetNode, VHS_VideoInfoLoaded, SeCModelLoader, VHS_VideoCombine, WanSCAILToVideo, AddMask, Int, HAIGC_VideoFrameRelay, ImageToMask, Mask To Image (mtb), GetNode, GetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, PointsEditor, LayerUtility: ImageScaleByAspectRatio V2, SeCVideoSegmentation, MaskToImage, Image Blank, ImageToMask, CheckpointLoaderSimple, SCAIL2ColoredMask, SAM3_VideoTrack, SAM3_TrackToMask, PreviewImage, VHS_VideoCombine, CLIPTextEncode, GoogleTranslator, CLIPTextEncode, GetNode, GoogleTranslator]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/Wan2.1_SCAIL2 视频角色替换工作流优化版 可指定服装替换_2069230264320094209.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1_SCAIL2 视频角色替换工作流优化版 可指定服装替换_2069230264320094209.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（132 个）：
- `GetNode`
- `VAELoader`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `BasicScheduler`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `easy forLoopStart`
- `easy forLoopEnd`
- `GetNode`
- `GetNode`
- `easy batchAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `SamplerCustom` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `CLIPVisionEncode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `MathExpression|pysssss`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `Note`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SamplerCustom` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `easy imageRemBg`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `SetNode`
- `WanSCAILToVideo`
- `LoadImage`
- `GetNode`
- `Int`
- `SAM3_VideoTrack`
- `HAIGC_VideoFrameRelay`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `VHS_VideoInfoLoaded`
- `SeCModelLoader`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `AddMask`
- `Int`
- `HAIGC_VideoFrameRelay`
- `ImageToMask`
- `Mask To Image (mtb)`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `PointsEditor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeCVideoSegmentation`
- `MaskToImage`
- `Image Blank`
- `ImageToMask`
- `CheckpointLoaderSimple` ★核心
- `SCAIL2ColoredMask`
- `SAM3_VideoTrack`
- `SAM3_TrackToMask`
- `PreviewImage`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `GoogleTranslator`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GoogleTranslator`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **45%**（59/132）

**有卡**：`VAELoader`、`CLIPVisionLoader`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`CLIPTextEncode`、`easy forLoopStart`、`easy forLoopEnd`、`easy batchAnything`、`GetImageRangeFromBatch`、`SamplerCustom`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPVisionEncode`、`ImageConcatMulti`、`VHS_VideoCombine`、`MathExpression|pysssss`、`Int`、`easy imageRemBg`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`CR Text`、`WanSCAILToVideo`、`LoadImage`、`SAM3_VideoTrack`、`HAIGC_VideoFrameRelay`、`VHS_VideoInfoLoaded`、`SeCModelLoader`、`AddMask`、`ImageToMask`、`Mask To Image (mtb)`、`VHS_LoadVideo`、`PointsEditor`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeCVideoSegmentation`、`MaskToImage`、`Image Blank`、`CheckpointLoaderSimple`、`SCAIL2ColoredMask`、`SAM3_TrackToMask`、`GoogleTranslator`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、CLIPTextEncode、LoadImage、KSamplerSelect
