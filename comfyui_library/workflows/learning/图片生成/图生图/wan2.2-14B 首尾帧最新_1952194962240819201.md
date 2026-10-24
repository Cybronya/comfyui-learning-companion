---
key: 图片生成/图生图/wan2.2-14B 首尾帧最新_1952194962240819201.json
name: wan2.2-14B 首尾帧最新_1952194962240819201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2-14B 首尾帧最新_1952194962240819201.json
hash: d2518d3e8831661b
coverage: 0.904762
learned_at: 2026-10-23 11:45:58
nodes: [RH_Translator, easy showAnything, PrimitiveBoolean, ImageStitch, RH_Captioner, DF_Integer, Textbox, easy showAnything, LoadWanVideoClipTextEncoder, easy ifElse, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoModelLoader, easy cleanGpuUsed, VHS_VideoCombine, easy cleanGpuUsed, WanVideoDecode, WanVideoVAELoader, WanVideoTextEncode, easy showAnything, WanVideoSLG, CogVideoEnhanceAVideo, SimpleMath+, LayerUtility: ImageMaskScaleAs, easy int, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSampler, easy cleanGpuUsed, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, WanVideoClipVisionEncode]
patterns: []
missing: []
---

# 图片生成/图生图/wan2.2-14B 首尾帧最新_1952194962240819201.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2-14B 首尾帧最新_1952194962240819201.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（42 个）：
- `RH_Translator`
- `easy showAnything`
- `PrimitiveBoolean`
- `ImageStitch`
- `RH_Captioner`
- `DF_Integer`
- `Textbox`
- `easy showAnything`
- `LoadWanVideoClipTextEncoder` ★核心
- `easy ifElse`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `easy showAnything`
- `WanVideoSLG`
- `CogVideoEnhanceAVideo`
- `SimpleMath+`
- `LayerUtility: ImageMaskScaleAs`
- `easy int`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `WanVideoClipVisionEncode`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`RH_Translator`、`PrimitiveBoolean`、`ImageStitch`、`RH_Captioner`、`DF_Integer`、`Textbox`、`LoadWanVideoClipTextEncoder`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoSLG`、`CogVideoEnhanceAVideo`、`SimpleMath+`、`LayerUtility: ImageMaskScaleAs`、`easy int`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoClipVisionEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
