---
key: 视频生成/文生视频/【丝滑补帧】Wan2.1 图生视频  KJ加强表情自然不崩脸_1927553770740146177.json
name: 【丝滑补帧】Wan2.1 图生视频  KJ加强表情自然不崩脸_1927553770740146177.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1927553770740146177.json
hash: 9ce0f43a14f7a7c7
coverage: 0.88
learned_at: 2026-10-15 22:43:25
nodes: [WanVideoBlockSwap, WanVideoClipVisionEncode, ImageUpscaleWithModel, PrimitiveInt, easy cleanGpuUsed, UpscaleModelLoader, RIFE VFI, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadImage, WanVideoModelLoader, WanVideoSLG, WanVideoImageToVideoEncode, WanVideoTorchCompileSettings, WanVideoTextEncode, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoDecode, easy cleanGpuUsed, WanVideoExperimentalArgs, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, JjkText, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/文生视频/【丝滑补帧】Wan2.1 图生视频  KJ加强表情自然不崩脸_1927553770740146177.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1927553770740146177.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `ImageUpscaleWithModel`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `UpscaleModelLoader`
- `RIFE VFI`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoImageToVideoEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `JjkText`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`ImageUpscaleWithModel`、`easy cleanGpuUsed`、`UpscaleModelLoader`、`RIFE VFI`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadImage`、`WanVideoModelLoader`、`WanVideoSLG`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
