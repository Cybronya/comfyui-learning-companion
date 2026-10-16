---
key: 视频生成/图生视频/Wan2.2-14B 图生视频-极速版_1950424438283091970.json
name: Wan2.2-14B 图生视频-极速版_1950424438283091970.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950424438283091970.json
hash: 10a335d28784cb20
coverage: 0.785714
learned_at: 2026-10-15 22:30:54
nodes: [JWInteger, PreviewImage, RH_Translator, MathExpression|pysssss, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoDecode, WanVideoSampler, WanVideoVAELoader, easy showAnything, LoadImage, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoSampler, easy showAnything, RH_Captioner, easy showAnything, TextCombinerTwo, JjkText, TextCombinerTwo, TextCombinerTwo, JjkText, ImageResize+, ImpactSwitch, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, WanVideoImageToVideoEncode, VHS_VideoCombine, ImpactSwitch, PreviewImage, ImageResize+, easy anythingIndexSwitch, Note, RH_Prompter, TextCombinerTwo, WanVideoModelLoader, WanVideoModelLoader, JjkText]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-14B 图生视频-极速版_1950424438283091970.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950424438283091970.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（56 个）：
- `JWInteger`
- `PreviewImage`
- `RH_Translator`
- `MathExpression|pysssss`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `easy showAnything`
- `LoadImage`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `easy showAnything`
- `RH_Captioner`
- `easy showAnything`
- `TextCombinerTwo`
- `JjkText`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `JjkText`
- `ImageResize+`
- `ImpactSwitch`
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
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `PreviewImage`
- `ImageResize+`
- `easy anythingIndexSwitch`
- `Note`
- `RH_Prompter`
- `TextCombinerTwo`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `JjkText`

## 知识

覆盖率 **79%**（44/56）

**有卡**：`JWInteger`、`RH_Translator`、`MathExpression|pysssss`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVAELoader`、`LoadImage`、`WanVideoTextEncode`、`RH_Captioner`、`TextCombinerTwo`、`ImageResize+`、`Int`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`RH_Prompter`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
