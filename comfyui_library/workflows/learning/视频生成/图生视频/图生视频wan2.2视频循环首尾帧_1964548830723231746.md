---
key: 视频生成/图生视频/图生视频wan2.2视频循环首尾帧_1964548830723231746.json
name: 图生视频wan2.2视频循环首尾帧_1964548830723231746.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频wan2.2视频循环首尾帧_1964548830723231746.json
hash: a3211539cf36a44a
coverage: 0.906977
learned_at: 2026-10-15 22:31:35
nodes: [LoadImage, RH_Translator, RH_Captioner, easy showAnything, ImageStitch, Textbox, easy ifElse, PrimitiveBoolean, easy showAnything, easy int, SimpleMath+, DF_Integer, WanVideoTextEncode, WanVideoImageToVideoEncode, easy showAnything, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, CreateCFGScheduleFloatList, easy cleanGpuUsed, WanVideoSampler, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, CogVideoEnhanceAVideo, WanVideoSLG, easy cleanGpuUsed, WanVideoVAELoader, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAs, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, LoadImage, easy cleanGpuUsed, WanVideoDecode, ColorMatchToReference]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频wan2.2视频循环首尾帧_1964548830723231746.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964548830723231746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（43 个）：
- `LoadImage`
- `RH_Translator`
- `RH_Captioner`
- `easy showAnything`
- `ImageStitch`
- `Textbox`
- `easy ifElse`
- `PrimitiveBoolean`
- `easy showAnything`
- `easy int`
- `SimpleMath+`
- `DF_Integer`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `easy showAnything`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `easy cleanGpuUsed`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAs`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `LoadImage`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `ColorMatchToReference`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`LoadImage`、`RH_Translator`、`RH_Captioner`、`ImageStitch`、`Textbox`、`PrimitiveBoolean`、`easy int`、`SimpleMath+`、`DF_Integer`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoBlockSwap`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoVAELoader`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAs`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`ColorMatchToReference`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
