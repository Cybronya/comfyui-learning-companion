---
key: 视频生成/文生视频/（自用）Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V1_1952587209671159809.json
name: （自用）Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V1_1952587209671159809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V1_1952587209671159809.json
hash: 44685c9d8b916163
coverage: 0.734694
learned_at: 2026-10-10 23:14:45
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, PrimitiveNode, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, JWInteger, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTextEncode, Note, CR Prompt Text, Wan22PromptSelector, easy showAnything, CR Prompt Text, CR Prompt Text, TextConcat, ShowText|pysssss, JWStringConcat, easy showAnything, JWInteger, RH_LLMAPI_NODE, WanVideoSampler, WanVideoVAELoader, LoadLatent, VHS_VideoCombine, WanVideoDecode, SaveLatent, WanVideoSampler, easy showAnything, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, SaveImage, LoadImage]
patterns: []
missing: [CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/（自用）Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V1_1952587209671159809.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V1_1952587209671159809.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（49 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
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
- `WanVideoTextEncode`
- `Note`
- `CR Prompt Text`
- `Wan22PromptSelector`
- `easy showAnything`
- `CR Prompt Text`
- `CR Prompt Text`
- `TextConcat`
- `ShowText|pysssss`
- `JWStringConcat`
- `easy showAnything`
- `JWInteger`
- `RH_LLMAPI_NODE`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `LoadLatent`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `SaveLatent`
- `WanVideoSampler` ★核心
- `easy showAnything`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **73%**（36/49）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`INTConstant`、`JWInteger`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoTextEncode`、`Wan22PromptSelector`、`TextConcat`、`JWStringConcat`、`RH_LLMAPI_NODE`、`WanVideoSampler`、`WanVideoVAELoader`、`LoadLatent`、`VHS_VideoCombine`、`WanVideoDecode`、`SaveLatent`、`WanVideoLoraSelect`、`SaveImage`、`LoadImage`

**缺卡**（3）：`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
