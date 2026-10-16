---
key: 视频生成/文生视频/Wan2.2 14B 文生视频1080P版_1950444010021240833.json
name: Wan2.2 14B 文生视频1080P版_1950444010021240833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950444010021240833.json
hash: c8bfbe203a0d3830
coverage: 0.851852
learned_at: 2026-10-15 22:43:35
nodes: [WanVideoSampler, easy showAnything, easy showAnything, UpscaleModelLoader, ImageUpscaleWithModel, RIFE VFI, ImageScale, SimpleMath+, SimpleMath+, PlaySound|pysssss, PlaySound|pysssss, WanVideoVAELoader, WanVideoDecode, WanVideoSetBlockSwap, WanVideoEmptyEmbeds, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, PrimitiveNode, easy cleanGpuUsed, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoEnhanceAVideo, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoSLG, WanVideoSampler, easy showAnything, INTConstant, INTConstant, JjkText, JWInteger, easy showAnything, easy anythingIndexSwitch, MathExpression|pysssss, CR Text Concatenate, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoBlockSwap, JjkText, VHS_VideoCombine, VHS_VideoCombine, RH_Prompter, easy showAnything, RH_Prompter, CR Text, JWInteger, JWInteger, JWInteger]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 14B 文生视频1080P版_1950444010021240833.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950444010021240833.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（54 个）：
- `WanVideoSampler` ★核心
- `easy showAnything`
- `easy showAnything`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `RIFE VFI`
- `ImageScale`
- `SimpleMath+`
- `SimpleMath+`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoEmptyEmbeds`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoEnhanceAVideo`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `easy showAnything`
- `INTConstant`
- `INTConstant`
- `JjkText`
- `JWInteger`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `MathExpression|pysssss`
- `CR Text Concatenate`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `JjkText`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RH_Prompter`
- `easy showAnything`
- `RH_Prompter`
- `CR Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **85%**（46/54）

**有卡**：`WanVideoSampler`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`RIFE VFI`、`ImageScale`、`SimpleMath+`、`PlaySound|pysssss`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoEmptyEmbeds`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`easy cleanGpuUsed`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`INTConstant`、`JWInteger`、`easy anythingIndexSwitch`、`MathExpression|pysssss`、`CR Text Concatenate`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`RH_Prompter`、`CR Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
