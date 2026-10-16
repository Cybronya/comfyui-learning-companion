---
key: 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版_2075046170388422658.json
name: wan2.2首尾帧kj图生视频+加速版_2075046170388422658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2075046170388422658.json
hash: 90cb50dd4e18d5e2
coverage: 0.95
learned_at: 2026-10-15 22:41:20
nodes: [LoadImage, LoadImage, VHS_VideoCombine, Note, CreateCFGScheduleFloatList, CR Text, easy clearCacheAll, WanVideoTextEncode, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM, easy cleanGpuUsed, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, MathExpression|pysssss, WanVideoVAELoader, INTConstant, WanVideoModelLoader, WanVideoSetLoRAs, ImageResizeKJv2, ImageResizeKJv2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSampler, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, PrimitiveFloat, Int, Int, WanVideoLoraSelect, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, WanVideoSampler, WanVideoImageToVideoEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版_2075046170388422658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075046170388422658.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `Note`
- `CreateCFGScheduleFloatList`
- `CR Text`
- `easy clearCacheAll`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `WanVideoVAELoader`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `PrimitiveFloat`
- `Int`
- `Int`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LoadImage`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`CR Text`、`easy clearCacheAll`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`、`MathExpression|pysssss`、`WanVideoVAELoader`、`INTConstant`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`Int`、`WanVideoLoraSelect`、`WanVideoDecode`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
