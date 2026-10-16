---
key: 视频生成/图生视频/wan2.2图生视频-标准版-(必收藏)_2059069738726285313.json
name: wan2.2图生视频-标准版-(必收藏)_2059069738726285313.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2059069738726285313.json
hash: 40dc63e7ff1e7f17
coverage: 0.933333
learned_at: 2026-10-15 22:38:36
nodes: [WanVideoSetBlockSwap, easy cleanGpuUsed, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoDecode, easy cleanGpuUsed, easy seed, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoModelLoader, INTConstant, easy cleanGpuUsed, CreateCFGScheduleFloatList, ImageResizeKJv2, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, WanVideoBlockSwap, WanVideoVAELoader, INTConstant, WanVideoLoraSelect, MathExpression|pysssss, PrimitiveFloat, VHS_VideoCombine, LoadImage, WanVideoImageToVideoEncode, WanVideoTextEncode, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频-标准版-(必收藏)_2059069738726285313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059069738726285313.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `easy seed`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `INTConstant`
- `easy cleanGpuUsed`
- `CreateCFGScheduleFloatList`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `INTConstant`
- `WanVideoLoraSelect`
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `PrimitiveFloat`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoDecode`、`easy seed`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoLoraSelect`、`INTConstant`、`CreateCFGScheduleFloatList`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`MathExpression|pysssss`、`VHS_VideoCombine`、`LoadImage`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
