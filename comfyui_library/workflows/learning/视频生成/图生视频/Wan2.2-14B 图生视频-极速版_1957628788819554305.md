---
key: 视频生成/图生视频/Wan2.2-14B 图生视频-极速版_1957628788819554305.json
name: Wan2.2-14B 图生视频-极速版_1957628788819554305.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1957628788819554305.json
hash: 384d176d2da8d843
coverage: 0.745455
learned_at: 2026-10-15 22:31:17
nodes: [JWInteger, PreviewImage, MathExpression|pysssss, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoSampler, WanVideoVAELoader, LoadImage, WanVideoTextEncode, WanVideoSampler, ImpactSwitch, Int, WanVideoImageToVideoEncode, ImageResize+, ImpactSwitch, Int, Int, Int, Int, Int, ImageResize+, Int, Int, Int, Int, RH_Captioner, easy showAnything, easy anythingIndexSwitch, TextCombinerTwo, TextCombinerTwo, TextCombinerTwo, JjkText, easy showAnything, Note, JjkText, RH_Prompter, easy showAnything, easy showAnything, easy showAnything, RH_Translator, WanVideoDecode, RH_Prompter, TextCombinerTwo, JjkText, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-14B 图生视频-极速版_1957628788819554305.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957628788819554305.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（55 个）：
- `JWInteger`
- `PreviewImage`
- `MathExpression|pysssss`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `LoadImage`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `ImpactSwitch`
- `Int`
- `WanVideoImageToVideoEncode`
- `ImageResize+`
- `ImpactSwitch`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `ImageResize+`
- `Int`
- `Int`
- `Int`
- `Int`
- `RH_Captioner`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `JjkText`
- `easy showAnything`
- `Note`
- `JjkText`
- `RH_Prompter`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `RH_Translator`
- `WanVideoDecode`
- `RH_Prompter`
- `TextCombinerTwo`
- `JjkText`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`

## 知识

覆盖率 **75%**（41/55）

**有卡**：`JWInteger`、`MathExpression|pysssss`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoVAELoader`、`LoadImage`、`WanVideoTextEncode`、`Int`、`WanVideoImageToVideoEncode`、`ImageResize+`、`RH_Captioner`、`easy anythingIndexSwitch`、`TextCombinerTwo`、`RH_Prompter`、`RH_Translator`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
