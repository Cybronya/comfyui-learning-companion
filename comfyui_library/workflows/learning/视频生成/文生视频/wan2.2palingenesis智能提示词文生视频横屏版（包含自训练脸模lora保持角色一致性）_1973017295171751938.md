---
key: 视频生成/文生视频/wan2.2palingenesis智能提示词文生视频横屏版（包含自训练脸模lora保持角色一致性）_1973017295171751938.json
name: wan2.2palingenesis智能提示词文生视频横屏版（包含自训练脸模lora保持角色一致性）_1973017295171751938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2palingenesis智能提示词文生视频横屏版（包含自训练脸模lora保持角色一致性）_1973017295171751938.json
hash: f1047ebf20a4f344
coverage: 0.733333
learned_at: 2026-10-10 23:09:44
nodes: [CR Prompt Text, CR Prompt Text, JWStringConcat, easy showAnything, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, easy showAnything, Note, Note, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSetLoRAs, INTConstant, INTConstant, WanVideoVAELoader, WanVideoDecode, GetImageSizeAndCount, JWInteger, VHS_VideoCombine, PrimitiveNode, ShowText|pysssss, WanVideoSampler, easy showAnything, WanVideoLoraSelect, WanVideoSampler, JWInteger, JWInteger, Note, WanVideoModelLoader, Wan22PromptSelector, Note, TextConcat, RH_LLMAPI_NODE, WanVideoEmptyEmbeds, WanVideoSetBlockSwap, CR Prompt Text, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoTextEncode]
patterns: []
missing: [CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
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

覆盖率 **73%**（33/45）

**有卡**：`JWStringConcat`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`INTConstant`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`JWInteger`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoModelLoader`、`Wan22PromptSelector`、`TextConcat`、`RH_LLMAPI_NODE`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`

**缺卡**（3）：`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
