---
key: 视频生成/文生视频/Wan2.2 自动手动文生视频（UnifiedReward+VBVR逻辑增强）-二次元赛琳娜版_2029097055917969409.json
name: Wan2.2 自动手动文生视频（UnifiedReward+VBVR逻辑增强）-二次元赛琳娜版_2029097055917969409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 自动手动文生视频（UnifiedReward+VBVR逻辑增强）-二次元赛琳娜版_2029097055917969409.json
hash: 56de11cdff8d3863
coverage: 0.655172
learned_at: 2026-10-11 03:16:49
nodes: [WanVideoModelLoader, Wan22PromptSelector, WanVideoLoraSelect, WanVideoLoraSelect, easy showAnything, SimpleMath+, Note, WanVideoLoraSelect, WanVideoLoraSelect, RH_LLMAPI_NODE, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, JWFloat, Note, Note, Int, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, WanVideoDecode, WanVideoEmptyEmbeds, Bjornulf_ShowInt, TTResolutionSelector, GetImageSizeAndCount, Reroute, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoBlockSwap, CR Text, Note, CR Prompt Text, CR Prompt Text, CR Prompt Text, easy showAnything, TextConcat, JWStringConcat, ShowText|pysssss, easy showAnything, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoLoraSelect, Reroute, WanVideoTextEncode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, CR Text, CR Text, MarkdownNote, MarkdownNote, WanVideoModelLoader]
patterns: []
missing: [CR Text, CR Text, CR Text, SimpleMath+, CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 自动手动文生视频（UnifiedReward+VBVR逻辑增强）-二次元赛琳娜版_2029097055917969409.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 自动手动文生视频（UnifiedReward+VBVR逻辑增强）-二次元赛琳娜版_2029097055917969409.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（58 个）：
- `WanVideoModelLoader`
- `Wan22PromptSelector`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `easy showAnything`
- `SimpleMath+`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `RH_LLMAPI_NODE`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `JWFloat`
- `Note`
- `Note`
- `Int`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `Bjornulf_ShowInt`
- `TTResolutionSelector`
- `GetImageSizeAndCount`
- `Reroute`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `CR Text`
- `Note`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy showAnything`
- `TextConcat`
- `JWStringConcat`
- `ShowText|pysssss`
- `easy showAnything`
- `PrimitiveNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Reroute`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Text`
- `CR Text`
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoModelLoader`

## 知识

覆盖率 **66%**（38/58）

**有卡**：`WanVideoModelLoader`、`Wan22PromptSelector`、`WanVideoLoraSelect`、`RH_LLMAPI_NODE`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`JWFloat`、`Int`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoEmptyEmbeds`、`Bjornulf_ShowInt`、`TTResolutionSelector`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`TextConcat`、`JWStringConcat`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`VHS_VideoCombine`

**缺卡**（7）：`CR Text`、`CR Text`、`CR Text`、`SimpleMath+`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
