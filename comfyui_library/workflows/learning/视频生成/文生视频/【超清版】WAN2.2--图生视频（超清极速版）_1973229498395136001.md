---
key: 视频生成/文生视频/【超清版】WAN2.2--图生视频（超清极速版）_1973229498395136001.json
name: 【超清版】WAN2.2--图生视频（超清极速版）_1973229498395136001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【超清版】WAN2.2--图生视频（超清极速版）_1973229498395136001.json
hash: 6b2577e45d872f3e
coverage: 0.939394
learned_at: 2026-10-15 22:47:42
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoBlockSwap, LoadImage, easy int, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoImageToVideoEncode, MathExpression|pysssss, INTConstant, GetImageSizeAndCount, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoLoraSelect, DF_Integer, JjkText, WanVideoSampler, WanVideoSampler, WanVideoTextEncode, SimpleMath+, WanVideoLoraSelect, JWInteger, WanVideoDecode, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, CreateCFGScheduleFloatList, WanVideoLoraSelect, VHS_VideoCombine, WanVideoModelLoader, WanVideoModelLoader, PrimitiveNode, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/【超清版】WAN2.2--图生视频（超清极速版）_1973229498395136001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【超清版】WAN2.2--图生视频（超清极速版）_1973229498395136001.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `LoadImage`
- `easy int`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoImageToVideoEncode`
- `MathExpression|pysssss`
- `INTConstant`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `DF_Integer`
- `JjkText`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `SimpleMath+`
- `WanVideoLoraSelect`
- `JWInteger`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `PrimitiveNode`
- `WanVideoLoraSelect`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`LoadImage`、`easy int`、`WanVideoSetBlockSwap`、`WanVideoImageToVideoEncode`、`MathExpression|pysssss`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`DF_Integer`、`WanVideoSampler`、`WanVideoTextEncode`、`SimpleMath+`、`JWInteger`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
