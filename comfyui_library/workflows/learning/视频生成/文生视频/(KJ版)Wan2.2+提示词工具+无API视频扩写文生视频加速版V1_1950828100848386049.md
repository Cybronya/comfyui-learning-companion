---
key: 视频生成/文生视频/(KJ版)Wan2.2+提示词工具+无API视频扩写文生视频加速版V1_1950828100848386049.json
name: (KJ版)Wan2.2+提示词工具+无API视频扩写文生视频加速版V1_1950828100848386049.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(KJ版)Wan2.2+提示词工具+无API视频扩写文生视频加速版V1_1950828100848386049.json
hash: bce6e23a8a1481a5
coverage: 0.772727
learned_at: 2026-10-15 22:43:37
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoEmptyEmbeds, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, JWInteger, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, VHS_VideoCombine, WanVideoVAELoader, Note, CR Prompt Text, Wan22PromptSelector, easy showAnything, RH_LLMAPI_NODE, CR Prompt Text, CR Prompt Text, TextConcat, easy showAnything, ShowText|pysssss, JWStringConcat, easy showAnything]
patterns: []
missing: []
---

# 视频生成/文生视频/(KJ版)Wan2.2+提示词工具+无API视频扩写文生视频加速版V1_1950828100848386049.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950828100848386049.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `PrimitiveNode`
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
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
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

## 知识

覆盖率 **77%**（34/44）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`INTConstant`、`JWInteger`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoVAELoader`、`CR Prompt Text`、`Wan22PromptSelector`、`RH_LLMAPI_NODE`、`TextConcat`、`JWStringConcat`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
