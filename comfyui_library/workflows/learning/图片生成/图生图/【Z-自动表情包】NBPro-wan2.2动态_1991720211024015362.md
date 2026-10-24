---
key: 图片生成/图生图/【Z-自动表情包】NBPro-wan2.2动态_1991720211024015362.json
name: 【Z-自动表情包】NBPro-wan2.2动态_1991720211024015362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Z-自动表情包】NBPro-wan2.2动态_1991720211024015362.json
hash: bb429cd9628ae4ed
coverage: 0.633028
learned_at: 2026-10-23 11:49:06
nodes: [PreviewImage, ImageResize+, Anything Everywhere, Note, Note, Note, Int, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, GetNode, easy showAnything, easy showAnything, ImageResize+, easy showAnything, CR String To Number, SetNode, SetNode, MathExpression|pysssss, SetNode, Note, Anything Everywhere, CLIPVisionLoader, LayerUtility: PurgeVRAM V2, ImageCASharpening+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, Note, CR String To Number, InversionDemoLazyIndexSwitch, LoadWanVideoT5TextEncoder, WanVideoDecode, ColorCorrectOfUtils, WanVideoModelLoader, WanVideoVAELoader, Note, Note, WanVideoModelLoader, JWInteger, WanVideoClipVisionEncode, Note, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoLoraSelect, Note, CR Text, FluxResolutionNode, ImageResize+, LoadImage, easy int, SetNode, GetNode, GetNode, WanVideoImageToVideoEncode, SetNode, GetNode, easy cleanGpuUsed, SetNode, SetNode, easy cleanGpuUsed, GetNode, GetNode, GetNode, Note, PreviewAny, SaveImage, easy imageCropFromMask, GrowMaskWithBlur, EG_ZZ_TMTX, Sa2VANodeTpl, VHS_VideoCombine, CogVideoEnhanceAVideo, WanVideoSampler, WanVideoSampler, PreviewImage, ImageResize+, SaveImage, RH_Nano_Banana2_Image2Image, SetNode, LoadImage, GetNode, GetNode, Qwen3_VQA_Plus, RMBG, SimpleMath+, SetNode, CR Text, CR Text, Fast Groups Muter (rgthree), WanVideoTextEncode, WanVideoSLG, WanVideoExperimentalArgs, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, Float]
patterns: []
missing: []
---

# 图片生成/图生图/【Z-自动表情包】NBPro-wan2.2动态_1991720211024015362.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【Z-自动表情包】NBPro-wan2.2动态_1991720211024015362.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（109 个）：
- `PreviewImage`
- `ImageResize+`
- `Anything Everywhere`
- `Note`
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
- `ColorCorrectOfUtils`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `JWInteger`
- `WanVideoClipVisionEncode`
- `Note`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `Note`
- `CR Text`
- `FluxResolutionNode`
- `ImageResize+`
- `LoadImage`
- `easy int`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `PreviewAny`
- `SaveImage`
- `easy imageCropFromMask`
- `GrowMaskWithBlur`
- `EG_ZZ_TMTX`
- `Sa2VANodeTpl`
- `VHS_VideoCombine`
- `CogVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PreviewImage`
- `ImageResize+`
- `SaveImage`
- `RH_Nano_Banana2_Image2Image`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `Qwen3_VQA_Plus`
- `RMBG`
- `SimpleMath+`
- `SetNode`
- `CR Text`
- `CR Text`
- `Fast Groups Muter (rgthree)`
- `WanVideoTextEncode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `Float`

## 知识

覆盖率 **63%**（69/109）

**有卡**：`ImageResize+`、`Int`、`InversionDemoLazyIndexSwitch`、`CR String To Number`、`MathExpression|pysssss`、`CLIPVisionLoader`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`ColorCorrectOfUtils`、`WanVideoModelLoader`、`WanVideoVAELoader`、`JWInteger`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`CR Text`、`FluxResolutionNode`、`LoadImage`、`easy int`、`WanVideoImageToVideoEncode`、`easy cleanGpuUsed`、`SaveImage`、`easy imageCropFromMask`、`GrowMaskWithBlur`、`EG_ZZ_TMTX`、`Sa2VANodeTpl`、`VHS_VideoCombine`、`CogVideoEnhanceAVideo`、`WanVideoSampler`、`RH_Nano_Banana2_Image2Image`、`Qwen3_VQA_Plus`、`RMBG`、`SimpleMath+`、`WanVideoTextEncode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`Float`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
