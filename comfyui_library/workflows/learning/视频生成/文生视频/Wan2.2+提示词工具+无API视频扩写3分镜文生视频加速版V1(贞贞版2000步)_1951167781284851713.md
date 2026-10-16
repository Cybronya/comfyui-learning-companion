---
key: 视频生成/文生视频/Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V1(贞贞版2000步)_1951167781284851713.json
name: Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V1(贞贞版2000步)_1951167781284851713.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1951167781284851713.json
hash: 32ab06868756f3e9
coverage: 0.782609
learned_at: 2026-10-15 22:43:37
nodes: [Note, WanVideoSetBlockSwap, WanVideoDecode, GetImageSizeAndCount, WanVideoBlockSwap, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncode, VHS_VideoCombine, WanVideoVAELoader, Note, CR Prompt Text, Wan22PromptSelector, easy showAnything, CR Prompt Text, CR Prompt Text, TextConcat, easy showAnything, ShowText|pysssss, JWStringConcat, easy showAnything, JWInteger, WanVideoSampler, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoLoraSelect, RH_LLMAPI_NODE, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V1(贞贞版2000步)_1951167781284851713.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1951167781284851713.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `PrimitiveNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
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
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `Note`
- `CR Prompt Text`
- `Wan22PromptSelector`
- `easy showAnything`
- `CR Prompt Text`
- `CR Prompt Text`
- `TextConcat`
- `easy showAnything`
- `ShowText|pysssss`
- `JWStringConcat`
- `easy showAnything`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `RH_LLMAPI_NODE`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`INTConstant`、`JWInteger`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoVAELoader`、`CR Prompt Text`、`Wan22PromptSelector`、`TextConcat`、`JWStringConcat`、`WanVideoSampler`、`WanVideoSetLoRAs`、`RH_LLMAPI_NODE`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
