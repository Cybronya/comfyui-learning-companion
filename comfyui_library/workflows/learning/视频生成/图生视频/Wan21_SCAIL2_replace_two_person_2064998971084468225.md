---
key: 视频生成/图生视频/Wan21_SCAIL2_replace_two_person_2064998971084468225.json
name: Wan21_SCAIL2_replace_two_person_2064998971084468225.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan21_SCAIL2_replace_two_person_2064998971084468225.json
hash: 155823d5f246f464
coverage: 0.391753
learned_at: 2026-10-15 22:39:33
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanSCAILToVideo, GetNode, GetNode, DiffusionModelLoaderKJ, MarkdownNote, CLIPVisionLoader, SetNode, SetNode, SetNode, CLIPLoader, VAELoader, SetNode, CLIPVisionEncode, SetNode, GetNode, GetNode, SetNode, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanSCAILToVideo, GetNode, GetNode, GetNode, SamplerCustom, GetNode, VAEDecode, GetImageRangeFromBatch, GetNode, GetImageRangeFromBatch, ColorTransfer, GetImageSize, ImageFromBatch, GetNode, ImageConcatMulti, BatchImagesNode, CLIPTextEncode, LoraLoaderModelOnly, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, ModelSamplingSD3, BasicScheduler, KSamplerSelect, SetNode, VAEDecode, GetNode, SetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, SamplerCustom, ImageResizeKJv2, GetNode, GetNode, CheckpointLoaderSimple, SCAIL2ColoredMask, GetNode, SetNode, LoadImage, PrimitiveBoolean, CLIPTextEncode, CLIPTextEncode, SAM3_VideoTrack, SAM3_VideoTrack, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 视频生成/图生视频/Wan21_SCAIL2_replace_two_person_2064998971084468225.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064998971084468225.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
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
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
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
- `PreviewImage`
- `SamplerCustom` ★核心
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `SCAIL2ColoredMask`
- `GetNode`
- `SetNode`
- `LoadImage`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **39%**（38/97）

**有卡**：`WanSCAILToVideo`、`DiffusionModelLoaderKJ`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`SamplerCustom`、`VAEDecode`、`GetImageRangeFromBatch`、`ColorTransfer`、`GetImageSize`、`ImageFromBatch`、`ImageConcatMulti`、`BatchImagesNode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`BasicScheduler`、`KSamplerSelect`、`VHS_VideoCombine`、`ImageResizeKJv2`、`CheckpointLoaderSimple`、`SCAIL2ColoredMask`、`LoadImage`、`PrimitiveBoolean`、`SAM3_VideoTrack`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect
