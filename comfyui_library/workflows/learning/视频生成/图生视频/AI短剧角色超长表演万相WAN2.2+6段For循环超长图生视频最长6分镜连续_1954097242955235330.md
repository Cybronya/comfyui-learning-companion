---
key: 视频生成/图生视频/AI短剧角色超长表演万相WAN2.2+6段For循环超长图生视频最长6分镜连续_1954097242955235330.json
name: AI短剧角色超长表演万相WAN2.2+6段For循环超长图生视频最长6分镜连续_1954097242955235330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1954097242955235330.json
hash: 76612572277b139c
coverage: 1
learned_at: 2026-10-15 22:31:06
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, TextInput_, TextInput_, Int2String, Bjornulf_ShowStringText, Int2String, Bjornulf_ShowStringText, MathExpression|pysssss, Int, MathExpression|pysssss, Int, TextInput_, LTXVPromptEnhancerLoader, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, LoadImage, VHS_VideoCombine, Bjornulf_ShowStringText, JjkConcat, TextInput_, TextInput_, TextInput_, TextInput_, WanVideoLoraSelect, INTConstant, CreateCFGScheduleFloatList, SimpleMath+, TTP_text_mix, ForLoopClose, GetImageRangeFromBatch, WanVideoContextOptions, LTXVPromptEnhancer, WanVideoModelLoader, WanVideoModelLoader, ImageResizeKJv2, ImageResizeKJ, WanVideoImageToVideoEncode, easy batchAnything, WanVideoTextEncode, VHS_VideoCombine, ForLoopOpen, GridStrings, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/AI短剧角色超长表演万相WAN2.2+6段For循环超长图生视频最长6分镜连续_1954097242955235330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954097242955235330.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（55 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `TextInput_`
- `TextInput_`
- `Int2String`
- `Bjornulf_ShowStringText`
- `Int2String`
- `Bjornulf_ShowStringText`
- `MathExpression|pysssss`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `TextInput_`
- `LTXVPromptEnhancerLoader`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `LoadImage`
- `VHS_VideoCombine`
- `Bjornulf_ShowStringText`
- `JjkConcat`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `WanVideoLoraSelect`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `SimpleMath+`
- `TTP_text_mix`
- `ForLoopClose`
- `GetImageRangeFromBatch`
- `WanVideoContextOptions`
- `LTXVPromptEnhancer`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `ImageResizeKJ`
- `WanVideoImageToVideoEncode`
- `easy batchAnything`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `ForLoopOpen`
- `GridStrings`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（55/55）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`TextInput_`、`Int2String`、`Bjornulf_ShowStringText`、`MathExpression|pysssss`、`Int`、`LTXVPromptEnhancerLoader`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`LoadImage`、`VHS_VideoCombine`、`JjkConcat`、`INTConstant`、`CreateCFGScheduleFloatList`、`SimpleMath+`、`TTP_text_mix`、`ForLoopClose`、`GetImageRangeFromBatch`、`WanVideoContextOptions`、`LTXVPromptEnhancer`、`WanVideoModelLoader`、`ImageResizeKJv2`、`ImageResizeKJ`、`WanVideoImageToVideoEncode`、`easy batchAnything`、`WanVideoTextEncode`、`ForLoopOpen`、`GridStrings`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
