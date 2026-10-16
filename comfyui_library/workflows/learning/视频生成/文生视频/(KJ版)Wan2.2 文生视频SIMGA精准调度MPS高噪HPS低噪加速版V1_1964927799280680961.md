---
key: 视频生成/文生视频/(KJ版)Wan2.2 文生视频SIMGA精准调度MPS高噪HPS低噪加速版V1_1964927799280680961.json
name: (KJ版)Wan2.2 文生视频SIMGA精准调度MPS高噪HPS低噪加速版V1_1964927799280680961.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1964927799280680961.json
hash: 5281bb230c99820d
coverage: 0.837838
learned_at: 2026-10-15 22:43:44
nodes: [VHS_VideoCombine, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, LoadWanVideoT5TextEncoder, WanVideoSampler, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncode, WanVideoLoraSelect, WanVideoBlockSwap, CreateCFGScheduleFloatList, PrimitiveNode, INTConstant, Float, WanVideoSampler, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, CR Prompt Text, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/(KJ版)Wan2.2 文生视频SIMGA精准调度MPS高噪HPS低噪加速版V1_1964927799280680961.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1964927799280680961.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `VHS_VideoCombine`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `INTConstant`
- `Float`
- `WanVideoSampler` ★核心
- `WanVideoScheduler`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`JWInteger`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`Float`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`CR Prompt Text`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
