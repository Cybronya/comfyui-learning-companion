---
key: 视频生成/文生视频/wan2.2图生视频V3.0（4步加速lora+kj版本）_1954108847948480514.json
name: wan2.2图生视频V3.0（4步加速lora+kj版本）_1954108847948480514.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2图生视频V3.0（4步加速lora+kj版本）_1954108847948480514.json
hash: 44f21cf941933278
coverage: 0.756757
learned_at: 2026-10-15 22:43:39
nodes: [WanVideoSetLoRAs, WanVideoTorchCompileSettings, SetNode, SetNode, WanVideoBlockSwap, WanVideoVAELoader, SetNode, LoadWanVideoT5TextEncoder, SetNode, GetNode, GetNode, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoDecode, WanVideoTextEncode, FloatToSigmas, Note, JWInteger, WanVideoSampler, WanVideoSampler, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, GetNode, WanVideoImageToVideoEncode, StringToFloatList, LoadImage, CR Text, MathExpression|pysssss, GetNode, MathExpression|pysssss, Primitive integer [Crystools], WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2图生视频V3.0（4步加速lora+kj版本）_1954108847948480514.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1954108847948480514.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `FloatToSigmas`
- `Note`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `StringToFloatList`
- `LoadImage`
- `CR Text`
- `MathExpression|pysssss`
- `GetNode`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`

## 知识

覆盖率 **76%**（28/37）

**有卡**：`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoTextEncode`、`FloatToSigmas`、`JWInteger`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoEncode`、`StringToFloatList`、`LoadImage`、`CR Text`、`MathExpression|pysssss`、`Primitive integer [Crystools]`、`WanVideoLoraSelect`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
