---
key: 视频生成/文生视频/（时间音符贞贞版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V4(横屏720P)_1961307588656828418.json
name: （时间音符贞贞版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V4(横屏720P)_1961307588656828418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1961307588656828418.json
hash: 037e7f184e07547d
coverage: 0.787234
learned_at: 2026-10-15 22:43:43
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, INTConstant, INTConstant, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncode, Note, CR Prompt Text, Wan22PromptSelector, easy showAnything, TextConcat, easy showAnything, ShowText|pysssss, JWStringConcat, easy showAnything, JWInteger, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoLoraSelect, RH_LLMAPI_NODE, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoSampler, WanVideoVAELoader, GetImageSizeAndCount, VHS_VideoCombine, WanVideoModelLoader, CR Prompt Text, PrimitiveNode, Note, CR Prompt Text, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/（时间音符贞贞版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V4(横屏720P)_1961307588656828418.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1961307588656828418.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `Note`
- `CR Prompt Text`
- `Wan22PromptSelector`
- `easy showAnything`
- `TextConcat`
- `easy showAnything`
- `ShowText|pysssss`
- `JWStringConcat`
- `easy showAnything`
- `JWInteger`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `RH_LLMAPI_NODE`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `CR Prompt Text`
- `PrimitiveNode`
- `Note`
- `CR Prompt Text`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **79%**（37/47）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`CR Prompt Text`、`Wan22PromptSelector`、`TextConcat`、`JWStringConcat`、`JWInteger`、`WanVideoSetLoRAs`、`RH_LLMAPI_NODE`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoDecode`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
