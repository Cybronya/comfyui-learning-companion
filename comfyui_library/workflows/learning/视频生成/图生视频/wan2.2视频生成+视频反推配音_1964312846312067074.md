---
key: 视频生成/图生视频/wan2.2视频生成+视频反推配音_1964312846312067074.json
name: wan2.2视频生成+视频反推配音_1964312846312067074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1964312846312067074.json
hash: 0a6e8f07302895fd
coverage: 0.830508
learned_at: 2026-10-15 22:31:34
nodes: [GetVideoComponents, LayerUtility: ImageScaleByAspectRatio V2, easy clearCacheAll, ImpactSwitch, LoadVideo, RH_Translator, Note, RH_Translator, PrimitiveBoolean, JWInteger, DF_Integer, ShowText|pysssss, RH_Captioner, easy ifElse, easy ifElse, ShowText|pysssss, ShowText|pysssss, Text Multiline, string_util_StrReplace, RH_LLMAPI_NODE, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, WanVideoDecode, WanVideoVAELoader, WanVideoImageToVideoEncode, INTConstant, MathExpression|pysssss, PrimitiveNode, easy int, WanVideoSampler, WanVideoSampler, LoadImage, PrimitiveBoolean, Note, Text Multiline, GetImageSizeAndCount, VHS_VideoCombine, RH_Translator, Text Multiline, AILab_MiniCPM_4_V_Advanced, Text Concatenate, VHS_VideoCombine, PreviewAudio, easy showAnything, HunyuanVideoFoley, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2视频生成+视频反推配音_1964312846312067074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964312846312067074.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（59 个）：
- `GetVideoComponents`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy clearCacheAll`
- `ImpactSwitch`
- `LoadVideo`
- `RH_Translator`
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
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `MathExpression|pysssss`
- `PrimitiveNode`
- `easy int`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadImage`
- `PrimitiveBoolean`
- `Note`
- `Text Multiline`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `RH_Translator`
- `Text Multiline`
- `AILab_MiniCPM_4_V_Advanced`
- `Text Concatenate`
- `VHS_VideoCombine`
- `PreviewAudio`
- `easy showAnything`
- `HunyuanVideoFoley`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`

## 知识

覆盖率 **83%**（49/59）

**有卡**：`GetVideoComponents`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy clearCacheAll`、`LoadVideo`、`RH_Translator`、`PrimitiveBoolean`、`JWInteger`、`DF_Integer`、`RH_Captioner`、`Text Multiline`、`string_util_StrReplace`、`RH_LLMAPI_NODE`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`SimpleMath+`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`INTConstant`、`MathExpression|pysssss`、`easy int`、`WanVideoSampler`、`LoadImage`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`AILab_MiniCPM_4_V_Advanced`、`Text Concatenate`、`PreviewAudio`、`HunyuanVideoFoley`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
