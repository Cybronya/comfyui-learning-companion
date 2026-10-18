---
key: 视频生成/图生视频/【4倍提速】Wan2.2 4步加速图生视频-智能扩写版v2_1954097767838838785.json
name: 【4倍提速】Wan2.2 4步加速图生视频-智能扩写版v2_1954097767838838785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【4倍提速】Wan2.2 4步加速图生视频-智能扩写版v2_1954097767838838785.json
hash: 878de9aa1f5a875b
coverage: 0.688889
learned_at: 2026-10-15 22:31:06
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTorchCompileSettings, SetNode, SetNode, WanVideoBlockSwap, WanVideoVAELoader, SetNode, LoadWanVideoT5TextEncoder, SetNode, GetNode, JWInteger, GetNode, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetBlockSwap, GetNode, Note, ShowText|pysssss, RH_LLMAPI_NODE, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, WanVideoImageToVideoEncode, Note, MathExpression|pysssss, ImpactSwitch, Note, JWInteger, WanVideoSampler, WanVideoSampler, GetNode, FloatToSigmas, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelect, MathExpression|pysssss, Primitive integer [Crystools], StringToFloatList, easy showAnything, Text Concatenate, Wan22PromptSelector, LoadImage, CR Text, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/【4倍提速】Wan2.2 4步加速图生视频-智能扩写版v2_1954097767838838785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954097767838838785.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
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
- `JWInteger`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `GetNode`
- `Note`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `Note`
- `MathExpression|pysssss`
- `ImpactSwitch`
- `Note`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `GetNode`
- `FloatToSigmas`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `StringToFloatList`
- `easy showAnything`
- `Text Concatenate`
- `Wan22PromptSelector`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`

## 知识

覆盖率 **69%**（31/45）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`JWInteger`、`WanVideoModelLoader`、`RH_LLMAPI_NODE`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`MathExpression|pysssss`、`WanVideoSampler`、`FloatToSigmas`、`WanVideoDecode`、`WanVideoLoraSelect`、`Primitive integer [Crystools]`、`StringToFloatList`、`Text Concatenate`、`Wan22PromptSelector`、`LoadImage`、`CR Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
