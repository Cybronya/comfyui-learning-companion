---
key: 视频生成/文生视频/(4步KJ版)Wan2.2+提示词工具+无API视频扩写文生视频加速版V1_1953756767052288002.json
name: (4步KJ版)Wan2.2+提示词工具+无API视频扩写文生视频加速版V1_1953756767052288002.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(4步KJ版)Wan2.2+提示词工具+无API视频扩写文生视频加速版V1_1953756767052288002.json
hash: 3bd29cf54ae123eb
coverage: 0.782609
learned_at: 2026-10-15 22:43:39
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoSampler, JWInteger, JWInteger, JWInteger, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTextEncode, WanVideoVAELoader, Note, CR Prompt Text, Wan22PromptSelector, easy showAnything, RH_LLMAPI_NODE, CR Prompt Text, CR Prompt Text, TextConcat, easy showAnything, ShowText|pysssss, JWStringConcat, easy showAnything, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoEmptyEmbeds, INTConstant, INTConstant, GetImageSizeAndCount, VHS_VideoCombine, CreateCFGScheduleFloatList, FloatToSigmas, StringToFloatList, PrimitiveNode]
patterns: []
missing: []
---

# 视频生成/文生视频/(4步KJ版)Wan2.2+提示词工具+无API视频扩写文生视频加速版V1_1953756767052288002.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1953756767052288002.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `Note`
- `CR Prompt Text`
- `Wan22PromptSelector`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `CR Prompt Text`
- `CR Prompt Text`
- `TextConcat`
- `easy showAnything`
- `ShowText|pysssss`
- `JWStringConcat`
- `easy showAnything`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoEmptyEmbeds`
- `INTConstant`
- `INTConstant`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `CreateCFGScheduleFloatList`
- `FloatToSigmas`
- `StringToFloatList`
- `PrimitiveNode`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`JWInteger`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoVAELoader`、`CR Prompt Text`、`Wan22PromptSelector`、`RH_LLMAPI_NODE`、`TextConcat`、`JWStringConcat`、`WanVideoLoraSelect`、`WanVideoEmptyEmbeds`、`INTConstant`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`FloatToSigmas`、`StringToFloatList`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
