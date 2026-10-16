---
key: 视频生成/图生视频/【高质量+加速】(KJ版)Wan2.2 图生视频（加速+质量提高）精准调度版_1982245487325659137.json
name: 【高质量+加速】(KJ版)Wan2.2 图生视频（加速+质量提高）精准调度版_1982245487325659137.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1982245487325659137.json
hash: 1fe1509128c6a9c6
coverage: 0.893617
learned_at: 2026-10-15 22:32:40
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoTextEncode, WanVideoBlockSwap, WanVideoTorchCompileSettings, INTConstant, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoLoraSelect, Note, LoadWanVideoT5TextEncoder, VAELoader, SaveLatent, VAEEncode, WanVideoDecode, WanVideoModelLoader, VHS_VideoCombine, VHS_VideoCombine, HunyuanVideoFoley, text_mul_replace, easy showAnything, Note, CR Prompt Text, JWInteger, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, VHS_VideoCombine, Float, WanVideoLoraSelect, WanVideoLoraSelect, JWInteger, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/【高质量+加速】(KJ版)Wan2.2 图生视频（加速+质量提高）精准调度版_1982245487325659137.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982245487325659137.json`

## 结构

**生成流程**：Model → Encode → Sampling → Process → Output → Other

**节点**（47 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `VAELoader`
- `SaveLatent`
- `VAEEncode` ★核心
- `WanVideoDecode`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `HunyuanVideoFoley`
- `text_mul_replace`
- `easy showAnything`
- `Note`
- `CR Prompt Text`
- `JWInteger`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `Float`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JWInteger`
- `LoadImage`

## 知识

覆盖率 **89%**（42/47）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`VAELoader`、`SaveLatent`、`VAEEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`HunyuanVideoFoley`、`text_mul_replace`、`CR Prompt Text`、`JWInteger`、`GetImageSizeAndCount`、`Float`、`LoadImage`

**用到的条目**：VAELoader、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、VAEEncode、LoadWanVideoT5TextEncoder、WanVideoDecode
