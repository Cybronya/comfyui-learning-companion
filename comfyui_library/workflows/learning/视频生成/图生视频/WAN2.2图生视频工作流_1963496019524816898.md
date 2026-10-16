---
key: 视频生成/图生视频/WAN2.2图生视频工作流_1963496019524816898.json
name: WAN2.2图生视频工作流_1963496019524816898.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1963496019524816898.json
hash: 131e3435983683ac
coverage: 0.935484
learned_at: 2026-10-15 22:31:33
nodes: [WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, WanVideoDecode, WanVideoSampler, WanVideoSampler, GetImageSizeAndCount, WanVideoSetLoRAs, LayerUtility: ImageScaleByAspectRatio V2, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, INTConstant, WanVideoImageToVideoEncode, MathExpression|pysssss, JWInteger, DF_Integer, easy int, PrimitiveNode, LoadImage, JjkText, VHS_VideoCombine, SimpleMath+]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2图生视频工作流_1963496019524816898.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963496019524816898.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `MathExpression|pysssss`
- `JWInteger`
- `DF_Integer`
- `easy int`
- `PrimitiveNode`
- `LoadImage`
- `JjkText`
- `VHS_VideoCombine`
- `SimpleMath+`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`WanVideoSampler`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`INTConstant`、`WanVideoImageToVideoEncode`、`MathExpression|pysssss`、`JWInteger`、`DF_Integer`、`easy int`、`LoadImage`、`VHS_VideoCombine`、`SimpleMath+`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
