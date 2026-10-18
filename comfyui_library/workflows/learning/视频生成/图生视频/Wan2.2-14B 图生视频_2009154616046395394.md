---
key: 视频生成/图生视频/Wan2.2-14B 图生视频_2009154616046395394.json
name: Wan2.2-14B 图生视频_2009154616046395394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-14B 图生视频_2009154616046395394.json
hash: 990bad54743d8bcd
coverage: 0.734694
learned_at: 2026-10-15 22:34:10
nodes: [Int, WanVideoLoraSelect, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoVAELoader, RH_LLMAPI_NODE, RH_LLMAPI_NODE, easy showAnything, JjkShowText, WanVideoSampler, easy cleanGpuUsed, WanVideoDecode, WanVideoTextEncode, RH_Captioner, TextCombinerTwo, CR Text Concatenate, RH_Prompter, RH_Prompter, ShowText, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, WanVideoSetLoRAs, ImageFromBatch+, Note, Int, Int, Int, RH_Translator, WanVideoSetLoRAs, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, RunningHub ThinkSound, Bjornulf_ShowInt, ImageResize+, WanVideoSampler, WanVideoImageToVideoEncode, CreateVideo, Bjornulf_ShowInt, PreviewImage, PreviewImage, ImpactSwitch, ImageResizeKJv2, ImageResize+, PreviewImage, Bjornulf_ShowInt, Bjornulf_ShowInt, Bjornulf_ShowInt, ImpactSwitch, ImpactSwitch, Bjornulf_ShowInt, JjkText, SaveVideo, Int, WanVideoModelLoader, WanVideoModelLoader, Int, Int, Int, Int, Int, Int, Int, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, Note, Int, easy showAnything, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, MathExpression|pysssss, TextCombinerTwo, TextCombinerTwo, JjkText, JjkText, Note, easy anythingIndexSwitch, JWInteger, Note, JjkText, Fast Groups Muter (rgthree), LoadImage, ShowText]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-14B 图生视频_2009154616046395394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009154616046395394.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（98 个）：
- `Int`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `JjkShowText`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `RH_Captioner`
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
- `WanVideoSetLoRAs`
- `ImageFromBatch+`
- `Note`
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
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `CreateVideo`
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
- `VHS_VideoCombine`
- `Note`
- `Int`
- `easy showAnything`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `MathExpression|pysssss`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `JjkText`
- `JjkText`
- `Note`
- `easy anythingIndexSwitch`
- `JWInteger`
- `Note`
- `JjkText`
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `ShowText`

## 知识

覆盖率 **73%**（72/98）

**有卡**：`Int`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`RH_LLMAPI_NODE`、`JjkShowText`、`WanVideoSampler`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoTextEncode`、`RH_Captioner`、`TextCombinerTwo`、`CR Text Concatenate`、`RH_Prompter`、`ShowText`、`WanVideoSetLoRAs`、`ImageFromBatch+`、`RH_Translator`、`RunningHub ThinkSound`、`Bjornulf_ShowInt`、`ImageResize+`、`WanVideoImageToVideoEncode`、`CreateVideo`、`ImageResizeKJv2`、`SaveVideo`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`MathExpression|pysssss`、`easy anythingIndexSwitch`、`JWInteger`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
