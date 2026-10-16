---
key: 视频生成/图生视频/wan2.2首尾帧——KJ流_1958363442241552386.json
name: wan2.2首尾帧——KJ流_1958363442241552386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958363442241552386.json
hash: c671ea012a2bb71b
coverage: 0.969697
learned_at: 2026-10-15 22:31:22
nodes: [WanVideoDecode, WanVideoEnhanceAVideo, UpscaleModelLoader, ImageScaleToMegapixels, WanVideoExperimentalArgs, WanVideoTeaCache, LayerUtility: ImageScaleByAspectRatio V2, WanVideoLoraSelect, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, WanVideoModelLoader, WanVideoTextEncode, PreviewImage, DownloadAndLoadGIMMVFIModel, WanVideoVAELoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoClipVisionEncode, WanVideoSampler, CreateCFGScheduleFloatList, Int, LoadImage, LoadImage, GIMMVFI_interpolate, WanVideoSLG, WanVideoImageToVideoEncode, Int, Int, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2首尾帧——KJ流_1958363442241552386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958363442241552386.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `UpscaleModelLoader`
- `ImageScaleToMegapixels`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `PreviewImage`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `Int`
- `LoadImage`
- `LoadImage`
- `GIMMVFI_interpolate`
- `WanVideoSLG`
- `WanVideoImageToVideoEncode`
- `Int`
- `Int`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`WanVideoDecode`、`WanVideoEnhanceAVideo`、`UpscaleModelLoader`、`ImageScaleToMegapixels`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoTextEncode`、`DownloadAndLoadGIMMVFIModel`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`CreateCFGScheduleFloatList`、`Int`、`LoadImage`、`GIMMVFI_interpolate`、`WanVideoSLG`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
