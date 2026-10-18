---
key: 视频生成/图生视频/Comfy挑战赛6（心跳）Wan2.2图生视频+音频_1971183114510864385.json
name: Comfy挑战赛6（心跳）Wan2.2图生视频+音频_1971183114510864385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Comfy挑战赛6（心跳）Wan2.2图生视频+音频_1971183114510864385.json
hash: a721b3301728113f
coverage: 0.886364
learned_at: 2026-10-15 22:31:55
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoSampler, Note, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncode, WanVideoBlockSwap, WanVideoTorchCompileSettings, Float, INTConstant, CreateCFGScheduleFloatList, JWInteger, PrimitiveNode, WanVideoLoraSelect, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoLoraSelect, Note, LoadWanVideoT5TextEncoder, easy showAnything, VAELoader, SaveLatent, VAEEncode, text_mul_replace, HunyuanVideoFoley, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, CR Prompt Text, JWInteger, LoadImage, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/Comfy挑战赛6（心跳）Wan2.2图生视频+音频_1971183114510864385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971183114510864385.json`

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
- `WanVideoSampler` ★核心
- `Note`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `Float`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `JWInteger`
- `PrimitiveNode`
- `WanVideoLoraSelect`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `easy showAnything`
- `VAELoader`
- `SaveLatent`
- `VAEEncode` ★核心
- `text_mul_replace`
- `HunyuanVideoFoley`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `CR Prompt Text`
- `JWInteger`
- `LoadImage`
- `WanVideoDecode`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`Float`、`INTConstant`、`CreateCFGScheduleFloatList`、`JWInteger`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`LoadWanVideoT5TextEncoder`、`VAELoader`、`SaveLatent`、`VAEEncode`、`text_mul_replace`、`HunyuanVideoFoley`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`CR Prompt Text`、`LoadImage`、`WanVideoDecode`

**用到的条目**：VAELoader、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、VAEEncode、LoadWanVideoT5TextEncoder、WanVideoDecode
