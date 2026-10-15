---
key: 视频生成/文生视频/wan2.2palingenesis智能提示词文生视频横屏版（包含自训练脸模lora保持角色一致性）_1973017295171751938.json
name: wan2.2palingenesis智能提示词文生视频横屏版（包含自训练脸模lora保持角色一致性）_1973017295171751938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2palingenesis智能提示词文生视频横屏版（包含自训练脸模lora保持角色一致性）_1973017295171751938.json
hash: f1047ebf20a4f344
coverage: 0.8
learned_at: 2026-10-15 22:47:35
nodes: [CR Prompt Text, CR Prompt Text, JWStringConcat, easy showAnything, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, easy showAnything, Note, Note, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSetLoRAs, INTConstant, INTConstant, WanVideoVAELoader, WanVideoDecode, GetImageSizeAndCount, JWInteger, VHS_VideoCombine, PrimitiveNode, ShowText|pysssss, WanVideoSampler, easy showAnything, WanVideoLoraSelect, WanVideoSampler, JWInteger, JWInteger, Note, WanVideoModelLoader, Wan22PromptSelector, Note, TextConcat, RH_LLMAPI_NODE, WanVideoEmptyEmbeds, WanVideoSetBlockSwap, CR Prompt Text, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2palingenesis智能提示词文生视频横屏版（包含自训练脸模lora保持角色一致性）_1973017295171751938.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2palingenesis智能提示词文生视频横屏版（包含自训练脸模lora保持角色一致性）_1973017295171751938.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `CR Prompt Text`
- `CR Prompt Text`
- `JWStringConcat`
- `easy showAnything`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `easy showAnything`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `INTConstant`
- `INTConstant`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `JWInteger`
- `VHS_VideoCombine`
- `PrimitiveNode`
- `ShowText|pysssss`
- `WanVideoSampler` ★核心
- `easy showAnything`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `JWInteger`
- `JWInteger`
- `Note`
- `WanVideoModelLoader`
- `Wan22PromptSelector`
- `Note`
- `TextConcat`
- `RH_LLMAPI_NODE`
- `WanVideoEmptyEmbeds`
- `WanVideoSetBlockSwap`
- `CR Prompt Text`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `WanVideoModelLoader`
- `WanVideoTextEncode`

## 知识

覆盖率 **80%**（36/45）

**有卡**：`CR Prompt Text`、`JWStringConcat`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`INTConstant`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`JWInteger`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoModelLoader`、`Wan22PromptSelector`、`TextConcat`、`RH_LLMAPI_NODE`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
