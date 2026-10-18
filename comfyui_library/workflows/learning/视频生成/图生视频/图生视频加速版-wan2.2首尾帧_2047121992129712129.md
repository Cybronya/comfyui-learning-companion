---
key: 视频生成/图生视频/图生视频加速版-wan2.2首尾帧_2047121992129712129.json
name: 图生视频加速版-wan2.2首尾帧_2047121992129712129.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频加速版-wan2.2首尾帧_2047121992129712129.json
hash: 5a00413e314e8802
coverage: 0.974359
learned_at: 2026-10-15 22:37:02
nodes: [LoadImage, LoadImage, VHS_VideoCombine, CreateCFGScheduleFloatList, CR Text, easy clearCacheAll, WanVideoTextEncode, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM, easy cleanGpuUsed, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, MathExpression|pysssss, WanVideoVAELoader, INTConstant, WanVideoModelLoader, WanVideoSetLoRAs, ImageResizeKJv2, ImageResizeKJv2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSampler, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, PrimitiveFloat, Int, Int, WanVideoLoraSelect, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, WanVideoSampler, WanVideoImageToVideoEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频加速版-wan2.2首尾帧_2047121992129712129.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047121992129712129.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
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

覆盖率 **97%**（38/39）

**有卡**：`LoadImage`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`CR Text`、`easy clearCacheAll`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`、`MathExpression|pysssss`、`WanVideoVAELoader`、`INTConstant`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`Int`、`WanVideoLoraSelect`、`WanVideoDecode`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
