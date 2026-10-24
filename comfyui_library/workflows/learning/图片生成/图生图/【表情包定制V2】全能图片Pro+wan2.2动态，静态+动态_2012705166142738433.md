---
key: 图片生成/图生图/【表情包定制V2】全能图片Pro+wan2.2动态，静态+动态_2012705166142738433.json
name: 【表情包定制V2】全能图片Pro+wan2.2动态，静态+动态_2012705166142738433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【表情包定制V2】全能图片Pro+wan2.2动态，静态+动态_2012705166142738433.json
hash: 8a1c49c94ae60601
coverage: 0.722892
learned_at: 2026-10-23 11:51:35
nodes: [PreviewImage, PreviewImage, ImageResize+, ImageResize+, SaveImage, Anything Everywhere, Note, Note, Int, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, GetNode, easy showAnything, easy showAnything, ImageResize+, easy showAnything, CR String To Number, SetNode, SetNode, MathExpression|pysssss, SetNode, Note, Anything Everywhere, CLIPVisionLoader, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, Note, CR String To Number, InversionDemoLazyIndexSwitch, LoadWanVideoT5TextEncoder, WanVideoDecode, easy int, ColorCorrectOfUtils, WanVideoModelLoader, WanVideoVAELoader, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, Note, Note, Note, WanVideoModelLoader, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, JWInteger, WanVideoClipVisionEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoTextEncode, Note, RHHiddenNodes, LoadImage, LoadImage, ImageResize+, CR Text, FluxResolutionNode, Note, VHS_VideoCombine, CR Text, RH_Nano_Banana2_Image2Image]
patterns: []
missing: []
---

# 图片生成/图生图/【表情包定制V2】全能图片Pro+wan2.2动态，静态+动态_2012705166142738433.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【表情包定制V2】全能图片Pro+wan2.2动态，静态+动态_2012705166142738433.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（83 个）：
- `PreviewImage`
- `PreviewImage`
- `ImageResize+`
- `ImageResize+`
- `SaveImage`
- `Anything Everywhere`
- `Note`
- `Note`
- `Int`
- `Anything Everywhere`
- `InversionDemoLazyIndexSwitch`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `easy showAnything`
- `ImageResize+`
- `easy showAnything`
- `CR String To Number`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `Note`
- `Anything Everywhere`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `ImageCASharpening+`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `Note`
- `CR String To Number`
- `InversionDemoLazyIndexSwitch`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `easy int`
- `ColorCorrectOfUtils`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `Note`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `JWInteger`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `Note`
- `RHHiddenNodes`
- `LoadImage`
- `LoadImage`
- `ImageResize+`
- `CR Text`
- `FluxResolutionNode`
- `Note`
- `VHS_VideoCombine`
- `CR Text`
- `RH_Nano_Banana2_Image2Image`

## 知识

覆盖率 **72%**（60/83）

**有卡**：`ImageResize+`、`SaveImage`、`Int`、`InversionDemoLazyIndexSwitch`、`CR String To Number`、`MathExpression|pysssss`、`CLIPVisionLoader`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`easy int`、`ColorCorrectOfUtils`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoImageToVideoEncode`、`JWInteger`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`RHHiddenNodes`、`LoadImage`、`CR Text`、`FluxResolutionNode`、`VHS_VideoCombine`、`RH_Nano_Banana2_Image2Image`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
