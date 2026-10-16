---
key: 视频生成/图生视频/(KJ版)Wan2.2 文生视频加速版V1（运动能力）_1950195066095714306.json
name: (KJ版)Wan2.2 文生视频加速版V1（运动能力）_1950195066095714306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950195066095714306.json
hash: 4fd0a8b6288690a9
coverage: 0.817518
learned_at: 2026-10-15 22:30:54
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, PrimitiveNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoTextEncode, Fast Groups Bypasser (rgthree), CR Prompt Text, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, CR Prompt Text, PrimitiveNode, VHS_VideoCombine, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, PrimitiveNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoTextEncode, CR Prompt Text, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, PrimitiveNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, JWInteger, Note, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoTextEncode, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/(KJ版)Wan2.2 文生视频加速版V1（运动能力）_1950195066095714306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950195066095714306.json`

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
- `WanVideoTextEncode`
- `CR Prompt Text`
- `PrimitiveNode`
- `VHS_VideoCombine`
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
