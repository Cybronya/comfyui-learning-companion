---
key: 视频生成/文生视频/【KJ版】Wan2.2最新轮回模型文生视频-智能扩写-4步加速_1972671166085287937.json
name: 【KJ版】Wan2.2最新轮回模型文生视频-智能扩写-4步加速_1972671166085287937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【KJ版】Wan2.2最新轮回模型文生视频-智能扩写-4步加速_1972671166085287937.json
hash: c49e793c4919319f
coverage: 0.732143
learned_at: 2026-10-10 23:10:03
nodes: [Wan22PromptSelector, JWInteger, JWInteger, WanVideoModelLoader, GetNode, GetNode, JWInteger, WanVideoTextEncode, GetNode, GetNode, WanVideoEmptyEmbeds, MathExpression|pysssss, RH_LLMAPI_NODE, Text Concatenate, ImpactSwitch, WanVideoTorchCompileSettings, SetNode, WanVideoVAELoader, SetNode, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, SetNode, SetNode, WanVideoSigmaToStep, Float, RH_LLMAPI_NODE, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, WanVideoDecode, CreateCFGScheduleFloatList, Fast Groups Bypasser (rgthree), INTConstant, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, easy showAnything, RIFE VFI, WanVideoLoraSelect, CR Text, JWInteger, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoScheduler, WanVideoScheduler]
patterns: []
missing: [CR Text, MathExpression|pysssss, RIFE VFI, Text Concatenate]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/【KJ版】Wan2.2最新轮回模型文生视频-智能扩写-4步加速_1972671166085287937.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【KJ版】Wan2.2最新轮回模型文生视频-智能扩写-4步加速_1972671166085287937.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（56 个）：
- `Wan22PromptSelector`
- `JWInteger`
- `JWInteger`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `JWInteger`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `WanVideoEmptyEmbeds`
- `MathExpression|pysssss`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `ImpactSwitch`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `WanVideoSigmaToStep`
- `Float`
- `RH_LLMAPI_NODE`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy showAnything`
- `RIFE VFI`
- `WanVideoLoraSelect`
- `CR Text`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoScheduler`
- `WanVideoScheduler`

## 知识

覆盖率 **73%**（41/56）

**有卡**：`Wan22PromptSelector`、`JWInteger`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`RH_LLMAPI_NODE`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSigmaToStep`、`Float`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoScheduler`

**缺卡**（4）：`CR Text`、`MathExpression|pysssss`、`RIFE VFI`、`Text Concatenate`

**用到的条目**：SeedVR2BlockSwap、SeedVR2ExtraArgs、SeedVR2GGUF、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
