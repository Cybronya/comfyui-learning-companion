---
key: 视频生成/文生视频/Wan2.2 文生视频高动态质量--(Palingenesis版)_1972223829290446850.json
name: Wan2.2 文生视频高动态质量--(Palingenesis版)_1972223829290446850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频高动态质量--(Palingenesis版)_1972223829290446850.json
hash: 9338aa7ab7bfc65a
coverage: 0.714286
learned_at: 2026-10-15 22:47:11
nodes: [WanVideoDecode, GetImageSizeAndCount, RIFE VFI, ImageListToImageBatch, ImageFromBatch, SaveImage, WanVideoTorchCompileSettings, WanVideoBlockSwap, VHS_VideoCombine, Fast Groups Bypasser (rgthree), Note, Note, Note, SetNode, SetNode, SetNode, SetNode, Int, GetNode, WanVideoLoraSelectMulti, CreateCFGScheduleFloatList, Float, Int, Int, WanVideoEmptyEmbeds, GetNode, GetNode, SimpleMath+, GetNode, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncode, WanVideoVAELoader, VHS_VideoCombine, INTConstant, WanVideoSigmaToStep, WanVideoScheduler, WanVideoScheduler, WanVideoSampler, WanVideoSampler, Text]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 文生视频高动态质量--(Palingenesis版)_1972223829290446850.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频高动态质量--(Palingenesis版)_1972223829290446850.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（42 个）：
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `RIFE VFI`
- `ImageListToImageBatch`
- `ImageFromBatch`
- `SaveImage`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `CreateCFGScheduleFloatList`
- `Float`
- `Int`
- `Int`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `INTConstant`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Text`

## 知识

覆盖率 **71%**（30/42）

**有卡**：`WanVideoDecode`、`GetImageSizeAndCount`、`RIFE VFI`、`ImageListToImageBatch`、`ImageFromBatch`、`SaveImage`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`Int`、`WanVideoLoraSelectMulti`、`CreateCFGScheduleFloatList`、`Float`、`WanVideoEmptyEmbeds`、`SimpleMath+`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoVAELoader`、`INTConstant`、`WanVideoSigmaToStep`、`WanVideoScheduler`、`WanVideoSampler`、`Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelectMulti、GetImageSizeAndCount
