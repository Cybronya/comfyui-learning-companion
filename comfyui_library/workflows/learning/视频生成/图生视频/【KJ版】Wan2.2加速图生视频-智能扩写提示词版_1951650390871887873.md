---
key: 视频生成/图生视频/【KJ版】Wan2.2加速图生视频-智能扩写提示词版_1951650390871887873.json
name: 【KJ版】Wan2.2加速图生视频-智能扩写提示词版_1951650390871887873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1951650390871887873.json
hash: 8f622c26dce7cb5e
coverage: 0.714286
learned_at: 2026-10-15 22:30:58
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTorchCompileSettings, SetNode, SetNode, WanVideoBlockSwap, WanVideoVAELoader, SetNode, LoadWanVideoT5TextEncoder, SetNode, GetNode, Primitive integer [Crystools], JWInteger, JWInteger, GetNode, MathExpression|pysssss, GetNode, WanVideoSampler, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, GetNode, WanVideoTextEncode, WanVideoSampler, WanVideoDecode, ImpactSwitch, LoadImage, Note, ShowText|pysssss, RH_LLMAPI_NODE, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, WanVideoImageToVideoEncode, CreateCFGScheduleFloatList, VHS_VideoCombine, Text Concatenate, Wan22PromptSelector, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/【KJ版】Wan2.2加速图生视频-智能扩写提示词版_1951650390871887873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951650390871887873.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `GetNode`
- `Primitive integer [Crystools]`
- `JWInteger`
- `JWInteger`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImpactSwitch`
- `LoadImage`
- `Note`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `WanVideoImageToVideoEncode`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `Text Concatenate`
- `Wan22PromptSelector`
- `CR Text`

## 知识

覆盖率 **71%**（30/42）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`Primitive integer [Crystools]`、`JWInteger`、`MathExpression|pysssss`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoDecode`、`LoadImage`、`RH_LLMAPI_NODE`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoEncode`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`Text Concatenate`、`Wan22PromptSelector`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
