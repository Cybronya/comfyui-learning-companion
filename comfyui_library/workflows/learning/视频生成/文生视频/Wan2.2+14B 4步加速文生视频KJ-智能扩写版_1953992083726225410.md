---
key: 视频生成/文生视频/Wan2.2+14B 4步加速文生视频KJ-智能扩写版_1953992083726225410.json
name: Wan2.2+14B 4步加速文生视频KJ-智能扩写版_1953992083726225410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1953992083726225410.json
hash: 85324582e2f34df4
coverage: 0.666667
learned_at: 2026-10-15 22:43:39
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, ImpactSwitch, StringToFloatList, WanVideoSetLoRAs, PrimitiveInt, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, WanVideoEmptyEmbeds, Reroute, FloatToSigmas, PrimitiveInt, WanVideoSampler, WanVideoSampler, MathExpression|pysssss, Reroute, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoBlockSwap, ShowText|pysssss, RH_LLMAPI_NODE, MathExpression|pysssss, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, DF_Int_to_Float, Reroute, PrimitiveStringMultiline, Text Concatenate, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, Wan22PromptSelector]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2+14B 4步加速文生视频KJ-智能扩写版_1953992083726225410.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1953992083726225410.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（39 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `ImpactSwitch`
- `StringToFloatList`
- `WanVideoSetLoRAs`
- `PrimitiveInt`
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoEmptyEmbeds`
- `Reroute`
- `FloatToSigmas`
- `PrimitiveInt`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `MathExpression|pysssss`
- `Reroute`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `DF_Int_to_Float`
- `Reroute`
- `PrimitiveStringMultiline`
- `Text Concatenate`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `Wan22PromptSelector`

## 知识

覆盖率 **67%**（26/39）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`StringToFloatList`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`FloatToSigmas`、`WanVideoSampler`、`MathExpression|pysssss`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`RH_LLMAPI_NODE`、`VHS_VideoCombine`、`DF_Int_to_Float`、`Text Concatenate`、`Wan22PromptSelector`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs、Wan22PromptSelector
