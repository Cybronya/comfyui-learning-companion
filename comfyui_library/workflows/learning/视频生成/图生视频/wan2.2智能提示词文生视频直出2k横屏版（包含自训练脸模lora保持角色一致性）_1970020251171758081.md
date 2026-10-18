---
key: 视频生成/图生视频/wan2.2智能提示词文生视频直出2k横屏版（包含自训练脸模lora保持角色一致性）_1970020251171758081.json
name: wan2.2智能提示词文生视频直出2k横屏版（包含自训练脸模lora保持角色一致性）_1970020251171758081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2智能提示词文生视频直出2k横屏版（包含自训练脸模lora保持角色一致性）_1970020251171758081.json
hash: c49966c300dba18a
coverage: 0.808511
learned_at: 2026-10-15 22:31:51
nodes: [CR Prompt Text, CR Prompt Text, Note, TextConcat, RH_LLMAPI_NODE, JWStringConcat, easy showAnything, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, easy showAnything, Note, Note, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, INTConstant, INTConstant, WanVideoVAELoader, WanVideoDecode, GetImageSizeAndCount, WanVideoEmptyEmbeds, JWInteger, VHS_VideoCombine, PrimitiveNode, ShowText|pysssss, WanVideoSampler, Wan22PromptSelector, WanVideoLoraSelect, easy showAnything, WanVideoLoraSelect, WanVideoLoraSelect, CreateCFGScheduleFloatList, WanVideoSampler, JWInteger, WanVideoLoraSelect, JWInteger, Note, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2智能提示词文生视频直出2k横屏版（包含自训练脸模lora保持角色一致性）_1970020251171758081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1970020251171758081.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `CR Prompt Text`
- `CR Prompt Text`
- `Note`
- `TextConcat`
- `RH_LLMAPI_NODE`
- `JWStringConcat`
- `easy showAnything`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `easy showAnything`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `INTConstant`
- `INTConstant`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoEmptyEmbeds`
- `JWInteger`
- `VHS_VideoCombine`
- `PrimitiveNode`
- `ShowText|pysssss`
- `WanVideoSampler` ★核心
- `Wan22PromptSelector`
- `WanVideoLoraSelect`
- `easy showAnything`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `JWInteger`
- `WanVideoLoraSelect`
- `JWInteger`
- `Note`
- `CR Prompt Text`

## 知识

覆盖率 **81%**（38/47）

**有卡**：`CR Prompt Text`、`TextConcat`、`RH_LLMAPI_NODE`、`JWStringConcat`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`INTConstant`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoEmptyEmbeds`、`JWInteger`、`VHS_VideoCombine`、`WanVideoSampler`、`Wan22PromptSelector`、`CreateCFGScheduleFloatList`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
