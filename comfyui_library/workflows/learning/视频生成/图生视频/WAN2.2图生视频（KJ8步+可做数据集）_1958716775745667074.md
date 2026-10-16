---
key: 视频生成/图生视频/WAN2.2图生视频（KJ8步+可做数据集）_1958716775745667074.json
name: WAN2.2图生视频（KJ8步+可做数据集）_1958716775745667074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958716775745667074.json
hash: df544d62de788b01
coverage: 0.914286
learned_at: 2026-10-15 22:31:22
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, WanVideoSampler, LayerUtility: PurgeVRAM, WanVideoTorchCompileSettings, WanVideoTextEncode, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, CreateCFGScheduleFloatList, GetImageSizeAndCount, WanVideoDecode, ImageFromBatch+, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, PreviewImage, LoadImage, Note, LoadImage, CR Prompt Text, MathExpression|pysssss, WanVideoImageToVideoEncode, JWInteger, MathExpression|pysssss, WanVideoSampler, PrimitiveInt, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2图生视频（KJ8步+可做数据集）_1958716775745667074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958716775745667074.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `PreviewImage`
- `LoadImage`
- `Note`
- `LoadImage`
- `CR Prompt Text`
- `MathExpression|pysssss`
- `WanVideoImageToVideoEncode`
- `JWInteger`
- `MathExpression|pysssss`
- `WanVideoSampler` ★核心
- `PrimitiveInt`
- `INTConstant`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`CreateCFGScheduleFloatList`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageFromBatch+`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadImage`、`CR Prompt Text`、`MathExpression|pysssss`、`WanVideoImageToVideoEncode`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
