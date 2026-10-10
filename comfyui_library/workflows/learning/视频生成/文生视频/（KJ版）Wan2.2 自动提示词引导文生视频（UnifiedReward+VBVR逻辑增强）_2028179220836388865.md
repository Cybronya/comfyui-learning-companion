---
key: 视频生成/文生视频/（KJ版）Wan2.2 自动提示词引导文生视频（UnifiedReward+VBVR逻辑增强）_2028179220836388865.json
name: （KJ版）Wan2.2 自动提示词引导文生视频（UnifiedReward+VBVR逻辑增强）_2028179220836388865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（KJ版）Wan2.2 自动提示词引导文生视频（UnifiedReward+VBVR逻辑增强）_2028179220836388865.json
hash: 922ce338e573d307
coverage: 0.734694
learned_at: 2026-10-11 03:16:53
nodes: [Note, WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, INTConstant, INTConstant, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, Note, CR Prompt Text, Wan22PromptSelector, TextConcat, easy showAnything, ShowText|pysssss, JWStringConcat, easy showAnything, JWInteger, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, RH_LLMAPI_NODE, WanVideoBlockSwap, JWInteger, JWInteger, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoSampler, WanVideoVAELoader, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoModelLoader, CR Prompt Text, CR Prompt Text, WanVideoLoraSelect, WanVideoTextEncode, PrimitiveNode, easy showAnything, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: [CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（KJ版）Wan2.2 自动提示词引导文生视频（UnifiedReward+VBVR逻辑增强）_2028179220836388865.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（KJ版）Wan2.2 自动提示词引导文生视频（UnifiedReward+VBVR逻辑增强）_2028179220836388865.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（49 个）：
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
- `Note`
- `CR Prompt Text`
- `Wan22PromptSelector`
- `TextConcat`
- `easy showAnything`
- `ShowText|pysssss`
- `JWStringConcat`
- `easy showAnything`
- `JWInteger`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `RH_LLMAPI_NODE`
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
- `CR Prompt Text`
- `CR Prompt Text`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `PrimitiveNode`
- `easy showAnything`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **73%**（36/49）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`Wan22PromptSelector`、`TextConcat`、`JWStringConcat`、`JWInteger`、`WanVideoSetLoRAs`、`RH_LLMAPI_NODE`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoTextEncode`

**缺卡**（3）：`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
