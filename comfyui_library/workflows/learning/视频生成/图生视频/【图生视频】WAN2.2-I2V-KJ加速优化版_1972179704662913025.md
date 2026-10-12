---
key: 视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json
name: 【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json
hash: 1fa9d85b3f9acc21
coverage: 0.72093
learned_at: 2026-10-13 00:04:36
nodes: [RH_Translator, DF_Integer, easy ifElse, ShowText|pysssss, string_util_StrReplace, RH_LLMAPI_NODE, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, GetImageSizeAndCount, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoSampler, WanVideoSampler, JWInteger, LoadWanVideoT5TextEncoder, WanVideoTextEncode, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, Note, PrimitiveNode, easy int, MathExpression|pysssss, INTConstant, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, CreateCFGScheduleFloatList, VHS_VideoCombine, WanVideoVAELoader, WanVideoDecode, PrimitiveBoolean, ShowText|pysssss, Text Multiline, ShowText|pysssss, RH_Translator, WanVideoSetLoRAs, LoadImage, Text Multiline]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, SimpleMath+, Text Multiline, Text Multiline, easy int]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
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

覆盖率 **72%**（31/43）

**有卡**：`RH_Translator`、`DF_Integer`、`string_util_StrReplace`、`RH_LLMAPI_NODE`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`WanVideoImageToVideoEncode`、`WanVideoLoraSelect`、`WanVideoSampler`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`INTConstant`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoDecode`、`PrimitiveBoolean`、`LoadImage`

**缺卡**（6）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`SimpleMath+`、`Text Multiline`、`Text Multiline`、`easy int`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
