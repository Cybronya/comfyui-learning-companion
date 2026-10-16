---
key: 视频生成/图生视频/wan2.2 图生视频_1953992101455548418.json
name: wan2.2 图生视频_1953992101455548418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953992101455548418.json
hash: 6dcfd82d66b246dc
coverage: 0.829787
learned_at: 2026-10-15 22:31:05
nodes: [RH_Translator, Note, Note, PrimitiveBoolean, PrimitiveBoolean, Text Multiline, JWInteger, ShowText|pysssss, RH_Captioner, easy ifElse, easy ifElse, ShowText|pysssss, ShowText|pysssss, Text Multiline, string_util_StrReplace, RH_LLMAPI_NODE, WanVideoBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, CreateCFGScheduleFloatList, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoSampler, INTConstant, MathExpression|pysssss, PrimitiveNode, easy int, WanVideoLoraSelect, DF_Integer, LoadImage, VHS_VideoCombine, RH_Translator]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 图生视频_1953992101455548418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953992101455548418.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（47 个）：
- `RH_Translator`
- `Note`
- `Note`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `Text Multiline`
- `JWInteger`
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
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `INTConstant`
- `MathExpression|pysssss`
- `PrimitiveNode`
- `easy int`
- `WanVideoLoraSelect`
- `DF_Integer`
- `LoadImage`
- `VHS_VideoCombine`
- `RH_Translator`

## 知识

覆盖率 **83%**（39/47）

**有卡**：`RH_Translator`、`PrimitiveBoolean`、`Text Multiline`、`JWInteger`、`RH_Captioner`、`string_util_StrReplace`、`RH_LLMAPI_NODE`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoLoraSelect`、`INTConstant`、`MathExpression|pysssss`、`easy int`、`DF_Integer`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
