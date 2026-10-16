---
key: 视频生成/文生视频/Wan2.2+Skyreels 5分镜提示词扩写文生无限长视频V1_1957481859263426562.json
name: Wan2.2+Skyreels 5分镜提示词扩写文生无限长视频V1_1957481859263426562.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1957481859263426562.json
hash: 6bba3ce30b676c16
coverage: 0.787234
learned_at: 2026-10-15 22:43:41
nodes: [Note, WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, Note, Note, Note, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, Note, Wan22PromptSelector, easy showAnything, CR Prompt Text, CR Prompt Text, TextConcat, JWStringConcat, easy showAnything, WanVideoSetLoRAs, WanVideoLoraSelect, PrimitiveNode, WanVideoBlockSwap, WanVideoEmptyEmbeds, CR Prompt Text, easy showAnything, ShowText|pysssss, INTConstant, INTConstant, JWInteger, JWInteger, JWInteger, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoSetLoRAs, GetImageSizeAndCount, VHS_VideoCombine, WanVideoTextEncode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoBlockSwap, RH_LLMAPI_NODE, WanVideoSampler, WanVideoSampler, WanVideoVAELoader, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2+Skyreels 5分镜提示词扩写文生无限长视频V1_1957481859263426562.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1957481859263426562.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Note`
- `Wan22PromptSelector`
- `easy showAnything`
- `CR Prompt Text`
- `CR Prompt Text`
- `TextConcat`
- `JWStringConcat`
- `easy showAnything`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `WanVideoBlockSwap`
- `WanVideoEmptyEmbeds`
- `CR Prompt Text`
- `easy showAnything`
- `ShowText|pysssss`
- `INTConstant`
- `INTConstant`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `RH_LLMAPI_NODE`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **79%**（37/47）

**有卡**：`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`Wan22PromptSelector`、`CR Prompt Text`、`TextConcat`、`JWStringConcat`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoEmptyEmbeds`、`INTConstant`、`JWInteger`、`CreateCFGScheduleFloatList`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoTextEncode`、`RH_LLMAPI_NODE`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoDecode`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
