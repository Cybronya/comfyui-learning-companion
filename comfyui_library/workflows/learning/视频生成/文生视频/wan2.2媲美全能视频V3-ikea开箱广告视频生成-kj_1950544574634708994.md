---
key: 视频生成/文生视频/wan2.2媲美全能视频V3-ikea开箱广告视频生成-kj_1950544574634708994.json
name: wan2.2媲美全能视频V3-ikea开箱广告视频生成-kj_1950544574634708994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2媲美全能视频V3-ikea开箱广告视频生成-kj_1950544574634708994.json
hash: 91fb3298054a621f
coverage: 0.837209
learned_at: 2026-10-15 22:43:36
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSampler, WanVideoSetBlockSwap, GetImageSizeAndCount, VHS_VideoCombine, WanVideoDecode, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, WanVideoBlockSwap, Note, Note, Note, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, MathExpression|pysssss, WanVideoVAELoader, WanVideoEmptyEmbeds, LoadImage, Note, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Note, Text Multiline, Primitive integer [Crystools], Text Multiline, easy anythingIndexSwitch, easy showAnything, RH_LLMAPI_NODE, Text Multiline, Text Multiline, StringReplace, Note, Text Multiline, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2媲美全能视频V3-ikea开箱广告视频生成-kj_1950544574634708994.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950544574634708994.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（43 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Note`
- `Note`
- `Note`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MathExpression|pysssss`
- `WanVideoVAELoader`
- `WanVideoEmptyEmbeds`
- `LoadImage`
- `Note`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Note`
- `Text Multiline`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `Text Multiline`
- `Text Multiline`
- `StringReplace`
- `Note`
- `Text Multiline`
- `WanVideoTextEncode`

## 知识

覆盖率 **84%**（36/43）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`Primitive integer [Crystools]`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`MathExpression|pysssss`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`LoadImage`、`Text Multiline`、`easy anythingIndexSwitch`、`RH_LLMAPI_NODE`、`StringReplace`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
