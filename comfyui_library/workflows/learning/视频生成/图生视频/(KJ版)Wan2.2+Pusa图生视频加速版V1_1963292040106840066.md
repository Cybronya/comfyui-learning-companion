---
key: 视频生成/图生视频/(KJ版)Wan2.2+Pusa图生视频加速版V1_1963292040106840066.json
name: (KJ版)Wan2.2+Pusa图生视频加速版V1_1963292040106840066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(KJ版)Wan2.2+Pusa图生视频加速版V1_1963292040106840066.json
hash: a1ff8d7d8cf60f40
coverage: 0.916667
learned_at: 2026-10-15 22:31:32
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoTorchCompileSettings, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, PrimitiveNode, WanVideoVAELoader, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoSampler, Note, JWInteger, INTConstant, INTConstant, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, JWInteger, CR Prompt Text, WanVideoDecode, VHS_VideoCombine, GetImageSizeAndCount, ImageFromBatch+, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版)Wan2.2+Pusa图生视频加速版V1_1963292040106840066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963292040106840066.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `Note`
- `JWInteger`
- `INTConstant`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `JWInteger`
- `CR Prompt Text`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `VHS_VideoCombine`

## 知识

覆盖率 **92%**（33/36）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`JWInteger`、`INTConstant`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`LoadImage`、`CR Prompt Text`、`WanVideoDecode`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`ImageFromBatch+`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
