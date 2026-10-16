---
key: 视频生成/图生视频/Wan21_SCAIL2_kimoto_no_replace_2066352425379909633.json
name: Wan21_SCAIL2_kimoto_no_replace_2066352425379909633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2066352425379909633.json
hash: a57c6fa3c4dcb927
coverage: 0.375
learned_at: 2026-10-15 22:39:48
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanSCAILToVideo, GetNode, GetNode, DiffusionModelLoaderKJ, MarkdownNote, CLIPVisionLoader, SetNode, SetNode, SetNode, CLIPLoader, VAELoader, SetNode, CLIPVisionEncode, SetNode, GetNode, GetNode, SetNode, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanSCAILToVideo, GetNode, GetNode, GetNode, SamplerCustom, GetNode, VAEDecode, GetImageRangeFromBatch, GetNode, GetImageRangeFromBatch, ColorTransfer, GetImageSize, ImageFromBatch, GetNode, ImageConcatMulti, BatchImagesNode, CLIPTextEncode, LoraLoaderModelOnly, SetNode, SetNode, SetNode, SetNode, CheckpointLoaderSimple, CLIPTextEncode, SAM3_VideoTrack, GetNode, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, PrimitiveNode, GetNode, GetNode, SetNode, ModelSamplingSD3, BasicScheduler, KSamplerSelect, SetNode, VAEDecode, GetNode, SetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, GetNode, GetNode, SamplerCustom, VHS_LoadVideo, ImageResizeKJv2, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 视频生成/图生视频/Wan21_SCAIL2_kimoto_no_replace_2066352425379909633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066352425379909633.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（96 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanSCAILToVideo`
- `GetNode`
- `GetNode`
- `DiffusionModelLoaderKJ`
- `MarkdownNote`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `CLIPVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `WanSCAILToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustom` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `GetNode`
- `GetImageRangeFromBatch`
- `ColorTransfer`
- `GetImageSize`
- `ImageFromBatch`
- `GetNode`
- `ImageConcatMulti`
- `BatchImagesNode`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `SAM3_VideoTrack`
- `GetNode`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ModelSamplingSD3`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `SamplerCustom` ★核心
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `LoadImage`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **38%**（36/96）

**有卡**：`WanSCAILToVideo`、`DiffusionModelLoaderKJ`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`SamplerCustom`、`VAEDecode`、`GetImageRangeFromBatch`、`ColorTransfer`、`GetImageSize`、`ImageFromBatch`、`ImageConcatMulti`、`BatchImagesNode`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`SAM3_VideoTrack`、`SCAIL2ColoredMask`、`ModelSamplingSD3`、`BasicScheduler`、`KSamplerSelect`、`VHS_VideoCombine`、`VHS_LoadVideo`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect
