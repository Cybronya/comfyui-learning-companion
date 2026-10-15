---
key: 视频生成/文生视频/wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873.json
name: wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873.json
hash: 092e209da07413a3
coverage: 0.911111
learned_at: 2026-10-15 22:47:36
nodes: [MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, PrimitiveBoolean, RH_Translator, WanVideoBlockSwap, WanVideoEmptyEmbeds, WanVideoVAELoader, WanVideoDecode, easy ifElse, CR Text, CR Text Concatenate, RH_Prompter, ShowText|pysssss, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, SimpleMath+, MathExpression|pysssss, INTConstant, GetImageSizeAndCount, RIFE VFI, WanVideoSampler, WanVideoTorchCompileSettings, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelect, WanVideoModelLoader, PrimitiveNode, DF_Integer, JWInteger, JWInteger, easy int, Note, Text Multiline, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PrimitiveBoolean`
- `RH_Translator`
- `WanVideoBlockSwap`
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `easy ifElse`
- `CR Text`
- `CR Text Concatenate`
- `RH_Prompter`
- `ShowText|pysssss`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `MathExpression|pysssss`
- `INTConstant`
- `GetImageSizeAndCount`
- `RIFE VFI`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `PrimitiveNode`
- `DF_Integer`
- `JWInteger`
- `JWInteger`
- `easy int`
- `Note`
- `Text Multiline`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **91%**（41/45）

**有卡**：`MathExpression|pysssss`、`PrimitiveBoolean`、`RH_Translator`、`WanVideoBlockSwap`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`WanVideoDecode`、`CR Text`、`CR Text Concatenate`、`RH_Prompter`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`LoadWanVideoT5TextEncoder`、`SimpleMath+`、`INTConstant`、`GetImageSizeAndCount`、`RIFE VFI`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`DF_Integer`、`JWInteger`、`easy int`、`Text Multiline`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
