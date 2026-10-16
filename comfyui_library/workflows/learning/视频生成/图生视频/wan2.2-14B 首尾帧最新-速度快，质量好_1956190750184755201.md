---
key: 视频生成/图生视频/wan2.2-14B 首尾帧最新-速度快，质量好_1956190750184755201.json
name: wan2.2-14B 首尾帧最新-速度快，质量好_1956190750184755201.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956190750184755201.json
hash: 5f7c19be66db41fe
coverage: 0.911111
learned_at: 2026-10-15 22:31:12
nodes: [RH_Translator, easy showAnything, ImageStitch, easy showAnything, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoModelLoader, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, WanVideoVAELoader, WanVideoTextEncode, easy showAnything, WanVideoClipVisionEncode, WanVideoSLG, CogVideoEnhanceAVideo, SimpleMath+, LayerUtility: ImageMaskScaleAs, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSampler, easy cleanGpuUsed, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, RH_Captioner, Textbox, easy cleanGpuUsed, WanVideoImageToVideoEncode, easy ifElse, LoadWanVideoClipTextEncoder, CLIPVisionLoader, WanVideoModelLoader, easy int, Textbox, PrimitiveBoolean, DF_Integer, VHS_VideoCombine, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-14B 首尾帧最新-速度快，质量好_1956190750184755201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956190750184755201.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（45 个）：
- `RH_Translator`
- `easy showAnything`
- `ImageStitch`
- `easy showAnything`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `easy showAnything`
- `WanVideoClipVisionEncode`
- `WanVideoSLG`
- `CogVideoEnhanceAVideo`
- `SimpleMath+`
- `LayerUtility: ImageMaskScaleAs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_Captioner`
- `Textbox`
- `easy cleanGpuUsed`
- `WanVideoImageToVideoEncode`
- `easy ifElse`
- `LoadWanVideoClipTextEncoder` ★核心
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `easy int`
- `Textbox`
- `PrimitiveBoolean`
- `DF_Integer`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **91%**（41/45）

**有卡**：`RH_Translator`、`ImageStitch`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoModelLoader`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`WanVideoSLG`、`CogVideoEnhanceAVideo`、`SimpleMath+`、`LayerUtility: ImageMaskScaleAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Captioner`、`Textbox`、`WanVideoImageToVideoEncode`、`LoadWanVideoClipTextEncoder`、`CLIPVisionLoader`、`easy int`、`PrimitiveBoolean`、`DF_Integer`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
