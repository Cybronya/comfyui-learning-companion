---
key: 视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json
name: 【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json
hash: 1fa9d85b3f9acc21
coverage: 0.860465
learned_at: 2026-10-15 22:43:00
nodes: [RH_Translator, DF_Integer, easy ifElse, ShowText|pysssss, string_util_StrReplace, RH_LLMAPI_NODE, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, GetImageSizeAndCount, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoSampler, WanVideoSampler, JWInteger, LoadWanVideoT5TextEncoder, WanVideoTextEncode, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, Note, PrimitiveNode, easy int, MathExpression|pysssss, INTConstant, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, CreateCFGScheduleFloatList, VHS_VideoCombine, WanVideoVAELoader, WanVideoDecode, PrimitiveBoolean, ShowText|pysssss, Text Multiline, ShowText|pysssss, RH_Translator, WanVideoSetLoRAs, LoadImage, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（43 个）：
- `RH_Translator`
- `DF_Integer`
- `easy ifElse`
- `ShowText|pysssss`
- `string_util_StrReplace`
- `RH_LLMAPI_NODE`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `Note`
- `PrimitiveNode`
- `easy int`
- `MathExpression|pysssss`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `PrimitiveBoolean`
- `ShowText|pysssss`
- `Text Multiline`
- `ShowText|pysssss`
- `RH_Translator`
- `WanVideoSetLoRAs`
- `LoadImage`
- `Text Multiline`

## 知识

覆盖率 **86%**（37/43）

**有卡**：`RH_Translator`、`DF_Integer`、`string_util_StrReplace`、`RH_LLMAPI_NODE`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`WanVideoImageToVideoEncode`、`WanVideoLoraSelect`、`WanVideoSampler`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`easy int`、`MathExpression|pysssss`、`INTConstant`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoDecode`、`PrimitiveBoolean`、`Text Multiline`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
