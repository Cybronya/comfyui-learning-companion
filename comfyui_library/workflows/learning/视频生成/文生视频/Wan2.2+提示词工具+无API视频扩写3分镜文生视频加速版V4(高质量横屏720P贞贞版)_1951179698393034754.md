---
key: 视频生成/文生视频/Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V4(高质量横屏720P贞贞版)_1951179698393034754.json
name: Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V4(高质量横屏720P贞贞版)_1951179698393034754.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1951179698393034754.json
hash: d3fcef1c38a9e540
coverage: 0.782609
learned_at: 2026-10-15 22:43:37
nodes: [Note, WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, INTConstant, INTConstant, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncode, Note, CR Prompt Text, Wan22PromptSelector, easy showAnything, CR Prompt Text, CR Prompt Text, TextConcat, easy showAnything, ShowText|pysssss, JWStringConcat, easy showAnything, JWInteger, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoLoraSelect, RH_LLMAPI_NODE, WanVideoLoraSelect, WanVideoLoraSelect, PrimitiveNode, WanVideoBlockSwap, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoSampler, WanVideoVAELoader, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V4(高质量横屏720P贞贞版)_1951179698393034754.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1951179698393034754.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `Note`
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
- `CR Prompt Text`
- `CR Prompt Text`
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
- `PrimitiveNode`
- `WanVideoBlockSwap`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoModelLoader`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`CR Prompt Text`、`Wan22PromptSelector`、`TextConcat`、`JWStringConcat`、`JWInteger`、`WanVideoSetLoRAs`、`RH_LLMAPI_NODE`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
