---
key: 视频生成/文生视频/wan2.2 图生视频 -  超级加速晋级版_1967469611824373761.json
name: wan2.2 图生视频 -  超级加速晋级版_1967469611824373761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1967469611824373761.json
hash: 2c518fed3e120d88
coverage: 0.886364
learned_at: 2026-10-15 22:43:45
nodes: [PrimitiveBoolean, Note, DF_Integer, Note, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoVAELoader, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoTextEncode, MathExpression|pysssss, INTConstant, SimpleMath+, easy int, PrimitiveNode, WanVideoDecode, GetImageSizeAndCount, easy ifElse, CR Text, CR Text Concatenate, RH_Prompter, ShowText|pysssss, RH_Translator, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, JWInteger, JWInteger, WanVideoEmptyEmbeds, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, Text Multiline]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2 图生视频 -  超级加速晋级版_1967469611824373761.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1967469611824373761.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `PrimitiveBoolean`
- `Note`
- `DF_Integer`
- `Note`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `MathExpression|pysssss`
- `INTConstant`
- `SimpleMath+`
- `easy int`
- `PrimitiveNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `easy ifElse`
- `CR Text`
- `CR Text Concatenate`
- `RH_Prompter`
- `ShowText|pysssss`
- `RH_Translator`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `Text Multiline`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`PrimitiveBoolean`、`DF_Integer`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`MathExpression|pysssss`、`INTConstant`、`SimpleMath+`、`easy int`、`WanVideoDecode`、`GetImageSizeAndCount`、`CR Text`、`CR Text Concatenate`、`RH_Prompter`、`RH_Translator`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`JWInteger`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`Text Multiline`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
