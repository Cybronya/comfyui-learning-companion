---
key: 视频生成/图生视频/Wan2.2 图生视频工作流_1991827663358849025.json
name: Wan2.2 图生视频工作流_1991827663358849025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1991827663358849025.json
hash: c089a2edb1bd72db
coverage: 0.935484
learned_at: 2026-10-15 22:33:14
nodes: [VHS_VideoCombine, LoadWanVideoT5TextEncoder, PrimitiveNode, WanVideoSampler, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, JWInteger, DF_Integer, easy int, CreateCFGScheduleFloatList, SimpleMath+, MathExpression|pysssss, INTConstant, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoImageToVideoEncode, WanVideoTextEncode, LoadImage, JjkText, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 图生视频工作流_1991827663358849025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1991827663358849025.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `JWInteger`
- `DF_Integer`
- `easy int`
- `CreateCFGScheduleFloatList`
- `SimpleMath+`
- `MathExpression|pysssss`
- `INTConstant`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `LoadImage`
- `JjkText`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`JWInteger`、`DF_Integer`、`easy int`、`CreateCFGScheduleFloatList`、`SimpleMath+`、`MathExpression|pysssss`、`INTConstant`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
