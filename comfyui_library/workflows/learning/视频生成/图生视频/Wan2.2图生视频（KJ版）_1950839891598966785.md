---
key: 视频生成/图生视频/Wan2.2图生视频（KJ版）_1950839891598966785.json
name: Wan2.2图生视频（KJ版）_1950839891598966785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950839891598966785.json
hash: 2660dc45bab959bf
coverage: 0.88
learned_at: 2026-10-15 22:30:56
nodes: [WanVideoVAELoader, Note, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VHS_VideoCombine, PrimitiveNode, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoModelLoader, LoadImage, WanVideoLoraSelect, Note, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoTextEncode, WanVideoSampler, WanVideoDecode, INTConstant, CreateCFGScheduleFloatList, INTConstant, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoImageToVideoEncode, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频（KJ版）_1950839891598966785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950839891598966785.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoVAELoader`
- `Note`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `VHS_VideoCombine`
- `PrimitiveNode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `LoadImage`
- `WanVideoLoraSelect`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `CR Prompt Text`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`WanVideoVAELoader`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoDecode`、`INTConstant`、`CreateCFGScheduleFloatList`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
