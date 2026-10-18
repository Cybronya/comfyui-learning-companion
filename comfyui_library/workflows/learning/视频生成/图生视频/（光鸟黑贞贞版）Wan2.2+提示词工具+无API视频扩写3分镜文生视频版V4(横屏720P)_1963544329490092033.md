---
key: 视频生成/图生视频/（光鸟黑贞贞版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V4(横屏720P)_1963544329490092033.json
name: （光鸟黑贞贞版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V4(横屏720P)_1963544329490092033.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（光鸟黑贞贞版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V4(横屏720P)_1963544329490092033.json
hash: 2e61f18d73b27da3
coverage: 0.787234
learned_at: 2026-10-15 22:31:33
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, INTConstant, INTConstant, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncode, Note, CR Prompt Text, easy showAnything, TextConcat, easy showAnything, ShowText|pysssss, JWStringConcat, easy showAnything, JWInteger, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoSampler, WanVideoVAELoader, GetImageSizeAndCount, VHS_VideoCombine, WanVideoModelLoader, CR Prompt Text, Note, WanVideoDecode, VHS_VideoCombine, Wan22PromptSelector, RH_LLMAPI_NODE, CR Prompt Text, PrimitiveNode]
patterns: []
missing: []
---

# 视频生成/图生视频/（光鸟黑贞贞版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V4(横屏720P)_1963544329490092033.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963544329490092033.json`

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
- `Note`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `RH_LLMAPI_NODE`
- `CR Prompt Text`
- `PrimitiveNode`

## 知识

覆盖率 **79%**（37/47）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`CR Prompt Text`、`TextConcat`、`JWStringConcat`、`JWInteger`、`WanVideoSetLoRAs`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoDecode`、`Wan22PromptSelector`、`RH_LLMAPI_NODE`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
