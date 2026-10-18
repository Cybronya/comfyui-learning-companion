---
key: 视频生成/文生视频/(KJ版)Wan2.2 文生视频加速版V1（情绪）_1950200316404916225.json
name: (KJ版)Wan2.2 文生视频加速版V1（情绪）_1950200316404916225.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(KJ版)Wan2.2 文生视频加速版V1（情绪）_1950200316404916225.json
hash: 410e1040a737485d
coverage: 0.817518
learned_at: 2026-10-15 22:43:35
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, PrimitiveNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoTextEncode, Fast Groups Bypasser (rgthree), CR Prompt Text, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, PrimitiveNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoTextEncode, CR Prompt Text, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, PrimitiveNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoTextEncode, CR Prompt Text, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, PrimitiveNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoTextEncode, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/文生视频/(KJ版)Wan2.2 文生视频加速版V1（情绪）_1950200316404916225.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950200316404916225.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（137 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `CR Prompt Text`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `CR Prompt Text`

## 知识

覆盖率 **82%**（112/137）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`INTConstant`、`JWInteger`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`WanVideoTextEncode`、`CR Prompt Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
