---
key: 视频生成/图生视频/（4+4-光鸟）KJ版Wan2.2优调版图生视频V1_1976156125466902529.json
name: （4+4-光鸟）KJ版Wan2.2优调版图生视频V1_1976156125466902529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1976156125466902529.json
hash: 7277938c727ce35a
coverage: 0.886364
learned_at: 2026-10-15 22:32:10
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncode, WanVideoBlockSwap, WanVideoTorchCompileSettings, Float, INTConstant, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoLoraSelect, Note, LoadWanVideoT5TextEncoder, VAELoader, SaveLatent, VAEEncode, VHS_VideoCombine, GetImageSizeAndCount, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, HunyuanVideoFoley, text_mul_replace, easy showAnything, WanVideoLoraSelect, Note, CR Prompt Text, JWInteger, LoadImage, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/（4+4-光鸟）KJ版Wan2.2优调版图生视频V1_1976156125466902529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976156125466902529.json`

## 结构

**生成流程**：Model → Encode → Sampling → Process → Output → Other

**节点**（44 个）：
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
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `Float`
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
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `HunyuanVideoFoley`
- `text_mul_replace`
- `easy showAnything`
- `WanVideoLoraSelect`
- `Note`
- `CR Prompt Text`
- `JWInteger`
- `LoadImage`
- `JWInteger`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`Float`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`LoadWanVideoT5TextEncoder`、`VAELoader`、`SaveLatent`、`VAEEncode`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoDecode`、`HunyuanVideoFoley`、`text_mul_replace`、`CR Prompt Text`、`JWInteger`、`LoadImage`

**用到的条目**：VAELoader、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、VAEEncode、LoadWanVideoT5TextEncoder、WanVideoDecode
