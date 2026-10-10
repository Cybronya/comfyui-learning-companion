---
key: 视频生成/文生视频/wan2.2媲美全能视频V3-ikea开箱广告视频生成-kj_1971495513445089282.json
name: wan2.2媲美全能视频V3-ikea开箱广告视频生成-kj_1971495513445089282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2媲美全能视频V3-ikea开箱广告视频生成-kj_1971495513445089282.json
hash: f5eaf7037bd11130
coverage: 0.534884
learned_at: 2026-10-10 23:09:45
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSampler, WanVideoSetBlockSwap, GetImageSizeAndCount, VHS_VideoCombine, WanVideoDecode, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, WanVideoBlockSwap, Note, Note, Note, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, MathExpression|pysssss, WanVideoVAELoader, WanVideoEmptyEmbeds, LoadImage, Note, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Note, Text Multiline, Primitive integer [Crystools], Text Multiline, easy anythingIndexSwitch, easy showAnything, RH_LLMAPI_NODE, Text Multiline, Text Multiline, StringReplace, Note, Text Multiline, WanVideoTextEncode]
patterns: []
missing: [MathExpression|pysssss, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Text Multiline, Text Multiline, Text Multiline, Text Multiline, Text Multiline, easy anythingIndexSwitch]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2媲美全能视频V3-ikea开箱广告视频生成-kj_1971495513445089282.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2媲美全能视频V3-ikea开箱广告视频生成-kj_1971495513445089282.json`

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

覆盖率 **53%**（23/43）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`LoadImage`、`RH_LLMAPI_NODE`、`StringReplace`、`WanVideoTextEncode`

**缺卡**（13）：`MathExpression|pysssss`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Text Multiline`、`Text Multiline`、`Text Multiline`、`Text Multiline`、`Text Multiline`、`easy anythingIndexSwitch`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
