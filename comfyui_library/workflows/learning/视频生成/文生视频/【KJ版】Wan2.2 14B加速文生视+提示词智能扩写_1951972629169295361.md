---
key: 视频生成/文生视频/【KJ版】Wan2.2 14B加速文生视+提示词智能扩写_1951972629169295361.json
name: 【KJ版】Wan2.2 14B加速文生视+提示词智能扩写_1951972629169295361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1951972629169295361.json
hash: 83f8cd4de456d7e1
coverage: 0.69697
learned_at: 2026-10-15 22:43:38
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect, Reroute, WanVideoSetLoRAs, WanVideoEmptyEmbeds, Reroute, CreateCFGScheduleFloatList, WanVideoVAELoader, WanVideoDecode, VHS_VideoCombine, MathExpression|pysssss, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, Text Concatenate, Wan22PromptSelector, PrimitiveInt, MathExpression|pysssss, ImpactSwitch, WanVideoSetLoRAs, WanVideoSampler, WanVideoSampler, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncode, LoadWanVideoT5TextEncoder, ShowText|pysssss, RH_LLMAPI_NODE, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/文生视频/【KJ版】Wan2.2 14B加速文生视+提示词智能扩写_1951972629169295361.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1951972629169295361.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（33 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `Reroute`
- `WanVideoSetLoRAs`
- `WanVideoEmptyEmbeds`
- `Reroute`
- `CreateCFGScheduleFloatList`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `Text Concatenate`
- `Wan22PromptSelector`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `ImpactSwitch`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **70%**（23/33）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoEmptyEmbeds`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`WanVideoDecode`、`VHS_VideoCombine`、`MathExpression|pysssss`、`Text Concatenate`、`Wan22PromptSelector`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`RH_LLMAPI_NODE`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
