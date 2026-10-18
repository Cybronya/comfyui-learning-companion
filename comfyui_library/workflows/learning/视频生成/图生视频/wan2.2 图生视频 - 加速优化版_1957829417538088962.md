---
key: 视频生成/图生视频/wan2.2 图生视频 - 加速优化版_1957829417538088962.json
name: wan2.2 图生视频 - 加速优化版_1957829417538088962.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 图生视频 - 加速优化版_1957829417538088962.json
hash: 7e95ca5bcf38449c
coverage: 0.829787
learned_at: 2026-10-15 22:31:18
nodes: [RH_Translator, Note, Note, RH_Translator, PrimitiveBoolean, JWInteger, DF_Integer, ShowText|pysssss, RH_Captioner, easy ifElse, easy ifElse, ShowText|pysssss, ShowText|pysssss, Text Multiline, string_util_StrReplace, RH_LLMAPI_NODE, WanVideoBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTorchCompileSettings, CreateCFGScheduleFloatList, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, WanVideoDecode, GetImageSizeAndCount, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoLoraSelect, VHS_VideoCombine, INTConstant, MathExpression|pysssss, PrimitiveNode, easy int, WanVideoSampler, WanVideoSampler, PrimitiveBoolean, LoadImage, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 图生视频 - 加速优化版_1957829417538088962.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957829417538088962.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `RH_Translator`
- `Note`
- `Note`
- `RH_Translator`
- `PrimitiveBoolean`
- `JWInteger`
- `DF_Integer`
- `ShowText|pysssss`
- `RH_Captioner`
- `easy ifElse`
- `easy ifElse`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `Text Multiline`
- `string_util_StrReplace`
- `RH_LLMAPI_NODE`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `INTConstant`
- `MathExpression|pysssss`
- `PrimitiveNode`
- `easy int`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PrimitiveBoolean`
- `LoadImage`
- `Text Multiline`

## 知识

覆盖率 **83%**（39/47）

**有卡**：`RH_Translator`、`PrimitiveBoolean`、`JWInteger`、`DF_Integer`、`RH_Captioner`、`Text Multiline`、`string_util_StrReplace`、`RH_LLMAPI_NODE`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`INTConstant`、`MathExpression|pysssss`、`easy int`、`WanVideoSampler`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
