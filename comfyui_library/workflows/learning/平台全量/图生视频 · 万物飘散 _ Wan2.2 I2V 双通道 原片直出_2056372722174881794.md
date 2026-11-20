---
key: 平台全量/图生视频 · 万物飘散 _ Wan2.2 I2V 双通道 原片直出_2056372722174881794.json
name: 图生视频 · 万物飘散 _ Wan2.2 I2V 双通道 原片直出_2056372722174881794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图生视频 · 万物飘散 _ Wan2.2 I2V 双通道 原片直出_2056372722174881794.json
hash: 83bdff7276c83ca9
coverage: 0.7
learned_at: 2026-11-14 01:56:22
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoSampler, WanVideoVAELoader, GetImageSizeAndCount, WanVideoDecode, CLIPVisionLoader, SetNode, WanVideoTeaCache, CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, Text Concatenate, WanVideoClipVisionEncode, WanVideoSampler, INTConstant, WanVideoImageToVideoEncode, GetNode, TextInput_, WanVideoModelLoader, WanVideoLoraSelect, INTConstant, ImageResizeKJv2, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTextEncode, Qwen3_VQA, GetNode, SetNode, SetNode, GetNode, SetNode, JWInteger, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, TextInput_, TextInput_, Text, CLIPTextEncode, SetNode, Text, CLIPTextEncode, CheckpointLoaderSimple, CLIPTextEncode, easy showAnything, LoadImage, VHS_VideoCombine, TextInput_, MathExpression|pysssss]
patterns: []
missing: []
parameters: {"checkpoint": "Lock_8.32.safetensors"}
---

# 平台全量/图生视频 · 万物飘散 _ Wan2.2 I2V 双通道 原片直出_2056372722174881794.json

> 来源文件 `comfyui_library/workflows/平台全量/图生视频 · 万物飘散 _ Wan2.2 I2V 双通道 原片直出_2056372722174881794.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（60 个）：
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoTeaCache`
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `Text Concatenate`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `TextInput_`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `INTConstant`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `Qwen3_VQA`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `JWInteger`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `TextInput_`
- `TextInput_`
- `Text`
- `CLIPTextEncode` ★核心
- `SetNode`
- `Text`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `LoadImage`
- `VHS_VideoCombine`
- `TextInput_`
- `MathExpression|pysssss`

## 关键参数

- `checkpoint` = `Lock_8.32.safetensors`

## 知识

覆盖率 **70%**（42/60）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoDecode`、`CLIPVisionLoader`、`WanVideoTeaCache`、`CreateCFGScheduleFloatList`、`LoadWanVideoT5TextEncoder`、`Text Concatenate`、`WanVideoClipVisionEncode`、`INTConstant`、`WanVideoImageToVideoEncode`、`TextInput_`、`WanVideoModelLoader`、`ImageResizeKJv2`、`WanVideoTextEncode`、`Qwen3_VQA`、`JWInteger`、`Text`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LoadImage`、`VHS_VideoCombine`、`MathExpression|pysssss`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode
