---
key: 视频生成/图生视频/WAN2.2 图生视频-超清极速版_1990675353976922114.json
name: WAN2.2 图生视频-超清极速版_1990675353976922114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1990675353976922114.json
hash: 50416e8745d72b3f
coverage: 0.939394
learned_at: 2026-10-15 22:33:11
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoBlockSwap, easy int, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoImageToVideoEncode, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, SimpleMath+, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, INTConstant, WanVideoDecode, GetImageSizeAndCount, WanVideoSampler, WanVideoSampler, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetLoRAs, PrimitiveNode, JWInteger, JjkText, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetLoRAs, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, DF_Integer]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2 图生视频-超清极速版_1990675353976922114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1990675353976922114.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `easy int`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoImageToVideoEncode`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `SimpleMath+`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `JWInteger`
- `JjkText`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `DF_Integer`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`easy int`、`WanVideoSetBlockSwap`、`WanVideoImageToVideoEncode`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`SimpleMath+`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`JWInteger`、`WanVideoLoraSelect`、`LoadImage`、`VHS_VideoCombine`、`DF_Integer`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
