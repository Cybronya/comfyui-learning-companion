---
key: 视频生成/图生视频/KJ版-wan2.2-14B 首尾帧最新_1952043105937731585.json
name: KJ版-wan2.2-14B 首尾帧最新_1952043105937731585.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952043105937731585.json
hash: be6482bae4c70421
coverage: 0.904762
learned_at: 2026-10-15 22:30:59
nodes: [RH_Translator, easy showAnything, PrimitiveBoolean, ImageStitch, DF_Integer, LoadImage, easy showAnything, LoadWanVideoClipTextEncoder, easy ifElse, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoModelLoader, easy cleanGpuUsed, VHS_VideoCombine, easy cleanGpuUsed, WanVideoDecode, WanVideoVAELoader, WanVideoTextEncode, easy showAnything, WanVideoClipVisionEncode, WanVideoSLG, CogVideoEnhanceAVideo, SimpleMath+, LoadImage, LayerUtility: ImageMaskScaleAs, easy int, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSampler, easy cleanGpuUsed, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, RH_Captioner, Textbox]
patterns: []
missing: []
---

# 视频生成/图生视频/KJ版-wan2.2-14B 首尾帧最新_1952043105937731585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952043105937731585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（42 个）：
- `RH_Translator`
- `easy showAnything`
- `PrimitiveBoolean`
- `ImageStitch`
- `DF_Integer`
- `LoadImage`
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
- `WanVideoClipVisionEncode`
- `WanVideoSLG`
- `CogVideoEnhanceAVideo`
- `SimpleMath+`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAs`
- `easy int`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_Captioner`
- `Textbox`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`RH_Translator`、`PrimitiveBoolean`、`ImageStitch`、`DF_Integer`、`LoadImage`、`LoadWanVideoClipTextEncoder`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`WanVideoSLG`、`CogVideoEnhanceAVideo`、`SimpleMath+`、`LayerUtility: ImageMaskScaleAs`、`easy int`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Captioner`、`Textbox`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
