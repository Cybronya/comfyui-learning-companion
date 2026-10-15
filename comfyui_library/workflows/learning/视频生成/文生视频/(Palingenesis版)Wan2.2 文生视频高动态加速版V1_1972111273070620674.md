---
key: 视频生成/文生视频/(Palingenesis版)Wan2.2 文生视频高动态加速版V1_1972111273070620674.json
name: (Palingenesis版)Wan2.2 文生视频高动态加速版V1_1972111273070620674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(Palingenesis版)Wan2.2 文生视频高动态加速版V1_1972111273070620674.json
hash: f667ee8347349231
coverage: 0.837838
learned_at: 2026-10-15 22:43:12
nodes: [VHS_VideoCombine, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, LoadWanVideoT5TextEncoder, WanVideoSampler, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoTextEncode, WanVideoLoraSelect, WanVideoBlockSwap, CreateCFGScheduleFloatList, PrimitiveNode, INTConstant, WanVideoSampler, WanVideoScheduler, WanVideoScheduler, WanVideoSigmaToStep, CR Prompt Text, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, Float]
patterns: []
missing: []
---

# 视频生成/文生视频/(Palingenesis版)Wan2.2 文生视频高动态加速版V1_1972111273070620674.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/(Palingenesis版)Wan2.2 文生视频高动态加速版V1_1972111273070620674.json`

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
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `INTConstant`
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
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Float`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`JWInteger`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`CR Prompt Text`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`WanVideoModelLoader`、`Float`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
