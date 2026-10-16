---
key: 视频生成/图生视频/WAN2.2最新图生视频_1960986981260038145.json
name: WAN2.2最新图生视频_1960986981260038145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1960986981260038145.json
hash: c335ee23d1961cee
coverage: 0.935484
learned_at: 2026-10-15 22:31:27
nodes: [WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, WanVideoDecode, WanVideoSampler, WanVideoSampler, GetImageSizeAndCount, WanVideoSetLoRAs, LayerUtility: ImageScaleByAspectRatio V2, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, INTConstant, SimpleMath+, WanVideoImageToVideoEncode, MathExpression|pysssss, JWInteger, DF_Integer, easy int, PrimitiveNode, JjkText, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2最新图生视频_1960986981260038145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1960986981260038145.json`

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
- `SimpleMath+`
- `WanVideoImageToVideoEncode`
- `MathExpression|pysssss`
- `JWInteger`
- `DF_Integer`
- `easy int`
- `PrimitiveNode`
- `JjkText`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`WanVideoSampler`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`INTConstant`、`SimpleMath+`、`WanVideoImageToVideoEncode`、`MathExpression|pysssss`、`JWInteger`、`DF_Integer`、`easy int`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
