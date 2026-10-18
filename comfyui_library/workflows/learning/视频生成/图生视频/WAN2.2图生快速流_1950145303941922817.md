---
key: 视频生成/图生视频/WAN2.2图生快速流_1950145303941922817.json
name: WAN2.2图生快速流_1950145303941922817.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2图生快速流_1950145303941922817.json
hash: 13c2680a18f2ed5b
coverage: 0.84375
learned_at: 2026-10-15 22:30:53
nodes: [WanVideoTextEncode, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoBlockSwap, VHS_VideoCombine, GetImageSizeAndCount, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoSetBlockSwap, INTConstant, CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, MathExpression|pysssss, MathExpression|pysssss, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, WanVideoSampler, Reroute, Reroute, WanVideoSampler, Reroute, Reroute, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, PrimitiveStringMultiline, ImpactInt]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2图生快速流_1950145303941922817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950145303941922817.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `WanVideoTextEncode`
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `Reroute`
- `Reroute`
- `WanVideoSampler` ★核心
- `Reroute`
- `Reroute`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ImpactInt`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`INTConstant`、`CreateCFGScheduleFloatList`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`、`MathExpression|pysssss`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoLoraSelect`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
