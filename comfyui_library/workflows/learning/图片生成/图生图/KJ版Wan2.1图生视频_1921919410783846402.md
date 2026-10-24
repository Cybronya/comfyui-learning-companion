---
key: 图片生成/图生图/KJ版Wan2.1图生视频_1921919410783846402.json
name: KJ版Wan2.1图生视频_1921919410783846402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KJ版Wan2.1图生视频_1921919410783846402.json
hash: 6fbefab270ab87d8
coverage: 0.846154
learned_at: 2026-10-23 11:03:56
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoBlockSwap, ImageUpscaleWithModel, UpscaleModelLoader, Note, JjkText, VHS_VideoCombine, easy cleanGpuUsed, RIFE VFI, PrimitiveInt, easy cleanGpuUsed, CLIPVisionLoader, WanVideoDecode, WanVideoModelLoader, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoSampler, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Note]
patterns: []
missing: []
---

# 图片生成/图生图/KJ版Wan2.1图生视频_1921919410783846402.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KJ版Wan2.1图生视频_1921919410783846402.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（26 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `Note`
- `JjkText`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`RIFE VFI`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
