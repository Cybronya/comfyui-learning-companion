---
key: 视频生成/图生视频/图生视频加速版Wan2.2 (Palingenesis版)_1972165369475559425.json
name: 图生视频加速版Wan2.2 (Palingenesis版)_1972165369475559425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1972165369475559425.json
hash: 6d75f681e3e54f6d
coverage: 0.878049
learned_at: 2026-10-15 22:31:58
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoImageToVideoEncode, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoModelLoader, WanVideoScheduler, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, WanVideoSigmaToStep, Float, WanVideoScheduler, MathExpression|pysssss, JWInteger, JWInteger, JWInteger, CR Prompt Text, LoadImage, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoTextEncode, PrimitiveNode, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoSampler, Note, GridAnnotation, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频加速版Wan2.2 (Palingenesis版)_1972165369475559425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972165369475559425.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoScheduler`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `WanVideoSigmaToStep`
- `Float`
- `WanVideoScheduler`
- `MathExpression|pysssss`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `LoadImage`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `Note`
- `GridAnnotation`
- `Note`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoModelLoader`、`WanVideoScheduler`、`WanVideoLoraSelect`、`INTConstant`、`WanVideoSigmaToStep`、`Float`、`MathExpression|pysssss`、`JWInteger`、`CR Prompt Text`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoVAELoader`、`GridAnnotation`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
