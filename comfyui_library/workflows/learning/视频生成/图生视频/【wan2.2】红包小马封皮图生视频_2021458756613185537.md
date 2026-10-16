---
key: 视频生成/图生视频/【wan2.2】红包小马封皮图生视频_2021458756613185537.json
name: 【wan2.2】红包小马封皮图生视频_2021458756613185537.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2021458756613185537.json
hash: c69d17fbd0863e22
coverage: 0.673913
learned_at: 2026-10-15 22:35:08
nodes: [GetNode, LoadImage, CLIPVisionLoader, GetNode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Fast Muter (rgthree), Fast Muter (rgthree), LayerUtility: ImageScaleByAspectRatio V2, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, GetNode, GetNode, GetNode, GetNode, GetNode, Label (rgthree), Label (rgthree), WanVideoDecode, SetNode, WanVideoEnhanceAVideo, FL_Math, Label (rgthree), Label (rgthree), SetNode, SetNode, SetNode, SetNode, GetNode, Note, Note, VHS_VideoCombine, RIFE VFI, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoTeaCache, WanVideoBlockSwap, WanVideoTextEncode, WanVideoSampler, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/【wan2.2】红包小马封皮图生视频_2021458756613185537.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2021458756613185537.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `GetNode`
- `LoadImage`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `Fast Muter (rgthree)`
- `Fast Muter (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoDecode`
- `SetNode`
- `WanVideoEnhanceAVideo`
- `FL_Math`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `RIFE VFI`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **67%**（31/46）

**有卡**：`LoadImage`、`CLIPVisionLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`Fast Muter (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`Label (rgthree)`、`WanVideoDecode`、`WanVideoEnhanceAVideo`、`FL_Math`、`VHS_VideoCombine`、`RIFE VFI`、`LayerUtility: PurgeVRAM`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
