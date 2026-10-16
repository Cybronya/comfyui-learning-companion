---
key: 视频生成/图生视频/[泼水特效] WAN2.2 美女真实泼水换装 画风真实 运行流畅 可更换lora_1980795448254484481.json
name: [泼水特效] WAN2.2 美女真实泼水换装 画风真实 运行流畅 可更换lora_1980795448254484481.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980795448254484481.json
hash: 9c7a32c4d64b5018
coverage: 0.911765
learned_at: 2026-10-15 22:32:33
nodes: [MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, SimpleMath+, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, INTConstant, WanVideoDecode, WanVideoSampler, WanVideoSampler, WanVideoSetLoRAs, PrimitiveNode, JWInteger, Fast Groups Bypasser (rgthree), WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, easy int, WanVideoSetLoRAs, WanVideoImageToVideoEncode, DF_Integer, JjkText, LoadImage, GetImageSizeAndCount, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/[泼水特效] WAN2.2 美女真实泼水换装 画风真实 运行流畅 可更换lora_1980795448254484481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980795448254484481.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `SimpleMath+`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `JWInteger`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `easy int`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `DF_Integer`
- `JjkText`
- `LoadImage`
- `GetImageSizeAndCount`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`SimpleMath+`、`CreateCFGScheduleFloatList`、`WanVideoSetBlockSwap`、`INTConstant`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoSetLoRAs`、`JWInteger`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`easy int`、`WanVideoImageToVideoEncode`、`DF_Integer`、`LoadImage`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
