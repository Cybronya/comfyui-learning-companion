---
key: 视频生成/图生视频/图生视频高清版+KJ极速版 Wan2.2 14B 可切换图生视频(升级优化版)_2014248417769295873.json
name: 图生视频高清版+KJ极速版 Wan2.2 14B 可切换图生视频(升级优化版)_2014248417769295873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2014248417769295873.json
hash: ad9a9409ebd40766
coverage: 0.742268
learned_at: 2026-10-15 22:34:34
nodes: [Int, WanVideoLoraSelect, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoVAELoader, RH_LLMAPI_NODE, JjkShowText, WanVideoSampler, WanVideoDecode, WanVideoTextEncode, RH_Captioner, TextCombinerTwo, CR Text Concatenate, RH_Prompter, RH_Prompter, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, WanVideoSetLoRAs, Int, Int, Int, RH_Translator, WanVideoSetLoRAs, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, RunningHub ThinkSound, Bjornulf_ShowInt, ImageResize+, CreateVideo, Bjornulf_ShowInt, PreviewImage, ImpactSwitch, ImageResizeKJv2, ImageResize+, PreviewImage, Bjornulf_ShowInt, Bjornulf_ShowInt, Bjornulf_ShowInt, ImpactSwitch, ImpactSwitch, Bjornulf_ShowInt, JjkText, WanVideoModelLoader, WanVideoModelLoader, Int, Int, Int, Int, Int, Int, Int, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, Note, Int, easy showAnything, MathExpression|pysssss, TextCombinerTwo, TextCombinerTwo, JjkText, JWInteger, Note, LoadImage, Note, ShowText, JjkText, ImpactSwitch, easy cleanGpuUsed, ImageFromBatch+, WanVideoImageToVideoEncode, WanVideoSampler, ImpactSwitch, PreviewImage, Int, SaveVideo, VHS_VideoCombine, ShowText, JjkText, easy showAnything, RH_LLMAPI_NODE, ImpactSwitch, Note, ImpactSwitch, easy anythingIndexSwitch]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频高清版+KJ极速版 Wan2.2 14B 可切换图生视频(升级优化版)_2014248417769295873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2014248417769295873.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（97 个）：
- `Int`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `RH_LLMAPI_NODE`
- `JjkShowText`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTextEncode`
- `RH_Captioner`
- `TextCombinerTwo`
- `CR Text Concatenate`
- `RH_Prompter`
- `RH_Prompter`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `WanVideoSetLoRAs`
- `Int`
- `Int`
- `Int`
- `RH_Translator`
- `WanVideoSetLoRAs`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `RunningHub ThinkSound`
- `Bjornulf_ShowInt`
- `ImageResize+`
- `CreateVideo`
- `Bjornulf_ShowInt`
- `PreviewImage`
- `ImpactSwitch`
- `ImageResizeKJv2`
- `ImageResize+`
- `PreviewImage`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `ImpactSwitch`
- `ImpactSwitch`
- `Bjornulf_ShowInt`
- `JjkText`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Note`
- `Int`
- `easy showAnything`
- `MathExpression|pysssss`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `JjkText`
- `JWInteger`
- `Note`
- `LoadImage`
- `Note`
- `ShowText`
- `JjkText`
- `ImpactSwitch`
- `easy cleanGpuUsed`
- `ImageFromBatch+`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `ImpactSwitch`
- `PreviewImage`
- `Int`
- `SaveVideo`
- `VHS_VideoCombine`
- `ShowText`
- `JjkText`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `Note`
- `ImpactSwitch`
- `easy anythingIndexSwitch`

## 知识

覆盖率 **74%**（72/97）

**有卡**：`Int`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`RH_LLMAPI_NODE`、`JjkShowText`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoTextEncode`、`RH_Captioner`、`TextCombinerTwo`、`CR Text Concatenate`、`RH_Prompter`、`WanVideoSetLoRAs`、`RH_Translator`、`RunningHub ThinkSound`、`Bjornulf_ShowInt`、`ImageResize+`、`CreateVideo`、`ImageResizeKJv2`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`MathExpression|pysssss`、`JWInteger`、`LoadImage`、`ShowText`、`easy cleanGpuUsed`、`ImageFromBatch+`、`WanVideoImageToVideoEncode`、`SaveVideo`、`VHS_VideoCombine`、`easy anythingIndexSwitch`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
