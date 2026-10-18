---
key: 视频生成/图生视频/(KJ版)Wan2.2图生视频精准调度加速_1976470630323326977.json
name: (KJ版)Wan2.2图生视频精准调度加速_1976470630323326977.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(KJ版)Wan2.2图生视频精准调度加速_1976470630323326977.json
hash: 9c580221f6118465
coverage: 0.918919
learned_at: 2026-10-15 22:32:11
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, CreateCFGScheduleFloatList, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, PrimitiveNode, WanVideoSampler, INTConstant, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoTextEncode, WanVideoModelLoader, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoLoraSelect, INTConstant, WanVideoScheduler, WanVideoSigmaToStep, WanVideoScheduler, Float, LoadWanVideoT5TextEncoder, JWInteger, WanVideoBlockSwap, WanVideoModelLoader, LoadImage, WanVideoVAELoader, VHS_VideoCombine, CR Prompt Text, JWInteger, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版)Wan2.2图生视频精准调度加速_1976470630323326977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976470630323326977.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `INTConstant`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `Float`
- `LoadWanVideoT5TextEncoder`
- `JWInteger`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `LoadImage`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `JWInteger`
- `Note`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`Float`、`LoadWanVideoT5TextEncoder`、`JWInteger`、`LoadImage`、`WanVideoVAELoader`、`VHS_VideoCombine`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
