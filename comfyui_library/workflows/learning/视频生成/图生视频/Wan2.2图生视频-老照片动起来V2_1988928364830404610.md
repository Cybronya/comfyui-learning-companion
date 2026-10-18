---
key: 视频生成/图生视频/Wan2.2图生视频-老照片动起来V2_1988928364830404610.json
name: Wan2.2图生视频-老照片动起来V2_1988928364830404610.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频-老照片动起来V2_1988928364830404610.json
hash: 6ea33a47871bbdef
coverage: 0.972973
learned_at: 2026-10-15 22:33:05
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTextEncode, PrimitiveNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoVAELoader, WanVideoImageToVideoEncode, INTConstant, WanVideoSigmaToStep, Float, CreateCFGScheduleFloatList, WanVideoScheduler, WanVideoScheduler, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoTorchCompileSettings, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, LoadImage, CR Prompt Text, LoadWanVideoT5TextEncoder, JWInteger, JWInteger, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频-老照片动起来V2_1988928364830404610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988928364830404610.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `PrimitiveNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `WanVideoSigmaToStep`
- `Float`
- `CreateCFGScheduleFloatList`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `LoadImage`
- `CR Prompt Text`
- `LoadWanVideoT5TextEncoder`
- `JWInteger`
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`INTConstant`、`WanVideoSigmaToStep`、`Float`、`CreateCFGScheduleFloatList`、`WanVideoScheduler`、`WanVideoSampler`、`LayerUtility: PurgeVRAM V2`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`WanVideoBlockSwap`、`LoadImage`、`CR Prompt Text`、`LoadWanVideoT5TextEncoder`、`JWInteger`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
