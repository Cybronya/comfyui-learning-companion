---
key: 视频生成/图生视频/图生视频（适合Lora搭配）_Wan2.2_KJ_2021871450138873858.json
name: 图生视频（适合Lora搭配）_Wan2.2_KJ_2021871450138873858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2021871450138873858.json
hash: 9ae9a1a534062e77
coverage: 0.622222
learned_at: 2026-10-15 22:35:09
nodes: [Note, Reroute, WanVideoDecode, easy int, Reroute, Reroute, LoadWanVideoT5TextEncoder, Reroute, Reroute, easy cleanGpuUsed, Reroute, Reroute, Reroute, WanVideoBlockSwap, WanVideoVAELoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoSampler, FastUnsharpSharpen, MathExpression_UTK, ImpactInt, easy cleanGpuUsed, INTConstant, CreateCFGScheduleFloatList, WanVideoTextEncode, WanVideoImageToVideoEncode, INTConstant, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, LayerUtility: ImageScaleByAspectRatio V2, Reroute, CR Text, WanVideoLoraSelect, Note, WanVideoSLG, WanVideoEnhanceAVideo, VHS_VideoCombine, LoadImage, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频（适合Lora搭配）_Wan2.2_KJ_2021871450138873858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2021871450138873858.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `Note`
- `Reroute`
- `WanVideoDecode`
- `easy int`
- `Reroute`
- `Reroute`
- `LoadWanVideoT5TextEncoder`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoSampler` ★核心
- `FastUnsharpSharpen`
- `MathExpression_UTK`
- `ImpactInt`
- `easy cleanGpuUsed`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `CR Text`
- `WanVideoLoraSelect`
- `Note`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **62%**（28/45）

**有卡**：`WanVideoDecode`、`easy int`、`LoadWanVideoT5TextEncoder`、`easy cleanGpuUsed`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSampler`、`FastUnsharpSharpen`、`MathExpression_UTK`、`ImpactInt`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
