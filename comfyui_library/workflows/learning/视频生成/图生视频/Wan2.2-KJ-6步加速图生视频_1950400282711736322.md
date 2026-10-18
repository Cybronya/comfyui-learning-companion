---
key: 视频生成/图生视频/Wan2.2-KJ-6步加速图生视频_1950400282711736322.json
name: Wan2.2-KJ-6步加速图生视频_1950400282711736322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-KJ-6步加速图生视频_1950400282711736322.json
hash: 2f8cfa4130ebdc59
coverage: 0.852941
learned_at: 2026-10-15 22:30:54
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, Reroute, WanVideoSetLoRAs, WanVideoSetBlockSwap, Reroute, Reroute, WanVideoSampler, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, Reroute, VHS_VideoCombine, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, CreateCFGScheduleFloatList, easy seed, WanVideoSampler, MathExpression|pysssss, WanVideoVAELoader, WanVideoTextEncode, DF_Integer, DF_Integer, DF_Integer, DF_Integer, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, WanVideoImageToVideoEncode, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-KJ-6步加速图生视频_1950400282711736322.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950400282711736322.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `Reroute`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `Reroute`
- `Reroute`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `Reroute`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `easy seed`
- `WanVideoSampler` ★核心
- `MathExpression|pysssss`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `DF_Integer`
- `DF_Integer`
- `DF_Integer`
- `DF_Integer`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **85%**（29/34）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`easy seed`、`MathExpression|pysssss`、`WanVideoVAELoader`、`WanVideoTextEncode`、`DF_Integer`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
