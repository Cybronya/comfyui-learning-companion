---
key: 视频生成/图生视频/Wan2.2-14B 图生视频_1956368575927910401.json
name: Wan2.2-14B 图生视频_1956368575927910401.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956368575927910401.json
hash: 93cea952c34b6738
coverage: 0.742857
learned_at: 2026-10-15 22:31:13
nodes: [Int, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoVAELoader, Int, RH_LLMAPI_NODE, WanVideoBlockSwap, WanVideoBlockSwap, RH_LLMAPI_NODE, WanVideoSetBlockSwap, WanVideoSetBlockSwap, easy showAnything, JjkShowText, WanVideoLoraSelect, WanVideoDecode, WanVideoTextEncode, JjkText, JjkText, easy showAnything, TextCombinerTwo, TextCombinerTwo, TextCombinerTwo, JjkText, CR Text Concatenate, RH_Prompter, RH_Prompter, ShowText, Int, Int, Int, Int, Int, Int, Int, Int, Note, MathExpression|pysssss, JWInteger, WanVideoSetLoRAs, ImageFromBatch+, SaveVideo, Note, Note, Int, Int, ShowText, Int, Int, Int, RH_Translator, Note, Int, Int, Int, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, RunningHub ThinkSound, Bjornulf_ShowInt, WanVideoSampler, WanVideoImageToVideoEncode, VHS_VideoCombine, CreateVideo, Fast Groups Muter (rgthree), Bjornulf_ShowInt, ImpactSwitch, ImageResize+, PreviewImage, Bjornulf_ShowInt, Bjornulf_ShowInt, Bjornulf_ShowInt, ImpactSwitch, ImpactSwitch, Bjornulf_ShowInt, ImpactSwitch, PreviewImage, PreviewImage, ImageResizeKJv2, ImageResize+, RH_Captioner, PreviewImage, easy anythingIndexSwitch, JjkText, Load Image From Url (mtb), String, WanVideoSetLoRAs, easy cleanGpuUsed, WanVideoSampler, easy cleanGpuUsed, Int, Int, Int, ImpactSwitch, Int, Int, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-14B 图生视频_1956368575927910401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956368575927910401.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（105 个）：
- `Int`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `Int`
- `RH_LLMAPI_NODE`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `RH_LLMAPI_NODE`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `easy showAnything`
- `JjkShowText`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `JjkText`
- `JjkText`
- `easy showAnything`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `JjkText`
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
- `Note`
- `MathExpression|pysssss`
- `JWInteger`
- `WanVideoSetLoRAs`
- `ImageFromBatch+`
- `SaveVideo`
- `Note`
- `Note`
- `Int`
- `Int`
- `ShowText`
- `Int`
- `Int`
- `Int`
- `RH_Translator`
- `Note`
- `Int`
- `Int`
- `Int`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `RunningHub ThinkSound`
- `Bjornulf_ShowInt`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`
- `CreateVideo`
- `Fast Groups Muter (rgthree)`
- `Bjornulf_ShowInt`
- `ImpactSwitch`
- `ImageResize+`
- `PreviewImage`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `ImpactSwitch`
- `ImpactSwitch`
- `Bjornulf_ShowInt`
- `ImpactSwitch`
- `PreviewImage`
- `PreviewImage`
- `ImageResizeKJv2`
- `ImageResize+`
- `RH_Captioner`
- `PreviewImage`
- `easy anythingIndexSwitch`
- `JjkText`
- `Load Image From Url (mtb)`
- `String`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `Int`
- `Int`
- `Int`
- `ImpactSwitch`
- `Int`
- `Int`
- `Int`

## 知识

覆盖率 **74%**（78/105）

**有卡**：`Int`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`RH_LLMAPI_NODE`、`WanVideoSetBlockSwap`、`JjkShowText`、`WanVideoDecode`、`WanVideoTextEncode`、`TextCombinerTwo`、`CR Text Concatenate`、`RH_Prompter`、`ShowText`、`MathExpression|pysssss`、`JWInteger`、`WanVideoSetLoRAs`、`ImageFromBatch+`、`SaveVideo`、`RH_Translator`、`RunningHub ThinkSound`、`Bjornulf_ShowInt`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`CreateVideo`、`ImageResize+`、`ImageResizeKJv2`、`RH_Captioner`、`easy anythingIndexSwitch`、`Load Image From Url (mtb)`、`String`、`easy cleanGpuUsed`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
