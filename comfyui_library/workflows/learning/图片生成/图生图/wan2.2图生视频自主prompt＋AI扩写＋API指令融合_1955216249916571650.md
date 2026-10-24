---
key: 图片生成/图生图/wan2.2图生视频自主prompt＋AI扩写＋API指令融合_1955216249916571650.json
name: wan2.2图生视频自主prompt＋AI扩写＋API指令融合_1955216249916571650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2图生视频自主prompt＋AI扩写＋API指令融合_1955216249916571650.json
hash: 700162ecc47980a1
coverage: 0.840909
learned_at: 2026-10-23 11:46:06
nodes: [WanVideoLoraSelect, JWStringConcat, LoadWanVideoT5TextEncoder, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetLoRAs, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoSetBlockSwap, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM, WanVideoSampler, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoDecode, Int, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, WanVideoVAELoader, RH_Captioner, CR Prompt Text, WanVideoTextEncode, easy showAnything, RH_LLMAPI_NODE, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, LoadImage, easy showAnything, TextConcat, ShowText|pysssss, ShowText|pysssss, JjkText, CR Prompt Text, INTConstant, INTConstant]
patterns: []
missing: []
---

# 图片生成/图生图/wan2.2图生视频自主prompt＋AI扩写＋API指令融合_1955216249916571650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2图生视频自主prompt＋AI扩写＋API指令融合_1955216249916571650.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `WanVideoLoraSelect`
- `JWStringConcat`
- `LoadWanVideoT5TextEncoder`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `Int`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `WanVideoVAELoader`
- `RH_Captioner`
- `CR Prompt Text`
- `WanVideoTextEncode`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `LoadImage`
- `easy showAnything`
- `TextConcat`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `JjkText`
- `CR Prompt Text`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **84%**（37/44）

**有卡**：`WanVideoLoraSelect`、`JWStringConcat`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoSetBlockSwap`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`WanVideoDecode`、`Int`、`MathExpression|pysssss`、`WanVideoVAELoader`、`RH_Captioner`、`CR Prompt Text`、`WanVideoTextEncode`、`RH_LLMAPI_NODE`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`LoadImage`、`TextConcat`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
