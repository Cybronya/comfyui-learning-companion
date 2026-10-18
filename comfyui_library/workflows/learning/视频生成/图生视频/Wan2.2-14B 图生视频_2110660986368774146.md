---
key: 视频生成/图生视频/Wan2.2-14B 图生视频_2110660986368774146.json
name: Wan2.2-14B 图生视频_2110660986368774146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-14B 图生视频_2110660986368774146.json
hash: ec009024676b7e17
coverage: 0.734694
learned_at: 2026-10-18 00:23:58
nodes: [Int, WanVideoLoraSelect, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoVAELoader, Int, RH_LLMAPI_NODE, RH_LLMAPI_NODE, easy showAnything, JjkShowText, WanVideoSampler, easy cleanGpuUsed, WanVideoDecode, WanVideoTextEncode, RH_Captioner, JjkText, JjkText, easy showAnything, TextCombinerTwo, TextCombinerTwo, CR Text Concatenate, RH_Prompter, RH_Prompter, ShowText, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Note, MathExpression|pysssss, JWInteger, WanVideoSetLoRAs, ImageFromBatch+, Note, Note, Int, Int, Int, RH_Translator, WanVideoSetLoRAs, Note, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, RunningHub ThinkSound, Bjornulf_ShowInt, ImageResize+, WanVideoSampler, WanVideoImageToVideoEncode, VHS_VideoCombine, CreateVideo, Fast Groups Muter (rgthree), Bjornulf_ShowInt, PreviewImage, PreviewImage, ImpactSwitch, ImageResizeKJv2, ImageResize+, PreviewImage, Bjornulf_ShowInt, Bjornulf_ShowInt, Bjornulf_ShowInt, ImpactSwitch, ImpactSwitch, Bjornulf_ShowInt, ImpactSwitch, ShowText, TextCombinerTwo, JjkText, SaveVideo, Int, WanVideoModelLoader, WanVideoModelLoader, Int, Int, Int, Int, Int, Int, Int, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, easy anythingIndexSwitch, LoadImage, ImpactSwitch, JjkText]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-14B 图生视频_2110660986368774146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2-14B 图生视频_2110660986368774146.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（98 个）：
- `Int`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `Int`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `JjkShowText`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `RH_Captioner`
- `JjkText`
- `JjkText`
- `easy showAnything`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `CR Text Concatenate`
- `RH_Prompter`
- `RH_Prompter`
- `ShowText`
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
- `Note`
- `MathExpression|pysssss`
- `JWInteger`
- `WanVideoSetLoRAs`
- `ImageFromBatch+`
- `Note`
- `Note`
- `Int`
- `Int`
- `Int`
- `RH_Translator`
- `WanVideoSetLoRAs`
- `Note`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `RunningHub ThinkSound`
- `Bjornulf_ShowInt`
- `ImageResize+`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`
- `CreateVideo`
- `Fast Groups Muter (rgthree)`
- `Bjornulf_ShowInt`
- `PreviewImage`
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
- `ImpactSwitch`
- `ShowText`
- `TextCombinerTwo`
- `JjkText`
- `SaveVideo`
- `Int`
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
- `easy anythingIndexSwitch`
- `LoadImage`
- `ImpactSwitch`
- `JjkText`

## 知识

覆盖率 **73%**（72/98）

**有卡**：`Int`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`RH_LLMAPI_NODE`、`JjkShowText`、`WanVideoSampler`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoTextEncode`、`RH_Captioner`、`TextCombinerTwo`、`CR Text Concatenate`、`RH_Prompter`、`ShowText`、`MathExpression|pysssss`、`JWInteger`、`WanVideoSetLoRAs`、`ImageFromBatch+`、`RH_Translator`、`RunningHub ThinkSound`、`Bjornulf_ShowInt`、`ImageResize+`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`CreateVideo`、`ImageResizeKJv2`、`SaveVideo`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`easy anythingIndexSwitch`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
