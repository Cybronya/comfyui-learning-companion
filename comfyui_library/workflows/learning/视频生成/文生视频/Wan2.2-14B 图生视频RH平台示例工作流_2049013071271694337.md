---
key: 视频生成/文生视频/Wan2.2-14B 图生视频RH平台示例工作流_2049013071271694337.json
name: Wan2.2-14B 图生视频RH平台示例工作流_2049013071271694337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-14B 图生视频RH平台示例工作流_2049013071271694337.json
hash: fdbdbc4a5fa0a49d
coverage: 0.653061
learned_at: 2026-10-11 19:49:43
nodes: [Int, WanVideoLoraSelect, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoVAELoader, Int, RH_LLMAPI_NODE, RH_LLMAPI_NODE, easy showAnything, JjkShowText, easy cleanGpuUsed, WanVideoDecode, RH_Captioner, JjkText, JjkText, easy showAnything, TextCombinerTwo, TextCombinerTwo, CR Text Concatenate, RH_Prompter, RH_Prompter, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Note, MathExpression|pysssss, WanVideoSetLoRAs, ImageFromBatch+, Int, Int, Int, Note, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, RunningHub ThinkSound, Bjornulf_ShowInt, WanVideoImageToVideoEncode, CreateVideo, Fast Groups Muter (rgthree), Bjornulf_ShowInt, PreviewImage, PreviewImage, ImpactSwitch, ImageResizeKJv2, ImageResize+, PreviewImage, Bjornulf_ShowInt, Bjornulf_ShowInt, Bjornulf_ShowInt, ImpactSwitch, ImpactSwitch, Bjornulf_ShowInt, TextCombinerTwo, JjkText, SaveVideo, Int, WanVideoModelLoader, Int, Int, Int, Int, Int, Int, Int, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, Note, JWInteger, ImpactSwitch, ImpactSwitch, Note, RH_Translator, ShowText, JjkText, LoadImage, VHS_VideoCombine, ShowText, easy anythingIndexSwitch, WanVideoTextEncode, WanVideoSampler, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, ImageResize+, ImpactSwitch, ImpactSwitch]
patterns: []
missing: [CR Text Concatenate, ImageFromBatch+, MathExpression|pysssss, RunningHub ThinkSound, easy anythingIndexSwitch, easy cleanGpuUsed, ImageResize+, ImageResize+]
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `RunningHub ThinkSound` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2-14B 图生视频RH平台示例工作流_2049013071271694337.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-14B 图生视频RH平台示例工作流_2049013071271694337.json`

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
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `RH_Captioner`
- `JjkText`
- `JjkText`
- `easy showAnything`
- `TextCombinerTwo`
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
- `Note`
- `MathExpression|pysssss`
- `WanVideoSetLoRAs`
- `ImageFromBatch+`
- `Int`
- `Int`
- `Int`
- `Note`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `RunningHub ThinkSound`
- `Bjornulf_ShowInt`
- `WanVideoImageToVideoEncode`
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
- `TextCombinerTwo`
- `JjkText`
- `SaveVideo`
- `Int`
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
- `Note`
- `JWInteger`
- `ImpactSwitch`
- `ImpactSwitch`
- `Note`
- `RH_Translator`
- `ShowText`
- `JjkText`
- `LoadImage`
- `VHS_VideoCombine`
- `ShowText`
- `easy anythingIndexSwitch`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `ImageResize+`
- `ImpactSwitch`
- `ImpactSwitch`

## 知识

覆盖率 **65%**（64/98）

**有卡**：`Int`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`RH_LLMAPI_NODE`、`JjkShowText`、`WanVideoDecode`、`RH_Captioner`、`TextCombinerTwo`、`RH_Prompter`、`WanVideoSetLoRAs`、`Bjornulf_ShowInt`、`WanVideoImageToVideoEncode`、`CreateVideo`、`ImageResizeKJv2`、`SaveVideo`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`JWInteger`、`RH_Translator`、`ShowText`、`LoadImage`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoSampler`

**缺卡**（8）：`CR Text Concatenate`、`ImageFromBatch+`、`MathExpression|pysssss`、`RunningHub ThinkSound`、`easy anythingIndexSwitch`、`easy cleanGpuUsed`、`ImageResize+`、`ImageResize+`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `RunningHub ThinkSound` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
