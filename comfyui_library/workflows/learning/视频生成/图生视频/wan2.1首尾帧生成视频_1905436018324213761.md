---
key: 视频生成/图生视频/wan2.1首尾帧生成视频_1905436018324213761.json
name: wan2.1首尾帧生成视频_1905436018324213761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1首尾帧生成视频_1905436018324213761.json
hash: 0c1c70ff6ef4c429
coverage: 0.972973
learned_at: 2026-10-15 22:29:26
nodes: [WanVideoTextEncode, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, WanVideoTorchCompileSettings, LoadWanVideoClipTextEncoder, easy cleanGpuUsed, CM_IntBinaryOperation, Note, easy cleanGpuUsed, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTeaCache, Text _O, AspectRatioSelector, WanVideoExperimentalArgs, CR Text, Bjornulf_ShowInt, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, Bjornulf_ShowInt, LoadImage, LoadImage, WanVideoSampler, VHS_VideoCombine, easy cleanGpuUsed, WanVideoDecode, DF_Int_to_Float, WanVideoSLG, LayerUtility: ImageScaleByAspectRatio, LayerUtility: ImageScaleByAspectRatio, CM_IntBinaryOperation, int _O, DF_Integer, WanVideoImageToVideoEncode, WanVideoVAELoader, WanVideoClipVisionEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1首尾帧生成视频_1905436018324213761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1905436018324213761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoClipTextEncoder` ★核心
- `easy cleanGpuUsed`
- `CM_IntBinaryOperation`
- `Note`
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTeaCache`
- `Text _O`
- `AspectRatioSelector`
- `WanVideoExperimentalArgs`
- `CR Text`
- `Bjornulf_ShowInt`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Bjornulf_ShowInt`
- `LoadImage`
- `LoadImage`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `DF_Int_to_Float`
- `WanVideoSLG`
- `LayerUtility: ImageScaleByAspectRatio`
- `LayerUtility: ImageScaleByAspectRatio`
- `CM_IntBinaryOperation`
- `int _O`
- `DF_Integer`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`easy cleanGpuUsed`、`WanVideoTorchCompileSettings`、`LoadWanVideoClipTextEncoder`、`CM_IntBinaryOperation`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTeaCache`、`Text _O`、`AspectRatioSelector`、`WanVideoExperimentalArgs`、`CR Text`、`Bjornulf_ShowInt`、`LoadImage`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoDecode`、`DF_Int_to_Float`、`WanVideoSLG`、`LayerUtility: ImageScaleByAspectRatio`、`int _O`、`DF_Integer`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
