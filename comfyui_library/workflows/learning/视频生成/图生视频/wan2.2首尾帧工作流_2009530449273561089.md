---
key: 视频生成/图生视频/wan2.2首尾帧工作流_2009530449273561089.json
name: wan2.2首尾帧工作流_2009530449273561089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2009530449273561089.json
hash: dd83baea1f07da50
coverage: 0.909091
learned_at: 2026-10-15 22:34:13
nodes: [RH_Translator, easy showAnything, ImageStitch, WanVideoSetBlockSwap, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, WanVideoVAELoader, WanVideoTextEncode, easy showAnything, WanVideoSLG, CogVideoEnhanceAVideo, SimpleMath+, WanVideoSampler, easy cleanGpuUsed, WanVideoSampler, RH_Captioner, easy cleanGpuUsed, WanVideoImageToVideoEncode, easy ifElse, CLIPVisionLoader, easy int, DF_Integer, VHS_VideoCombine, LoadImage, LoadImage, easy showAnything, Textbox, PrimitiveBoolean, WanVideoClipVisionEncode, LoadWanVideoClipTextEncoder, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2首尾帧工作流_2009530449273561089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009530449273561089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（44 个）：
- `RH_Translator`
- `easy showAnything`
- `ImageStitch`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `easy showAnything`
- `WanVideoSLG`
- `CogVideoEnhanceAVideo`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `RH_Captioner`
- `easy cleanGpuUsed`
- `WanVideoImageToVideoEncode`
- `easy ifElse`
- `CLIPVisionLoader`
- `easy int`
- `DF_Integer`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `Textbox`
- `PrimitiveBoolean`
- `WanVideoClipVisionEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`

## 知识

覆盖率 **91%**（40/44）

**有卡**：`RH_Translator`、`ImageStitch`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoModelLoader`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoSLG`、`CogVideoEnhanceAVideo`、`SimpleMath+`、`WanVideoSampler`、`RH_Captioner`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`easy int`、`DF_Integer`、`VHS_VideoCombine`、`LoadImage`、`Textbox`、`PrimitiveBoolean`、`WanVideoClipVisionEncode`、`LoadWanVideoClipTextEncoder`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAs`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
