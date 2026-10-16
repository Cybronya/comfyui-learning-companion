---
key: 视频生成/图生视频/Wan2.2-首尾帧-kj优化加速版_1954893685562359810.json
name: Wan2.2-首尾帧-kj优化加速版_1954893685562359810.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1954893685562359810.json
hash: f8d971b78a67067e
coverage: 0.918919
learned_at: 2026-10-15 22:31:07
nodes: [RH_Translator, easy showAnything, ImageStitch, DF_Integer, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoTextEncode, SimpleMath+, WanVideoSampler, easy cleanGpuUsed, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, RH_Captioner, easy int, LoadImage, LoadImage, easy showAnything, LoadWanVideoClipTextEncoder, LayerUtility: ImageMaskScaleAs, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoDecode, VHS_VideoCombine, WanVideoVAELoader, WanVideoImageToVideoEncode, CreateCFGScheduleFloatList, CogVideoEnhanceAVideo, WanVideoSLG, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-首尾帧-kj优化加速版_1954893685562359810.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954893685562359810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（37 个）：
- `RH_Translator`
- `easy showAnything`
- `ImageStitch`
- `DF_Integer`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_Captioner`
- `easy int`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `LoadWanVideoClipTextEncoder` ★核心
- `LayerUtility: ImageMaskScaleAs`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `CreateCFGScheduleFloatList`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `MarkdownNote`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`RH_Translator`、`ImageStitch`、`DF_Integer`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoTextEncode`、`SimpleMath+`、`WanVideoSampler`、`easy cleanGpuUsed`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Captioner`、`easy int`、`LoadImage`、`LoadWanVideoClipTextEncoder`、`LayerUtility: ImageMaskScaleAs`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`CreateCFGScheduleFloatList`、`CogVideoEnhanceAVideo`、`WanVideoSLG`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
