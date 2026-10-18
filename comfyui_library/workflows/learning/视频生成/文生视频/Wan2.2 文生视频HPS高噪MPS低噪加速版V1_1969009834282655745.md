---
key: 视频生成/文生视频/Wan2.2 文生视频HPS高噪MPS低噪加速版V1_1969009834282655745.json
name: Wan2.2 文生视频HPS高噪MPS低噪加速版V1_1969009834282655745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频HPS高噪MPS低噪加速版V1_1969009834282655745.json
hash: d5ffa2effa6c2711
coverage: 0.837838
learned_at: 2026-10-15 22:43:46
nodes: [Note, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncode, WanVideoLoraSelect, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, WanVideoScheduler, WanVideoScheduler, Float, WanVideoEmptyEmbeds, JWInteger, Note, Note, Note, JWInteger, JWInteger, WanVideoSigmaToStep, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, PrimitiveNode, INTConstant, LoadWanVideoT5TextEncoder, Note, CR Prompt Text, WanVideoBlockSwap, WanVideoTorchCompileSettings]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 文生视频HPS高噪MPS低噪加速版V1_1969009834282655745.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1969009834282655745.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `Note`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoScheduler`
- `Float`
- `WanVideoEmptyEmbeds`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `WanVideoSigmaToStep`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `PrimitiveNode`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `CR Prompt Text`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoScheduler`、`Float`、`WanVideoEmptyEmbeds`、`JWInteger`、`WanVideoSigmaToStep`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`INTConstant`、`LoadWanVideoT5TextEncoder`、`CR Prompt Text`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
