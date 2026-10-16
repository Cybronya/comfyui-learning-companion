---
key: 视频生成/图生视频/（4+4）KJ版Wan2.2优调版图生视频实验版V2（LightX2v+Rcm）_1980273017576185857.json
name: （4+4）KJ版Wan2.2优调版图生视频实验版V2（LightX2v+Rcm）_1980273017576185857.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980273017576185857.json
hash: 4706c2bf96df9a97
coverage: 0.895833
learned_at: 2026-10-15 22:32:30
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoTextEncode, WanVideoBlockSwap, WanVideoTorchCompileSettings, Float, INTConstant, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, Note, LoadWanVideoT5TextEncoder, VAELoader, SaveLatent, VAEEncode, WanVideoDecode, WanVideoModelLoader, VHS_VideoCombine, VHS_VideoCombine, HunyuanVideoFoley, text_mul_replace, easy showAnything, Note, CR Prompt Text, JWInteger, LoadImage, JWInteger, WanVideoSampler, GetImageSizeAndCount, WanVideoLoraSelect, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/（4+4）KJ版Wan2.2优调版图生视频实验版V2（LightX2v+Rcm）_1980273017576185857.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980273017576185857.json`

## 结构

**生成流程**：Model → Encode → Sampling → Process → Output → Other

**节点**（48 个）：
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
- `Float`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
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
- `LoadImage`
- `JWInteger`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **90%**（43/48）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`Float`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`LoadWanVideoT5TextEncoder`、`VAELoader`、`SaveLatent`、`VAEEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`HunyuanVideoFoley`、`text_mul_replace`、`CR Prompt Text`、`JWInteger`、`LoadImage`、`GetImageSizeAndCount`、`WanVideoLoraSelect`

**用到的条目**：VAELoader、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、VAEEncode、LoadWanVideoT5TextEncoder、WanVideoDecode
