---
key: 视频生成/文生视频/（KJ版2+2极速）Wan2.2自动镜头新版lightning0928文生视频V3_1972282645650534402.json
name: （KJ版2+2极速）Wan2.2自动镜头新版lightning0928文生视频V3_1972282645650534402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（KJ版2+2极速）Wan2.2自动镜头新版lightning0928文生视频V3_1972282645650534402.json
hash: b7ec87703c3b8717
coverage: 0.72
learned_at: 2026-10-10 23:14:26
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTextEncode, Note, CR Prompt Text, easy showAnything, easy showAnything, ShowText|pysssss, JWStringConcat, easy showAnything, JWInteger, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoVAELoader, VHS_VideoCombine, CR Prompt Text, Note, WanVideoDecode, Wan22PromptSelector, CR Prompt Text, RH_LLMAPI_NODE, PrimitiveNode, WanVideoModelLoader, WanVideoModelLoader, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelect, WanVideoSampler, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoLoraSelect, INTConstant, INTConstant, TextConcat, GetImageSizeAndCount, ImageFromBatch+]
patterns: []
missing: [ImageFromBatch+, CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（KJ版2+2极速）Wan2.2自动镜头新版lightning0928文生视频V3_1972282645650534402.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（KJ版2+2极速）Wan2.2自动镜头新版lightning0928文生视频V3_1972282645650534402.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（50 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `Note`
- `CR Prompt Text`
- `easy showAnything`
- `easy showAnything`
- `ShowText|pysssss`
- `JWStringConcat`
- `easy showAnything`
- `JWInteger`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `Note`
- `WanVideoDecode`
- `Wan22PromptSelector`
- `CR Prompt Text`
- `RH_LLMAPI_NODE`
- `PrimitiveNode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `INTConstant`
- `INTConstant`
- `TextConcat`
- `GetImageSizeAndCount`
- `ImageFromBatch+`

## 知识

覆盖率 **72%**（36/50）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`JWStringConcat`、`JWInteger`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoDecode`、`Wan22PromptSelector`、`RH_LLMAPI_NODE`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`INTConstant`、`TextConcat`、`GetImageSizeAndCount`

**缺卡**（4）：`ImageFromBatch+`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
