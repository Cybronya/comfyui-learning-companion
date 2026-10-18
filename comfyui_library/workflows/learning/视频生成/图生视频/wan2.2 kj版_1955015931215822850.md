---
key: 视频生成/图生视频/wan2.2 kj版_1955015931215822850.json
name: wan2.2 kj版_1955015931215822850.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 kj版_1955015931215822850.json
hash: e0fbc099df3951ef
coverage: 0.96875
learned_at: 2026-10-15 22:31:07
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTorchCompileSettings, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, WanVideoLoraSelect, Text Multiline, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoVAELoader, PrimitiveNode, DF_Integer, JWInteger, LoadImage, RH_Translator, WanVideoTextEncode, INTConstant, MathExpression|pysssss, easy int]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 kj版_1955015931215822850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955015931215822850.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `WanVideoLoraSelect`
- `Text Multiline`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `PrimitiveNode`
- `DF_Integer`
- `JWInteger`
- `LoadImage`
- `RH_Translator`
- `WanVideoTextEncode`
- `INTConstant`
- `MathExpression|pysssss`
- `easy int`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`Text Multiline`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`DF_Integer`、`JWInteger`、`LoadImage`、`RH_Translator`、`WanVideoTextEncode`、`INTConstant`、`MathExpression|pysssss`、`easy int`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
