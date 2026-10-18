---
key: 视频生成/图生视频/(insight+ani全能视频Sv3新版)wan2.2高动态卡通动漫图生视频加速版v1_1972564669351260162.json
name: (insight+ani全能视频Sv3新版)wan2.2高动态卡通动漫图生视频加速版v1_1972564669351260162.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(insight+ani全能视频Sv3新版)wan2.2高动态卡通动漫图生视频加速版v1_1972564669351260162.json
hash: 3ddbbc91ba7e05b7
coverage: 0.878788
learned_at: 2026-10-15 22:31:59
nodes: [Note, WanVideoDecode, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoSampler, Note, WanVideoTextEncode, WanVideoTorchCompileSettings, INTConstant, CreateCFGScheduleFloatList, WanVideoSigmaToStep, JWInteger, Float, WanVideoScheduler, WanVideoScheduler, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, CR Prompt Text, JWInteger, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, PrimitiveNode, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/(insight+ani全能视频Sv3新版)wan2.2高动态卡通动漫图生视频加速版v1_1972564669351260162.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972564669351260162.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `Note`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `Note`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSigmaToStep`
- `JWInteger`
- `Float`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `CR Prompt Text`
- `JWInteger`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `Note`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`WanVideoDecode`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSigmaToStep`、`JWInteger`、`Float`、`WanVideoScheduler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadImage`、`CR Prompt Text`、`VHS_VideoCombine`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
