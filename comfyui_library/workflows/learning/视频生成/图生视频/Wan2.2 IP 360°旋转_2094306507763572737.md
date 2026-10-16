---
key: 视频生成/图生视频/Wan2.2 IP 360°旋转_2094306507763572737.json
name: Wan2.2 IP 360°旋转_2094306507763572737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 IP 360°旋转_2094306507763572737.json
hash: 4ccf34e68812f1d3
coverage: 1
learned_at: 2026-10-16 23:42:29
nodes: [WanVideoMagCache, WanVideoEnhanceAVideo, SimpleMath+, SimpleMath+, Float, DF_Get_image_size, ImageResize, WanVideoClipVisionEncode, LoadWanVideoClipTextEncoder, LayerUtility: PurgeVRAM, LoadWanVideoT5TextEncoder, Float to Int, WanVideoTextEncode, WanVideoImageToVideoEncode, WanVideoSLG, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, INTConstant, INTConstant, LayerUtility: PurgeVRAM, WanVideoVAELoader, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoDecode, WanVideoModelLoader, WanVideoLoraSelectMulti, Float, VHS_VideoCombine, Text, math_calculate, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 IP 360°旋转_2094306507763572737.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2 IP 360°旋转_2094306507763572737.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoMagCache`
- `WanVideoEnhanceAVideo`
- `SimpleMath+`
- `SimpleMath+`
- `Float`
- `DF_Get_image_size`
- `ImageResize`
- `WanVideoClipVisionEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `LayerUtility: PurgeVRAM`
- `LoadWanVideoT5TextEncoder`
- `Float to Int`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `INTConstant`
- `LayerUtility: PurgeVRAM`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `Float`
- `VHS_VideoCombine`
- `Text`
- `math_calculate`
- `LoadImage`

## 知识

覆盖率 **100%**（35/35）

**有卡**：`WanVideoMagCache`、`WanVideoEnhanceAVideo`、`SimpleMath+`、`Float`、`DF_Get_image_size`、`ImageResize`、`WanVideoClipVisionEncode`、`LoadWanVideoClipTextEncoder`、`LayerUtility: PurgeVRAM`、`LoadWanVideoT5TextEncoder`、`Float to Int`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoSLG`、`WanVideoSampler`、`INTConstant`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`Text`、`math_calculate`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
