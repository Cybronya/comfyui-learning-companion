---
key: 视频生成/文生视频/(KJ版)Wan2.2 文生视频精准调度加速版V4（加速及质量提高）_1950086334457274370.json
name: (KJ版)Wan2.2 文生视频精准调度加速版V4（加速及质量提高）_1950086334457274370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950086334457274370.json
hash: 97c2d16c9698a1e3
coverage: 0.842105
learned_at: 2026-10-15 22:43:34
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, JWInteger, JWInteger, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, CR Prompt Text, VHS_VideoCombine, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoTextEncode, PrimitiveNode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoSigmaToStep, Float, INTConstant, WanVideoScheduler, WanVideoScheduler]
patterns: []
missing: []
---

# 视频生成/文生视频/(KJ版)Wan2.2 文生视频精准调度加速版V4（加速及质量提高）_1950086334457274370.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950086334457274370.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `PrimitiveNode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoSigmaToStep`
- `Float`
- `INTConstant`
- `WanVideoScheduler`
- `WanVideoScheduler`

## 知识

覆盖率 **84%**（32/38）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`JWInteger`、`WanVideoTorchCompileSettings`、`CR Prompt Text`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoSigmaToStep`、`Float`、`INTConstant`、`WanVideoScheduler`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
